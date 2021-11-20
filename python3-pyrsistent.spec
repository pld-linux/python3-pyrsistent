#
# Conditional build:
%bcond_without	tests	# unit tests

%define		module	pyrsistent
Summary:	Persistent/Functional/Immutable data structures
Summary(pl.UTF-8):	Trwałe/funkcyjne/niezmienne struktury danych
Name:		python3-pyrsistent
Version:	0.16.0
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyrsistent/
Source0:	https://files.pythonhosted.org/packages/source/p/pyrsistent/%{module}-%{version}.tar.gz
# Source0-md5:	4ba30da6f0a63554e70ac6c4c1904929
URL:		http://github.com/tobgu/pyrsistent/
BuildRequires:	python3-devel >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-hypothesis
# < 5? works also with 5.4.1
BuildRequires:	python3-pytest < 5
BuildRequires:	python3-six
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pyrsistent is a number of persistent collections (by some referred to
as functional data structures). Persistent in the sense that they are
immutable.

%description -l pl.UTF-8
Pyrsistent to zbiór trwałych kolekcji (nazywanych także funkcyjnymi
strukturami danych). Są trwałe w tym sensie, że są niezmienne.

%prep
%setup -q -n %{module}-%{version}

# Remove bundled egg-info
%{__rm} -r %{module}.egg-info

%build
%py3_build

%if %{with tests}
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENCE.mit README.rst
%attr(755,root,root) %{py3_sitedir}/pvectorc.cpython-*.so
%{py3_sitedir}/_pyrsistent_version.py
%{py3_sitedir}/__pycache__/_pyrsistent_version.cpython-*.py[co]
%{py3_sitedir}/pyrsistent
%{py3_sitedir}/pyrsistent-%{version}-py*.egg-info
