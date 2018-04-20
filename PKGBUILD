# Script generated with Bloom
pkgdesc="ROS - A package to support MongoDB-based storage and analysis for data from a ROS system, eg. saved messages, configurations etc"
url='http://www.ros.org/wiki/mongodb_store'

pkgname='ros-kinetic-mongodb-store'
pkgver='0.3.7_1'
pkgrel=1
arch=('any')
license=('MIT'
)

makedepends=('mongodb'
'openssl'
'python2-catkin_pkg'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-libmongocxx-ros'
'ros-kinetic-message-generation'
'ros-kinetic-mongodb-store-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-rostest'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-topic-tools'
)

depends=('mongodb'
'python2-pymongo'
'ros-kinetic-geometry-msgs'
'ros-kinetic-libmongocxx-ros'
'ros-kinetic-mongodb-store-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-std-msgs'
'ros-kinetic-std-srvs'
'ros-kinetic-topic-tools'
)

conflicts=()
replaces=()

_dir=mongodb_store
source=()
md5sums=()

prepare() {
    cp -R $startdir/mongodb_store $srcdir/mongodb_store
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

