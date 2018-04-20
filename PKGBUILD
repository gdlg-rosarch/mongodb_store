# Script generated with Bloom
pkgdesc="ROS - A wrapper for the libmongocxx for mongodb_store"
url='https://github.com/mongodb/mongo-cxx-driver'

pkgname='ros-kinetic-libmongocxx-ros'
pkgver='0.3.7_1'
pkgrel=1
arch=('any')
license=('Apache'
)

makedepends=('boost'
'ca-certificates'
'git'
'openssl'
'ros-kinetic-catkin'
'ros-kinetic-roscpp'
'scons'
)

depends=('boost'
'openssl'
'ros-kinetic-roscpp'
)

conflicts=()
replaces=()

_dir=libmongocxx_ros
source=()
md5sums=()

prepare() {
    cp -R $startdir/libmongocxx_ros $srcdir/libmongocxx_ros
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

