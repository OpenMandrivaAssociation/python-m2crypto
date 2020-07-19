%define _exclude_files_from_autoprov %{python2_sitearch}/.*\\.so\\|%{python3_sitearch}/.*\\.so

Summary: 	Crypto and SSL toolkit for Python
Name: 		python-m2crypto
Version:	0.36.0
Release:	1
License:	MIT
Group: 		Development/Python
Url: 		https://gitlab.com/m2crypto/m2crypto
Source0:	https://files.pythonhosted.org/packages/ff/df/84609ed874b5e6fcd3061a517bf4b6e4d0301f553baf9fa37bef2b509797/M2Crypto-0.36.0.tar.gz
#Patch0:		m2crypto-0.26.2-gcc_macros.patch
BuildRequires:	pkgconfig(python2)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python2-setuptools
BuildRequires:	python-setuptools
BuildRequires:	swig
BuildRequires:	pkgconfig(openssl)

%description
M2Crypto is a crypto and SSL toolkit for Python featuring the following:

    * RSA, DSA, DH, HMACs, message digests, symmetric ciphers (including AES).
    * SSL functionality to implement clients and servers.
    * HTTPS extensions to Python's httplib, urllib, and xmlrpclib.
    * Unforgeable HMAC'ing AuthCookies for web session management.
    * FTP/TLS client and server.
    * S/MIME.
    * ZServerSSL: A HTTPS server for Zope.
    * ZSmime: An S/MIME messenger for Zope.

%package -n	python2-m2crypto
Summary:	Crypto and SSL toolkit for Python 2
Group: 		Development/Python

Obsoletes:	python-m2crypto < 0.23.0-2
Provides:	python-m2crypto = %{version}-%{release}

%description -n	python2-m2crypto
M2Crypto is a crypto and SSL toolkit for Python 2 featuring the following:

    * RSA, DSA, DH, HMACs, message digests, symmetric ciphers (including AES).
    * SSL functionality to implement clients and servers.
    * HTTPS extensions to Python's httplib, urllib, and xmlrpclib.
    * Unforgeable HMAC'ing AuthCookies for web session management.
    * FTP/TLS client and server.
    * S/MIME.
    * ZServerSSL: A HTTPS server for Zope.
    * ZSmime: An S/MIME messenger for Zope.

%prep
%setup -q -n M2Crypto-%version
%autopatch -p1

rm -rf *.egg-info

%build
# Collect GCC predefinitions - patch0 makes SWIG use them. Implementation below is from fedora.
#
# __REGISTER_PREFIX__ is defined to unquoted $ on some platforms; gcc handles
# this fine, but swig chokes on it.
# __GNUC__ really should be included in gcc_macros.h, but this currently breaks
# builds on ppc64: https://bugzilla.redhat.com/show_bug.cgi?id=1317553 .
%{__cc} -E -dM - < /dev/null | grep -v __STDC__ | grep -v __REGISTER_PREFIX__ | grep -v __GNUC__ \
	| sed 's/^\(#define \([^ ]*\) .*\)$/#undef \2\n\1/' > SWIG/gcc_macros.h

CFLAGS="$RPM_OPT_FLAGS" ; export CFLAGS
if pkg-config openssl ; then
	CFLAGS="$CFLAGS `pkg-config --cflags openssl`" ; export CFLAGS
	LDFLAGS="$LDFLAGS`pkg-config --libs-only-L openssl`" ; export LDFLAGS
fi
%py2_build
%py3_build

%install
%py2_install
%py3_install


%files -n python2-m2crypto
%doc README.rst
%{python2_sitearch}/M2Crypto
%{python2_sitearch}/*.egg-info

%files
%{python_sitearch}/M2Crypto
%{python_sitearch}/*.egg-info
