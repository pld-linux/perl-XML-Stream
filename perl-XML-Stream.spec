#
# Conditional build:
%bcond_with	tests	# do not perform "make test"
#
%define		pdir	XML
%define		pnam	Stream
Summary:	XML::Stream - XML streams interface for Perl
Summary(pl.UTF-8):	XML::Stream - interfejs do strumieni XML dla Perla
Name:		perl-XML-Stream
Version:	1.24
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	62717494479cba3746bfeab73d2f955c
Patch0:		%{name}-warnings.patch
Patch1:		ssl-ca.patch
URL:		http://search.cpan.org/dist/XML-Stream/
BuildRequires:	perl-Unicode-String >= 2.06
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Authen-SASL
BuildRequires:	perl-Encode
BuildRequires:	perl-MIME-Base64
BuildRequires:	perl-Test-Simple >= 0.92
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(HTTP::ProxyAutoConfig)'

%description
This module provides you with access to XML Streams. An XML Stream is
just that. A stream of XML over a connection between two computers.

%description -l pl.UTF-8
Ten moduł daje dostęp do strumieni XML. Strumień XML jest po prostu
tym, co mówi nazwa - strumieniem XML po połączeniu między dwoma
komputerami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
for i in Stream.pm Stream/*.pm Stream/*/*.pm; do
	%{__perl} -pi -e 's/^(use 5.006_)0(01;)(.*)$/$1$2$3/' lib/XML/$i
done
%patch -P0 -p1
%patch -P1 -p1

%build
echo -e "y\ny\ny\n" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	UNINST=0 \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES INFO
%{perl_vendorlib}/XML/*
%{_mandir}/man3/*
