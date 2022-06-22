%global debug_package %{nil}
%global gem_name serverengine
Summary:        a framework to implement robust multiprocess servers like Unicorn
Name:           rubygem-%{gem_name}
Version:        2.2.5
Release:        1%{?dist}
License:        Apache 2.0
Vendor:         Microsoft Corporation
Distribution:   Mariner
Group:          Development/Languages
URL:            https://github.com/treasure-data/serverengine
Source0:        https://github.com/treasure-data/serverengine/archive/refs/tags/v%{version}.tar.gz#/%{gem_name}-%{version}.tar.gz
BuildRequires:  git
BuildRequires:  ruby
Requires:       rubygem-sigdump
Provides:       rubygem(%{gem_name}) = %{version}-%{release}

%description
a framework to implement robust multiprocess servers like Unicorn.

%prep
%setup -q -n %{gem_name}-%{version}

%build
gem build %{gem_name}

%install
gem install -V --local --force --install-dir %{buildroot}/%{gemdir} %{gem_name}-%{version}.gem
#add LICENSE file to buildroot from Source0
cp LICENSE %{buildroot}%{gem_instdir}/

%files
%defattr(-,root,root,-)
%license %{gemdir}/gems/%{gem_name}-%{version}/LICENSE
%{gemdir}

%changelog
* Wed Jun 22 2022 Neha Agarwal <nehaagarwal@microsoft.com> - 2.2.5-1
- Update to v2.2.5.
- Build from .tar.gz source.

* Mon Jan 04 2021 Henry Li <lihl@microsoft.com> - 2.2.1-1
- License verified
- Original version for CBL-Mariner
