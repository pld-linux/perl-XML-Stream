#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Stream
Summary:	XML::Stream - XML streams interface for Perl
Summary(pl):	XML::Stream - interfejs do strumieni XML dla Perla
Name:		perl-XML-Stream
Version:	1.19
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2d6a5b66d02c79c86e54bc3e79e2c3b0
%{?with_tests:BuildRequires:	perl-Authen-SASL}
BuildRequires:	perl-Unicode-String >= 2.06
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(HTTP::ProxyAutoConfig)'

%description
This module provides you with access to XML Streams. An XML Stream is
just that. A stream of XML over a connection between two computers.

%description -l pl
Ten modu³ daje dostêp do strumieni XML. Strumieñ XML jest po prostu
tym, co mówi nazwa - strumieniem XML po po³±czeniu miêdzy dwoma
komputerami.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
for i in Stream.pm Stream/*.pm Stream/*/*.pm; do
	%{__perl} -pi -e 's/^(use 5.006_)0(01;)(.*)$/$1$2$3/' lib/XML/$i
done

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
