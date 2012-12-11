%define upstream_name    POE-Component-Server-Syslog
%define upstream_version 1.20

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Syslog server ability for POE
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(POE)
BuildRequires:	perl(Params::Validate)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Time::ParseDate)
BuildArch:	noarch

%description
This module follows the POE::Filter specification. Actually, it
technically supports both the older specification (C<get>) and the newer
specification (C<get_one>). If, at some point, POE deprecates the older
specification, this module will drop support for it. As such, only use
of the newer specification is recommended.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
rm -f t/000-signature.t
make test

%install
%makeinstall_std

%files
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.200.0-2mdv2011.0
+ Revision: 657458
- rebuild for updated spec-helper

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.200.0-1
+ Revision: 638936
- update to new version 1.20

* Fri May 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.180.0-1mdv2010.0
+ Revision: 380861
- update to 1.18
- using %%perl_convert_version
- fixed license tag

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.16-2mdv2009.0
+ Revision: 268702
- rebuild early 2009.0 package (before pixel changes)

* Thu Apr 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.16-1mdv2009.0
+ Revision: 195405
- new version

* Sat Feb 02 2008 Jérôme Quelin <jquelin@mandriva.org> 1.14-1mdv2008.1
+ Revision: 161447
- import perl-POE-Component-Server-Syslog


