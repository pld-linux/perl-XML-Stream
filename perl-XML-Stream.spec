%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	Stream
Summary:	XML::Stream - XML streams interface for perl
Summary(pl):	XML::Stream - obs³uga strumieni XML
Name:		perl-XML-Stream
Version:	1.17
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3545686d95034a707e9f8cb17797214f
BuildRequires:	perl-Unicode-String >= 2.06
BuildRequires:	perl-devel >= 5.005_03-14
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(HTTP::ProxyAutoConfig)'

%description
XML::Stream module - XML streams interface for perl.

%description -l pl
Modu³ XML::Stream - Obs³uga strumieni XML dla perla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
for i in Stream.pm Stream/*.pm Stream/*/*.pm; do
	%{__perl} -pi -e 's/^(use 5.006_)0(01;)(.*)$/$1$2$3/' $i
done

%build
echo -e "y\ny\ny\n" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

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
