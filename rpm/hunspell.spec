Name:      hunspell
Summary:   A spell checker and morphological analyzer library
Version:   1.7.1
Release:   1
Source0:   %{name}-%{version}.tar.bz2
URL:       https://github.com/sailfishos/hunspell
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
License:   LGPLv2+ or GPLv2+ or MPLv1.1
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: gettext-devel
BuildRequires: libtool
BuildRequires: ncurses-devel

%description
Hunspell is a spell checker and morphological analyzer
library and program designed for languages with rich morphology and
complex word compounding or character encoding. Hunspell interfaces:
Ispell-like terminal interface using Curses library, Ispell pipe
interface, C++ class and C functions.


%package tools
Requires: %{name} = %{version}
Summary: Hunspell tools

%description tools
Hunspell tools


%package devel
Requires: %{name} = %{version}
Requires: pkgconfig
Summary: Files for developing with hunspell

%description devel
Includes and definitions for developing with hunspell


%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
Man pages for %{name}.


%prep
%setup -q -n %{name}-%{version}/hunspell

%build

autoreconf -vfi

%configure
%make_build


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_docdir}/%{name}-%{version}
install -m0644 -t %{buildroot}%{_docdir}/%{name}-%{version} \
        README README.md AUTHORS THANKS

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root,-)
%license COPYING COPYING.LESSER COPYING.MPL
%{_libdir}/*.so.*
%{_bindir}/hunspell

%files devel
%defattr(-,root,root,-)
%license license.hunspell license.myspell
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/hunspell.pc
%exclude %{_libdir}/*.la
%exclude %{_libdir}/*.a

%files tools
%{_bindir}/affixcompress
%{_bindir}/makealias
%{_bindir}/munch
%{_bindir}/unmunch
%{_bindir}/analyze
%{_bindir}/chmorph
%{_bindir}/hzip
%{_bindir}/hunzip
%{_bindir}/ispellaff2myspell
%{_bindir}/wordlist2hunspell
%{_bindir}/wordforms

%files doc
%defattr(-,root,root,-)
%{_mandir}/man*/h*.*
%exclude %{_mandir}/hu/man1/hunspell.1.gz
%{_docdir}/%{name}-%{version}
