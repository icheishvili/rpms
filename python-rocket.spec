%define upstream_name Rocket

Name:           python-rocket
Version:        1.1.1
Release:        1%{?dist}
Summary:        Modern, multi-threaded, comet-friendly WSGI web server

Group:          Development/Libraries
License:        MIT
URL:            http://pypi.python.org/pypi/rocket/
Source0:        http://pypi.python.org/packages/source/r/rocket/Rocket-1.1.1.zip
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-setuptools
BuildRequires:  python-devel
Requires:       python

%description
The Rocket web server is a server designed to handle the increased needs
of modern web applications implemented in pure Python. It can serve WSGI
applications and static files. Rocket has the ability to be extended to
handle different types of networked request-response jobs. Rocket runs on
cPython 2.5- 3.x and Jython 2.5 (without the need to run through the 2to3
translation tool). Rocket is similar in purpose to Cherrypy's Wsgiserver
but with added flexibility, speed and concurrency.


%prep
%setup -q -n %{upstream_name}-%{version}


%build
%{__python} setup.py build


%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %{python_sitelib}/%{upstream_name}-%{version}-*
%dir %{python_sitelib}/rocket
%{python_sitelib}/%{upstream_name}-%{version}-*/*
%{python_sitelib}/rocket/*


%changelog
* Sun Oct 3 2010 Ilia Cheishvili <ilia.cheishvili@gmail.com> - 1.1.1-1
- Initial Package
