%include	/usr/lib/rpm/macros.perl
Summary:	XML streams perl module
Summary(pl):	Modu³ perla do obs³ugi strumieni XML
Name:		perl-XML-Stream
Version:	1.12
Release:	1
License:	LGPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	http://www.obelisk.net/jarl/modules/XML-Stream-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq "perl(HTTP::ProxyAutoConfig)"

%description
Net-Jabber - XML streams interface for perl.

%description -l pl
Net-Jabber - Obs³uga strumieni XML dla perla.
%prep
%setup -q -n XML-Stream-%{version}

%build
echo -e "y\ny\ny\n" |perl Makefile.PL
%{__make} OPTIMIZE="%{?debug:-O -g}%{!?debug:$RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

%{__make} install UNINST=0 DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGES INFO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%{perl_sitelib}/XML/*

%{_mandir}/man3/*
