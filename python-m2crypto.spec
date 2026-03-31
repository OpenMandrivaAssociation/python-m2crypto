%define module m2crypto
%define oname M2Crypto

Name:		python-m2crypto
Summary:	Crypto and SSL toolkit for Python
Version:	0.48.0
Release:	1
License:	BSD-2-Clause
Group:		Development/Python
URL:		https://git.sr.ht/~mcepl/m2crypto
Source0:	https://git.sr.ht/~mcepl/m2crypto/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Upstream does not always make releases on pypi coinciding with the gitlab and now sourcehut hosted repo.
# Source0:	https://files.pythonhosted.org/packages/source/m/%%{module}/%%{module}-%%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	swig

# Package used to have a py2 version
%rename python2-m2crypto

%description
M2Crypto is a crypto and SSL toolkit for Python featuring the following:

RSA, DSA, DH, HMACs, message digests, symmetric ciphers (including
AES). SSL functionality to implement clients and servers. HTTPS
extensions to Python's httplib, urllib, and xmlrpclib. Unforgeable
HMAC'ing AuthCookies for web session management. FTP/TLS client and
server. S/MIME. ZServerSSL: A HTTPS server for Zope. ZSmime: An S/MIME
messenger for Zope.

%prep -a
# Remove bundled egg-info
rm -rf src/%{oname}.egg-info

%build -p
export LDFLAGS="%{ldflags} -lpython%{py_ver}"

%files
%doc README.md
%{python_sitearch}/%{oname}
%{python_sitearch}/%{module}-%{version}.dist-info
