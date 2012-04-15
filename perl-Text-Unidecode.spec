#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Text
%define		pnam	Unidecode
%include	/usr/lib/rpm/macros.perl
Summary:	Text::Unidecode -- US-ASCII transliterations of Unicode text
Name:		perl-Text-Unidecode
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	06f6bddb396ab386aa66a2bc8a04df76
URL:		http://search.cpan.org/dist/Text-Unidecode/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprov	perl(Text::Unidecode::x..)

%description
Text::Unidecode provides a function, unidecode(...) that takes Unicode
data and tries to represent it in US-ASCII characters (i.e., the
universally displayable characters between 0x00 and 0x7F). The
representation is almost always an attempt at transliteration -- i.e.,
conveying, in Roman letters, the pronunciation expressed by the text
in some other writing system.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO.txt
%{perl_vendorlib}/Text/Unidecode.pm
%{perl_vendorlib}/Text/Unidecode
%{_mandir}/man3/Text::Unidecode.3pm*
