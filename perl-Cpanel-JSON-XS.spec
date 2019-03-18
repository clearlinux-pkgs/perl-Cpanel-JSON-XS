#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Cpanel-JSON-XS
Version  : 4.10
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Cpanel-JSON-XS-4.10.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RU/RURBAN/Cpanel-JSON-XS-4.10.tar.gz
Summary  : cPanel fork of JSON::XS, fast and correct serializing
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Cpanel-JSON-XS-bin = %{version}-%{release}
Requires: perl-Cpanel-JSON-XS-lib = %{version}-%{release}
Requires: perl-Cpanel-JSON-XS-license = %{version}-%{release}
Requires: perl-Cpanel-JSON-XS-man = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Cpanel::JSON::XS - cPanel fork of JSON::XS, fast and correct serializing
SYNOPSIS
use Cpanel::JSON::XS;

%package bin
Summary: bin components for the perl-Cpanel-JSON-XS package.
Group: Binaries
Requires: perl-Cpanel-JSON-XS-license = %{version}-%{release}

%description bin
bin components for the perl-Cpanel-JSON-XS package.


%package dev
Summary: dev components for the perl-Cpanel-JSON-XS package.
Group: Development
Requires: perl-Cpanel-JSON-XS-lib = %{version}-%{release}
Requires: perl-Cpanel-JSON-XS-bin = %{version}-%{release}
Provides: perl-Cpanel-JSON-XS-devel = %{version}-%{release}
Requires: perl-Cpanel-JSON-XS = %{version}-%{release}

%description dev
dev components for the perl-Cpanel-JSON-XS package.


%package lib
Summary: lib components for the perl-Cpanel-JSON-XS package.
Group: Libraries
Requires: perl-Cpanel-JSON-XS-license = %{version}-%{release}

%description lib
lib components for the perl-Cpanel-JSON-XS package.


%package license
Summary: license components for the perl-Cpanel-JSON-XS package.
Group: Default

%description license
license components for the perl-Cpanel-JSON-XS package.


%package man
Summary: man components for the perl-Cpanel-JSON-XS package.
Group: Default

%description man
man components for the perl-Cpanel-JSON-XS package.


%prep
%setup -q -n Cpanel-JSON-XS-4.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Cpanel-JSON-XS
cp COPYING %{buildroot}/usr/share/package-licenses/perl-Cpanel-JSON-XS/COPYING
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Cpanel/JSON/XS.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Cpanel/JSON/XS/Boolean.pm
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/Cpanel/JSON/XS/Type.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/cpanel_json_xs

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Cpanel::JSON::XS.3
/usr/share/man/man3/Cpanel::JSON::XS::Boolean.3
/usr/share/man/man3/Cpanel::JSON::XS::Type.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/x86_64-linux-thread-multi/auto/Cpanel/JSON/XS/XS.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Cpanel-JSON-XS/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/cpanel_json_xs.1
