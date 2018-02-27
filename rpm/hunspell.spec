Name:      hunspell
Summary:   A spell checker and morphological analyzer library
Version:   1.6.2
Release:   1
Source0:   %{name}-%{version}.tar.bz2
Group:     System/Libraries
URL:       http://hunspell.github.io/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
License:   LGPLv2+ or GPLv2+ or MPLv1.1
BuildRequires: libtool, autoconf, automake, ncurses-devel

%description
Hunspell is a spell checker and morphological analyzer
library and program designed for languages with rich morphology and
complex word compounding or character encoding. Hunspell interfaces:
Ispell-like terminal interface using Curses library, Ispell pipe
interface, C++ class and C functions.


%package tools
Requires: %{name} = %{version}
Summary: Hunspell tools
Group: System/Libraries

%description tools
Hunspell tools


%package devel
Requires: pkgconfig
Summary: Files for developing with hunspell
Group: Development/Libraries

%description devel
Includes and definitions for developing with hunspell

%prep
%setup -q -n %{name}-%{version}/hunspell

%build
%{__make} clean || true

autoreconf -vfi

CFLAGS="$CFLAGS -fPIC"
CXXFLAGS="$CXXFLAGS -fPIC"
%configure 
make %{?_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files 
%defattr(-,root,root,-)
%doc README README.myspell COPYING COPYING.LESSER COPYING.MPL AUTHORS AUTHORS.myspell license.hunspell license.myspell THANKS
%{_libdir}/*.so.*
%{_libdir}/*.so
%{_bindir}/hunspell

%files devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/hunspell.pc

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
%{_mandir}/man1/hunspell.1.gz
%{_mandir}/man1/hunzip.1.gz
%{_mandir}/man1/hzip.1.gz
%{_mandir}/man3/hunspell.3.gz
%{_mandir}/man5/hunspell.5.gz
%lang(hu) %{_mandir}/hu/man1/hunspell.1.gz

