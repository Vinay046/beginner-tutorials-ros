Name:           ros-indigo-ros-tutorials
Version:        0.5.4
Release:        0%{?dist}
Summary:        ROS ros_tutorials package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ros_tutorials
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-roscpp-tutorials
Requires:       ros-indigo-rospy-tutorials
Requires:       ros-indigo-turtlesim
BuildRequires:  ros-indigo-catkin

%description
ros_tutorials contains packages that demonstrate various features of ROS, as
well as support packages which help demonstrate those features.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
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
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sun Sep 20 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.5.4-0
- Autogenerated by Bloom

* Mon May 04 2015 Dirk Thomas <dthomas@osrfoundation.org> - 0.5.3-0
- Autogenerated by Bloom

* Tue Dec 23 2014 Dirk Thomas <dthomas@osrfoundation.org> - 0.5.2-0
- Autogenerated by Bloom

