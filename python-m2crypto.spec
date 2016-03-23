Summary:	Crypto and SSL toolkit for Python
Name:		python-m2crypto
Version:	0.24.0
Release:	1
License:	MIT
Group:		Development/Python
Url:		http://chandlerproject.org/Projects/MeTooCrypto
Source0:	http://pypi.python.org/packages/source/M/M2Crypto/M2Crypto-%{version}.tar.gz
BuildRequires:	swig
BuildRequires:	pkgconfig(openssl)
BuildRequires:  pkgconfig(python2)
BuildRequires:	python2-setuptools

%description
M2Crypto is a crypto and SSL toolkit for Python featuring the following:

    * RSA, DSA, DH, HMACs, message digests, symmetric ciphers (including AES).
    * SSL functionality to implement clients and servers.
    * HTTPS extensions to Python's httplib, urllib, and xmlrpclib.
    * Unforgeable HMAC'ing AuthCookies for web session management.
    * FTP/TLS client and server.
    * S/MIME.
    * ZServerSSL:	A HTTPS server for Zope.
    * ZSmime:	An S/MIME messenger for Zope.

%prep
%setup -q -n M2Crypto-%{version}
for i in SWIG/_ec.i SWIG/_evp.i; do
	sed -i -e "s/openssl\/opensslconf/%{multiarch_platform}\/openssl\/opensslconf/" "$i"
done

%build
env CFLAGS="$RPM_OPT_FLAGS" python2 setup.py build
# test requires some files ( such as a certificat, so disabled for now )
#PYTHONPATH="./build/lib.linux-i686-2.4/M2Crypto/:." python2 tests/alltests.py
%install
python2 setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%files
%{py2_platsitedir}/M2Crypto
%{py2_platsitedir}/*.egg-info

