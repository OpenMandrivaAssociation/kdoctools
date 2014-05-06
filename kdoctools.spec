%define major 5

Name: kdoctools
Version: 4.98.0
Release: 3
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/%{version}/%{name}-%{version}.tar.xz
Patch0: kdoctools-4.98.0-DATA_INSTALL_DIR-is-absolute.patch
Summary: Tools for handling KDE Frameworks 5 documentation
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: qmake5
BuildRequires: cmake
BuildRequires: cmake(KF5Archive)
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: docbook-style-xsl docbook-dtd45-xml
Requires: docbook-style-xsl docbook-dtd45-xml

%description
Tools for handling KDE Frameworks 5 documentation

%package devel
Summary: Development files for %{name}
Group: Development/C
Requires: %{name} = %{EVRD}
Requires: extra-cmake-modules5
Requires: pkgconfig(Qt5Core)
Requires: cmake(KF5Archive)

%description devel
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%apply_patches
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_bindir}/*
%{_datadir}/kdoctools5
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_mandir}/man8/*

%files devel
%{_includedir}/*
%{_libdir}/cmake/KF5DocTools
%{_libdir}/libKF5XsltKde.a
