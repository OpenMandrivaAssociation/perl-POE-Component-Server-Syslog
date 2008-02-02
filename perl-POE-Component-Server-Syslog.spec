
%define realname   POE-Component-Server-Syslog
%define version    1.14
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Syslog server ability for POE
Source:     http://www.cpan.org/modules/by-module/POE/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Carp)
BuildRequires: perl(IO::Socket)
BuildRequires: perl(POE)
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::More)
BuildRequires: perl(Time::ParseDate)

BuildArch: noarch

%description
This module follows the POE::Filter specification. Actually, it
technically supports both the older specification (C<get>) and the newer
specification (C<get_one>). If, at some point, POE deprecates the older
specification, this module will drop support for it. As such, only use
of the newer specification is recommended.



%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes META.yml LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*



