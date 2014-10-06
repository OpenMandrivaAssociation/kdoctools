%define major 5

Name: kdoctools
Version: 5.3.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: Tools for handling KDE Frameworks 5 documentation
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: qmake5
BuildRequires: cmake >= 2.8.12.2-5
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
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%find_lang kio_help5

L="`pwd`/%{name}.lang"
cd %{buildroot}
for i in .%{_docdir}/HTML/*; do
	LNG=`echo $i |cut -d/ -f6`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f %{name}.lang,kio_help5.lang
%{_bindir}/*
%{_datadir}/kf5/kdoctools
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_mandir}/man8/*

%files devel
%{_includedir}/*
%{_libdir}/cmake/KF5DocTools
%{_libdir}/libKF5XsltKde.a
