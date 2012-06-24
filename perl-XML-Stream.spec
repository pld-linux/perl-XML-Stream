%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Stream
Summary:	XML::Stream -- XML streams interface for perl
Summary(pl):	XML::Stream -- obs�uga strumieni XML
Name:		perl-XML-Stream
Version:	1.16
Release:	2
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Unicode-String >= 2.06
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	"perl(HTTP::ProxyAutoConfig)"

%description
XML::Stream module - XML streams interface for perl.

%description -l pl
Modu� XML::Stream - Obs�uga strumieni XML dla perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo -e "y\ny\ny\n" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%{__make} install UNINST=0 DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES INFO
%{perl_vendorlib}/XML/*
%{_mandir}/man3/*
