Name:           ros-jade-srdfdom
Version:        0.3.4
Release:        0%{?dist}
Summary:        ROS srdfdom package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/srdfdom
Source0:        %{name}-%{version}.tar.gz

Requires:       boost-devel
Requires:       console-bridge-devel
Requires:       ros-jade-urdfdom-py
Requires:       tinyxml-devel
Requires:       urdfdom-headers-devel
BuildRequires:  boost-devel
BuildRequires:  console-bridge-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-rostest
BuildRequires:  ros-jade-urdfdom-py
BuildRequires:  tinyxml-devel
BuildRequires:  urdfdom-headers-devel

%description
Parser for Semantic Robot Description Format (SRDF).

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Mon Jan 30 2017 Dave Coleman <dave@dav.ee> - 0.3.4-0
- Autogenerated by Bloom

* Fri Sep 09 2016 Dave Coleman <dave@dav.ee> - 0.3.3-0
- Autogenerated by Bloom

* Thu Aug 25 2016 Dave Coleman <dave@dav.ee> - 0.3.2-0
- Autogenerated by Bloom

* Tue Aug 02 2016 Ioan Sucan <isucan@willowgarage.com> - 0.3.1-0
- Autogenerated by Bloom

* Sun Mar 15 2015 Ioan Sucan <isucan@willowgarage.com> - 0.2.7-0
- Autogenerated by Bloom

