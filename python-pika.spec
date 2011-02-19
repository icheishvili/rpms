%define short_name pika

Name:           python-%{short_name}
Version:        0.9.3
Release:        1%{?dist}
Summary:        AMQP 0-9-1 client library for Python

Group:          Development/Libraries
License:        MPLv1.1 or GPLv2
URL:            http://github.com/tonyg/pika
# The tarball comes from here:
# http://github.com/tonyg/pika/tarball/v%{version}
# GitHub has layers of redirection and renames that make this a troublesome
# URL to include directly.
Source0:        tonyg-%{short_name}-v%{version}-0-gfaf4cc0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-setuptools
BuildRequires:  python-devel
Requires:       python

%description
Pika is a pure-Python implementation of the AMQP 0-9-1 protocol that
tries to stay fairly independent of the underlying network support
library.


%prep
%setup -q -n tonyg-%{short_name}-faf4cc0


%build
%{__python} setup.py build

%install
%{__rm} -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
%{__rm} -rf %{buildroot}


%files
%defattr(-,root,root,-)
%dir %{python_sitelib}/%{short_name}*
%{python_sitelib}/%{short_name}*/*
%doc COPYING
%doc LICENSE-GPL-2.0
%doc LICENSE-MPL-Pika
%doc README.md
%doc THANKS
%doc TODO
%doc examples

%changelog
* Sat Oct 2 2010 Ilia Cheishvili <ilia.cheishvili@gmail.com> - 0.5.2-1
- Initial Package

