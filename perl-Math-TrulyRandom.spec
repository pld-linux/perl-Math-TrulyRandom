%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	TrulyRandom
Summary:	TrulyRandom - Perl interface to a truly random number generator function
Summary(pl):	TrulyRandom - interfejs do generatora liczb naprawdê losowych
Name:		perl-Math-TrulyRandom
Version:	1.0
Release:	9
License:	distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The TrulyRandom module provides an ability to generate truly random
numbers from within Perl programs. The source of the randomness is
from interrupt timing discrepancies.

%description -l pl
Modu³ TrulyRandom pozwala na generowanie w programach perlowych liczb
naprawdê losowych. ¬ród³em losowo¶ci s± rozbie¿no¶ci w czasach
przerwañ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch -p1

%build
%{__perl} Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README examples/example_1.pl
%{perl_sitearch}/Math/TrulyRandom.pm
%dir %{perl_sitearch}/auto/Math/TrulyRandom
%{perl_sitearch}/auto/Math/TrulyRandom/TrulyRandom.bs
%attr(755,root,root) %{perl_sitearch}/auto/Math/TrulyRandom/TrulyRandom.so
%{_mandir}/man3/*
