%define major 5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kdoctools
Version: 5.12.0
Release: 1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Tools for handling KDE Frameworks 5 documentation
URL: http://kde.org/
License: LGPL v2.1
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5I18n)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: docbook-style-xsl docbook-dtd45-xml
BuildRequires: pkgconfig(libxslt)
BuildRequires: pkgconfig(libexslt)
BuildRequires: perl(URI::Escape)
Requires: docbook-style-xsl
Requires: docbook-dtd45-xml

%description
Tools for handling KDE Frameworks 5 documentation.

%package devel
Summary: Development files for %{name}
Group: Development/C
Requires: %{name} = %{EVRD}
Requires: cmake(ECM)
Requires: pkgconfig(Qt5Core)
Requires: cmake(KF5Archive)

%description devel
Development files (Headers etc.) for %{name}.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang kio_help5 || touch kio_help5.lang
%find_lang kdoctools5 || touch kdoctools5.lang

L="`pwd`/%{name}.lang"
cd %{buildroot}
for i in .%{_docdir}/HTML/*; do
	LNG=`echo $i |cut -d/ -f6`
	echo -n "%lang($LNG) " >>$L
	echo $i |cut -b2- >>$L
done

%files -f %{name}.lang,kio_help5.lang,kdoctools5.lang
%{_bindir}/*
%{_datadir}/kf5/kdoctools
%{_mandir}/man1/*
%{_mandir}/man7/*
%{_mandir}/man8/*
%{_mandir}/*/man1/*
%{_mandir}/*/man7/*
%{_mandir}/*/man8/*

%files devel
%{_includedir}/*
%{_libdir}/cmake/KF5DocTools
%{_libdir}/libKF5XsltKde.a
