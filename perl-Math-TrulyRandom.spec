#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# tests seem to hang
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	TrulyRandom
Summary:	TrulyRandom - Perl interface to a truly random number generator function
Summary(pl.UTF-8):	TrulyRandom - interfejs perlowy do generatora liczb naprawdę losowych
Name:		perl-Math-TrulyRandom
Version:	1.0
Release:	11
# if used in a product, Systemics should be given attribution
License:	free use, distributable
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	32e2273ee192203837cb1a21756a27a0
Patch0:		%{name}-paths.patch
URL:		http://search.cpan.org/dist/Math-TrulyRandom/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	code_which_works_on_modern_linux(not_detected_in_version) = 1.0
ExclusiveArch:	abacus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The TrulyRandom module provides an ability to generate truly random
numbers from within Perl programs. The source of the randomness is
from interrupt timing discrepancies.

%description -l pl.UTF-8
Moduł TrulyRandom pozwala na generowanie w programach perlowych liczb
naprawdę losowych. Źródłem losowości są rozbieżności w czasach
przerwań.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
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
