# (tpg) 2021-07-05 lot of errors ld.lld: error: undefined symbol: _Py_NoneStruct
%define _disable_ld_no_undefined 1

Summary:	Crypto and SSL toolkit for Python
Name:		python-m2crypto
Version:	0.38.0
Release:	4
License:	MIT
Group:		Development/Python
Url:		https://gitlab.com/m2crypto/m2crypto
Source0:	https://files.pythonhosted.org/packages/aa/36/9fef97358e378c1d3bd567c4e8f8ca0428a8d7e869852cef445ee6da91fd/M2Crypto-%{version}.tar.gz
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

%package -n python2-m2crypto
Summary:	Crypto and SSL toolkit for Python 2
Group:		Development/Python
Obsoletes:	python-m2crypto < 0.23.0-2
Provides:	python-m2crypto = %{version}-%{release}

%description -n python2-m2crypto
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
%autosetup -n M2Crypto-%{version} -p1

rm -rf *.egg-info

%build
%set_build_flags

if pkg-config openssl ; then
    CFLAGS="$CFLAGS $(pkg-config --cflags openssl)" ; export CFLAGS
    LDFLAGS="$LDFLAGS$(pkg-config --libs-only-L openssl)" ; export LDFLAGS
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
