%include	/usr/lib/rpm/macros.perl
Summary:	Math-TrulyRandom perl module
Summary(pl):	Modu³ perla Math-TrulyRandom
Name:		perl-Math-TrulyRandom
Version:	1.0
Release:	3
Copyright:	distributable
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Math/Math-TrulyRandom-%{version}.tar.gz
Patch0:		perl-Math-TrulyRandom-paths.patch
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math-TrulyRandom perl module.

%description -l pl
Modu³ perla Math-TrulyRandom.

%prep
%setup -q -n Math-TrulyRandom-%{version}
%patch -p1

%build
perl Makefile.PL
make OPTIMIZE="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded \
	$RPM_BUILD_ROOT/%{perl_sitearch}/auto/Math/TrulyRandom/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Math/TrulyRandom
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz examples/example_1.pl

%{perl_sitearch}/Math/TrulyRandom.pm

%dir %{perl_sitearch}/auto/Math/TrulyRandom
%{perl_sitearch}/auto/Math/TrulyRandom/.packlist
%{perl_sitearch}/auto/Math/TrulyRandom/TrulyRandom.bs
%attr(755,root,root) %{perl_sitearch}/auto/Math/TrulyRandom/TrulyRandom.so

%{_mandir}/man3/*
