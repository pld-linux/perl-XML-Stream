%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Stream
Summary:	XML streams perl module
Summary(pl):	Modu³ perla do obs³ugi strumieni XML
Name:		perl-XML-Stream
Version:	1.15
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Unicode-String >= 2.06
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq "perl(HTTP::ProxyAutoConfig)"

%description
XML::Stream module - XML streams interface for perl.

%description -l pl
Modu³ XML::Stream - Obs³uga strumieni XML dla perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo -e "y\ny\ny\n" |perl Makefile.PL
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
%{perl_sitelib}/XML/*
%{_mandir}/man3/*
