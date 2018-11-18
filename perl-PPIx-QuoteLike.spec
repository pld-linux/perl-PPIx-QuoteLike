#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	PPIx
%define		pnam	QuoteLike
%include	/usr/lib/rpm/macros.perl
Summary:	PPIx::QuoteLike - Parse Perl string literals and string-literal-like things
Name:		perl-PPIx-QuoteLike
Version:	0.006
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://cpan.metacpan.org/authors/id/W/WY/WYANT/PPIx-QuoteLike-%{version}.tar.gz
# Source0-md5:	9ecce45ae1a38cf6fb2df4d3ae7be450
URL:		https://metacpan.org/release/PPIx-QuoteLike/
BuildRequires:	perl-Module-Build
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

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	installdirs=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a eg $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/PPIx/*.pm
%{perl_vendorlib}/PPIx/QuoteLike
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
