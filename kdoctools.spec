%define major 5
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

%define libname %{mklibname KF5DocTools %{major}}
%define develname %{mklibname -d KF5DocTools}

Name: kdoctools
Version:	5.32.0
Release:	1
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

%package -n %{libname}
Summary: The KDocTools library
Group: System/Libraries

%description -n %{libname}
The KDocTools library.

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
Requires: %{name} = %{EVRD}
Requires: cmake(ECM)
Requires: pkgconfig(Qt5Core)
Requires: cmake(KF5Archive)
%rename %{name}-devel

%description -n %{develname}
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
%lang(ca) %{_mandir}/ca/man?/*
%lang(de) %{_mandir}/de/man?/*
%lang(es) %{_mandir}/es/man?/*
%lang(it) %{_mandir}/it/man?/*
%lang(nl) %{_mandir}/nl/man?/*
%lang(pt_BR) %{_mandir}/pt_BR/man?/*
%lang(ru) %{_mandir}/ru/man?/*
%lang(sv) %{_mandir}/sv/man?/*
%lang(uk) %{_mandir}/uk/man?/*

%files -n %{libname}
%{_libdir}/libKF5DocTools.so.%{major}*

%files -n %{develname}
%{_includedir}/*
%{_libdir}/cmake/KF5DocTools
%{_libdir}/libKF5DocTools.so
