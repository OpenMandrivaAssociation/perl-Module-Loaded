%define	module	Module-Loaded
%define name	perl-%{module}
%define	modprefix Module

%define version 0.01

%define	rel	1
%define release %mkrel %{rel}

Summary:	Mark modules as loaded or unloaded
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{modprefix}/%{module}-%{version}.tar.gz
%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildArch:	noarch


%description
When testing applications, often you find yourself needing to provide
functionality in your test environment that would usually be provided by
external modules. Rather than munging the %INC by hand to mark these external
modules as loaded, so they are not attempted to be loaded by perl, this module
offers you a very simple way to mark modules as loaded and/or unloaded.

%prep
%setup -q -n %{module}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/%{modprefix}/*
%{_mandir}/*/*
