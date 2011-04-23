%define upstream_name    POE-Component-Server-Syslog
%define upstream_version 1.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

License:    GPL+ or Artistic
Group:      Development/Perl
Summary:    Syslog server ability for POE
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/POE/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(IO::Socket)
BuildRequires: perl(POE)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::ParseDate)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This module follows the POE::Filter specification. Actually, it
technically supports both the older specification (C<get>) and the newer
specification (C<get_one>). If, at some point, POE deprecates the older
specification, this module will drop support for it. As such, only use
of the newer specification is recommended.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
rm -f t/000-signature.t
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*

