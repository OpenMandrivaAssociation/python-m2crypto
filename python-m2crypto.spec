%define rname m2crypto
%define name python-%rname
%define version 0.17
%define release %mkrel 1


Summary: 	Crypto and SSL toolkit for Python
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source0: 	%{rname}-%{version}.tar.bz2
License:	Historical Permission Notice and Disclaimer
Group: 		Development/Python
Url: 		http://sandbox.rulemaker.net/ngps/m2/
BuildRequires:	python-devel swig openssl-devel


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

%prep
%setup -q -n %{rname}-%version

%build
env CFLAGS="$RPM_OPT_FLAGS" python setup.py build
# test requires some files ( such as a certificat, so disabled for now )
#PYTHONPATH="./build/lib.linux-i686-2.4/M2Crypto/:." python tests/alltests.py
%install
python setup.py install --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{py_platsitedir}/M2Crypto
%{py_platsitedir}/*.egg-info
%doc CHANGES README INSTALL LICENCE

