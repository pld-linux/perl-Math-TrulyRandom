%define	pdir	Math
%define	pnam	TrulyRandom
%include	/usr/lib/rpm/macros.perl
Summary:	Math-TrulyRandom perl module
Summary(pl):	Modu� perla Math-TrulyRandom
Name:		perl-Math-TrulyRandom
Version:	1.0
Release:	6

License:	distributable
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
Patch0:		%{name}-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-TrulyRandom perl module.

%description -l pl
Modu� perla Math-TrulyRandom.

%prep
%setup -q -n Math-TrulyRandom-%{version}
%patch -p1

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz examples/example_1.pl
%{perl_sitearch}/Math/TrulyRandom.pm
%dir %{perl_sitearch}/auto/Math/TrulyRandom
%{perl_sitearch}/auto/Math/TrulyRandom/TrulyRandom.bs
%attr(755,root,root) %{perl_sitearch}/auto/Math/TrulyRandom/TrulyRandom.so
%{_mandir}/man3/*
