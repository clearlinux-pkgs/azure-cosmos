#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-cosmos
Version  : 3.1.2
Release  : 3
URL      : https://files.pythonhosted.org/packages/9c/47/c77b0008c9f3bf90c533a7f538b149c7cd28d2d9c5303d3fc017ada6c09c/azure-cosmos-3.1.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/9c/47/c77b0008c9f3bf90c533a7f538b149c7cd28d2d9c5303d3fc017ada6c09c/azure-cosmos-3.1.2.tar.gz
Summary  : Azure Cosmos Python SDK
Group    : Development/Tools
License  : MIT
Requires: azure-cosmos-python = %{version}-%{release}
Requires: azure-cosmos-python3 = %{version}-%{release}
Requires: requests
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : requests
BuildRequires : six

%description
Azure Cosmos DB is a globally distributed, multi-model database service that supports document, key-value, wide-column, and graph databases.
        
        Use the Azure Cosmos DB SQL API SDK for Python to manage databases and the JSON documents they contain in this NoSQL database service.
        
        * Create Cosmos DB **databases** and modify their settings
        * Create and modify **containers** to store collections of JSON documents
        * Create, read, update, and delete the **items** (JSON documents) in your containers
        * Query the documents in your database using **SQL-like syntax**
        
        Looking for source code or API reference?
        
        * [SDK source code][source_code]
        * [SDK reference documentation][ref_cosmos_sdk]
        
        Please see the latest version of the [Azure Cosmos DB Python SDK for SQL API][ref_v4_source]
        
        ## Getting started
        
        * Azure subscription - [Create a free account][azure_sub]
        * Azure [Cosmos DB account][cosmos_account] - SQL API
        * [Python 2.7 or 3.5.3+][python]

%package python
Summary: python components for the azure-cosmos package.
Group: Default
Requires: azure-cosmos-python3 = %{version}-%{release}

%description python
python components for the azure-cosmos package.


%package python3
Summary: python3 components for the azure-cosmos package.
Group: Default
Requires: python3-core
Provides: pypi(azure_cosmos)
Requires: pypi(requests)
Requires: pypi(six)

%description python3
python3 components for the azure-cosmos package.


%prep
%setup -q -n azure-cosmos-3.1.2
cd %{_builddir}/azure-cosmos-3.1.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1588781266
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## Remove excluded files
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/__init__.py
rm -f %{buildroot}/usr/lib/python3.8/site-packages/azure/__pycache__/__init__.cpython-38.pyc

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
