#
# Conditional build:
%bcond_without	tests		# unit tests
#
%define		pdir	PPIx
%define		pnam	QuoteLike
Summary:	PPIx::QuoteLike - Parse Perl string literals and string-literal-like things
Summary(pl.UTF-8):	PPIx::QuoteLike - analiza literałów tekstowych Perla i rzeczy do nich podobnych
Name:		perl-PPIx-QuoteLike
Version:	0.023
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/W/WY/WYANT/PPIx-QuoteLike-%{version}.tar.gz
# Source0-md5:	551890e6c65a3eb0f4b753ad4288acb2
URL:		https://metacpan.org/dist/PPIx-QuoteLike
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-PPI >= 1.117
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This Perl class parses Perl string literals and things that are
reasonably like string literals. Its real reason for being is to find
interpolated variables for Perl::Critic policies and similar code.

%description -l pl.UTF-8
Ta klasa Perla analizuje literały łańcuchów znakowych Perla oraz
rzeczy, które są do nich rozsądnie podobne. Głównym powodem istnienia
tego modułu jest wyszukiwanie interpolowanych zmiennych dla polityk
Perl::Critic i podobnego kodu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	installdirs=vendor

%{__make}

%if %{with tests}
%{__make} test
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__sed} -i -e '1s,/usr/bin/env perl,%{__perl},' \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/eg/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/PPIx/QuoteLike.pm
%{perl_vendorlib}/PPIx/QuoteLike
%{_mandir}/man3/PPIx::QuoteLike*.3pm*
%{_examplesdir}/%{name}-%{version}
