#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# tests seem to hang
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	TrulyRandom
Summary:	TrulyRandom - Perl interface to a truly random number generator function
Summary(pl):	TrulyRandom - interfejs perlowy do generatora liczb naprawdê losowych
Name:		perl-Math-TrulyRandom
Version:	1.0
Release:	10
# if used in a product, Systemics should be given attribution
License:	free use, distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	32e2273ee192203837cb1a21756a27a0
Patch0:		%{name}-paths.patch
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	code_which_works_on_modern_linux(not_detected_in_version) = 1.0
ExclusiveArch:	abacus
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README examples/example_1.pl
%{perl_vendorarch}/Math/TrulyRandom.pm
%dir %{perl_vendorarch}/auto/Math/TrulyRandom
%{perl_vendorarch}/auto/Math/TrulyRandom/TrulyRandom.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Math/TrulyRandom/TrulyRandom.so
%{_mandir}/man3/*
