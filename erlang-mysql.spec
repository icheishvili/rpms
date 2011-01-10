%global debug_package %{nil}
%define git_version_sha 93750e1
%define git_author_name dizzyd

Name:           erlang-mysql
Version:        2010.11.02
Release:        1%{?dist}
Summary:        This MySQL driver for Erlang is based on the Yxa driver obtained from Process One

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/dizzyd/%{name}-driver
Source0:        https://download.github.com/%{git_author_name}-%{name}-driver-%{git_version_sha}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  erlang
Requires:       erlang

%description
This MySQL driver for Erlang is based on the Yxa driver obtained from
Process One
(at https://support.process-one.net/doc/display/CONTRIBS/Yxa). It
includes several new features such as prepared statements,
transactions, binary queries, type-converted query results, more
efficient logging and a new connection pooling mechanism.


%prep
%setup -q -n %{git_author_name}-%{name}-driver-%{git_version_sha}

%build
erlc ./src/*.erl
%{__mv} *.beam ./ebin/
%{__rm} ./ebin/.gitignore



%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/erlang/lib/%{name}-%{version}/
cp -r ebin %{buildroot}/%{_libdir}/erlang/lib/%{name}-%{version}/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_libdir}/erlang/lib/%{name}-%{version}

%doc COPYING.txt
%doc README.txt
%doc SOURCE.txt


%changelog
* Sun Jan 9 2011 Ilia Cheishvili <ilia.cheishvili@gmail.com> - 2010-11-02-1
- Initial Package
