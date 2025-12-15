%define module types-psutil
%define oname types_psutil

Name:		python-types-psutil
Version:	7.1.3.20251211
Release:	1
Summary:	Typing stubs for psutil
URL:		https://pypi.org/project/types-psutil/
License:	Apache-2.0
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/t/types-psutil/%{oname}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(setuptools)

%description
Typing stubs for psutil.

%files
%{py_sitedir}/psutil-stubs
%{py_sitedir}/%{oname}-%{version}.dist-info
%license LICENSE
%doc README.md
