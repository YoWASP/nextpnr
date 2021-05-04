#!/bin/sh -ex

export SOURCE_DATE_EPOCH=$(git log -1 --format=%ct)

WASI_SDK=wasi-sdk-11.0
WASI_SDK_URL=https://github.com/WebAssembly/wasi-sdk/releases/download/wasi-sdk-11/wasi-sdk-11.0-linux.tar.gz
if ! [ -d ${WASI_SDK} ]; then curl -L ${WASI_SDK_URL} | tar xzf -; fi
WASI_SDK_PATH=$(pwd)/${WASI_SDK}

BOOST=boost_1_75_0
BOOST_URL=https://boostorg.jfrog.io/artifactory/main/release/1.75.0/source/boost_1_75_0.tar.gz
if ! [ -d ${BOOST} ]; then 
  curl -L ${BOOST_URL} | tar xzf -
  # not necessary once boost 1.76.0 is released
  patch -d ${BOOST} -p1 <boost-1.75.0-wasi.patch
fi

EIGEN=eigen-3.3.9
EIGEN_URL=https://gitlab.com/libeigen/eigen/-/archive/3.3.9/eigen-3.3.9.tar.gz
if ! [ -d ${EIGEN} ]; then curl -L ${EIGEN_URL} | tar xzf -; fi

cat >Toolchain-WASI.cmake <<END
cmake_minimum_required(VERSION 3.4.0)

set(WASI TRUE)

set(CMAKE_SYSTEM_NAME Generic)
set(CMAKE_SYSTEM_VERSION 1)
set(CMAKE_SYSTEM_PROCESSOR wasm32)

set(CMAKE_C_COMPILER ccache ${WASI_SDK_PATH}/bin/clang)
set(CMAKE_CXX_COMPILER ccache ${WASI_SDK_PATH}/bin/clang++)
set(CMAKE_LINKER ${WASI_SDK_PATH}/bin/wasm-ld CACHE STRING "wasienv build")
set(CMAKE_AR ${WASI_SDK_PATH}/bin/ar CACHE STRING "wasienv build")
set(CMAKE_RANLIB ${WASI_SDK_PATH}/bin/ranlib CACHE STRING "wasienv build")

set(CMAKE_C_FLAGS "--sysroot ${WASI_SDK_PATH}/share/wasi-sysroot")
set(CMAKE_CXX_FLAGS "--sysroot ${WASI_SDK_PATH}/share/wasi-sysroot")
set(CMAKE_EXE_LINKER_FLAGS "-Wl,--no-threads -Wl,--strip-all" CACHE STRING "wasienv build")

set(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
set(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
set(CMAKE_FIND_ROOT_PATH_MODE_PACKAGE ONLY)
END

if ! [ -f ${BOOST}/tools/build/src/engine/b2 ]; then
  (cd ${BOOST}/tools/build/src/engine && ./build.sh);
fi
cat >${BOOST}/project-config.jam <<END
using clang : : ccache clang++ --sysroot ${WASI_SDK_PATH}/share/wasi-sysroot -D_WASI_EMULATED_MMAN -DBOOST_NO_EXCEPTIONS -DBOOST_SP_NO_ATOMIC_ACCESS -DBOOST_AC_DISABLE_THREADS -DBOOST_NO_CXX11_HDR_MUTEX -DBOOST_HAS_UNISTD_H ;
project : default-build <toolset>clang ;

libraries = --with-program_options --with-iostreams --with-filesystem --with-system ;
END
(cd ${BOOST} && PATH=${WASI_SDK_PATH}/bin:$PATH ./tools/build/src/engine/b2 threading=single link=static)

cmake -B eigen-build -S ${EIGEN} -DCMAKE_INSTALL_PREFIX=$(pwd)/eigen-prefix
make -C eigen-build install

make -C icestorm-src EXE=".wasm" \
  CXX="ccache ${WASI_SDK_PATH}/bin/clang++" \
  CXXFLAGS="--sysroot ${WASI_SDK_PATH}/share/wasi-sysroot -fno-exceptions -flto" \
  LDFLAGS="--sysroot ${WASI_SDK_PATH}/share/wasi-sysroot -fno-exceptions -flto -Wl,--strip-all" \
  SUBDIRS="icebox icepack icemulti icepll icebram" \
  PREFIX="" DESTDIR=$(pwd)/icestorm-prefix \
  install
cp icestorm-src/icefuzz/timings_*.txt $(pwd)/icestorm-prefix/share/icebox/

cmake -B prjtrellis-build -S prjtrellis-src/libtrellis \
  -DCMAKE_TOOLCHAIN_FILE=../Toolchain-WASI.cmake \
  -DBOOST_ROOT=$(pwd)/${BOOST} \
  -DSTATIC_BUILD=ON \
  -DBUILD_SHARED=OFF \
  -DBUILD_PYTHON=OFF
cmake --build prjtrellis-build

cmake -B libtrellis-build -S prjtrellis-src/libtrellis \
  -DCMAKE_INSTALL_PREFIX=$(pwd)/libtrellis-prefix
make -C libtrellis-build install

cmake -B nextpnr-bba-build -S nextpnr-src/bba
cmake --build nextpnr-bba-build

mkdir -p nextpnr-build
cmake -B nextpnr-build -S nextpnr-src \
  -DCMAKE_TOOLCHAIN_FILE=../Toolchain-WASI.cmake \
  -DCMAKE_CXX_COMPILER_LAUNCHER=ccache \
  -DSTATIC_BUILD=ON \
  -DBOOST_ROOT=$(pwd)/${BOOST} \
  -DEigen3_DIR=$(pwd)/eigen-prefix/share/eigen3/cmake \
  -DBBA_IMPORT=$(pwd)/nextpnr-bba-build/bba-export.cmake \
  -DBUILD_GUI=OFF \
  -DBUILD_PYTHON=OFF \
  -DEXTERNAL_CHIPDB=ON \
  -DEXTERNAL_CHIPDB_ROOT=/share \
  -DARCH="ice40;ecp5" \
  -DICESTORM_INSTALL_PREFIX=$(pwd)/icestorm-prefix \
  -DTRELLIS_INSTALL_PREFIX=$(pwd)/libtrellis-prefix
cmake --build nextpnr-build
