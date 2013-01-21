%if 0%{?fedora} > 12 || 0%{?rhel} > 6
%global with_python3 1
%else
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

%global upstream_name Rocket
%global normal_name rocket

Name:           python-%{normal_name}
Version:        1.2.4
Release:        1%{?dist}
Summary:        Modern, multi-threaded, comet-friendly WSGI web server

Group:          Development/Libraries
License:        MIT
URL:            http://pypi.python.org/pypi/rocket/
Source0:        http://pypi.python.org/packages/source/r/rocket/Rocket-%{version}.zip
BuildArch:      noarch

Requires:       python
BuildRequires:  python-setuptools
BuildRequires:  python-devel
%if 0%{?with_python3}
BuildRequires:  python3-setuptools
BuildRequires:  python3-devel
Requires:       python3
%endif # if with_python3


%description
The Rocket web server is a server designed to handle the increased needs
of modern web applications implemented in pure Python. It can serve WSGI
applications and static files. Rocket has the ability to be extended to
handle different types of networked request-response jobs. Rocket runs on
cPython 2.5- 3.x and Jython 2.5 (without the need to run through the 2to3
translation tool). Rocket is similar in purpose to Cherrypy's Wsgiserver
but with added flexibility, speed and concurrency.

%if 0%{?with_python3}
%package -n     python3-rocket
Summary:        Modern, multi-threaded, comet-friendly WSGI web server
Group:          Development/Libraries

%description -n python3-rocket
The Rocket web server is a server designed to handle the increased needs
of modern web applications implemented in pure Python. It can serve WSGI
applications and static files. Rocket has the ability to be extended to
handle different types of networked request-response jobs. Rocket runs on
cPython 2.5- 3.x and Jython 2.5 (without the need to run through the 2to3
translation tool). Rocket is similar in purpose to Cherrypy's Wsgiserver
but with added flexibility, speed and concurrency.
%endif # with_python3


%prep
%setup -q -n %{upstream_name}-%{version}
%{__rm} -rf %{upstream_name}.egg_info

%if 0%{?with_python3}
%{__rm} -rf %{py3dir}
%{__cp} -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
CFLAGS="$RPM_OPT_FLAGS" %{__python3} setup.py build
popd
%endif # with_python3

%install
rm -rf %{buildroot}

# Must do the python3 install first because the scripts in /usr/bin are
# overwritten with every setup.py install (and we want the python2 version
# to be the default for now).
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3

%{__python} setup.py install --skip-build --root %{buildroot}

%check
%{__python} setup.py test

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py test
popd
%endif # with_python3


%clean
rm -rf %{buildroot}

%files
%{python_sitelib}/%{upstream_name}-%{version}*
%{python_sitelib}/%{normal_name}

%if 0%{?with_python3}
%files -n python3-rocket
%{python3_sitelib}/%{upstream_name}-%{version}*
%{python3_sitelib}/%{normal_name}
%endif # with_python3


%changelog
* Sun Jan 06 2013 Ilia Cheishvili <ilia.cheishvili@gmail.com> - 1.2.4-1
- Initial Package
