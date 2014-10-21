Name:           ros-indigo-mongodb-store
Version:        0.1.3
Release:        0%{?dist}
Summary:        ROS mongodb_store package

Group:          Development/Libraries
License:        MIT
URL:            http://www.ros.org/wiki/mongodb_store
Source0:        %{name}-%{version}.tar.gz

Requires:       libmongo-client-devel
Requires:       mongodb
Requires:       mongodb-devel
Requires:       python-pymongo
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-mongodb-store-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-std-srvs
BuildRequires:  libmongo-client-devel
BuildRequires:  mongodb
BuildRequires:  mongodb-devel
BuildRequires:  openssl-devel
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-mongodb-store-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-rospy
BuildRequires:  ros-indigo-rostest
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-std-srvs

%description
A package to support MongoDB-based storage and analysis for data from a ROS
system, eg. saved messages, configurations etc

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Tue Oct 21 2014 Chris Burbridge <cburbridge@gmail.com> - 0.1.3-0
- Autogenerated by Bloom

* Tue Oct 21 2014 Chris Burbridge <cburbridge@gmail.com> - 0.1.2-0
- Autogenerated by Bloom

* Fri Oct 17 2014 Chris Burbridge <cburbridge@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

* Thu Oct 16 2014 Chris Burbridge <cburbridge@gmail.com> - 0.1.0-0
- Autogenerated by Bloom

* Thu Oct 09 2014 Chris Burbridge <cburbridge@gmail.com> - 0.0.5-1
- Autogenerated by Bloom

* Thu Oct 09 2014 Chris Burbridge <cburbridge@gmail.com> - 0.0.5-0
- Autogenerated by Bloom

* Sat Sep 13 2014 Chris Curbridge <cburbridge@gmail.com> - 0.0.4-0
- Autogenerated by Bloom

* Wed Sep 10 2014 Chris Curbridge <cburbridge@gmail.com> - 0.0.3-0
- Autogenerated by Bloom

