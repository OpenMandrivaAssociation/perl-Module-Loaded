%define	upstream_name	 Module-Loaded
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.08
Release:	1

Summary:	Mark modules as loaded or unloaded
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Module/Module-Loaded-0.08.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
When testing applications, often you find yourself needing to provide
functionality in your test environment that would usually be provided by
external modules. Rather than munging the %INC by hand to mark these external
modules as loaded, so they are not attempted to be loaded by perl, this module
offers you a very simple way to mark modules as loaded and/or unloaded.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Module/*
%{_mandir}/*/*


%changelog
* Mon Sep 07 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 432798
- update to 0.06

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.20.0-1mdv2010.0
+ Revision: 408965
- rebuild using %%perl_convert_version

* Tue Dec 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.02-1mdv2009.1
+ Revision: 314758
- update to new version 0.02

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.01-1mdv2009.0
+ Revision: 136289
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Jun 22 2007 Buchan Milne <bgmilne@mandriva.org> 0.01-1mdv2008.0
+ Revision: 42863
- Import perl-Module-Loaded



* Thu Jun 21 2007 Buchan Milne <bgmilne@mandriva.org> 0.01-1mdv2007.1
- initial package

