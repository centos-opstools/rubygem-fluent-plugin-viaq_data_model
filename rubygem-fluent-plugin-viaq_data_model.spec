# Generated from fluent-plugin-viaq_data_model-0.0.3.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fluent-plugin-viaq_data_model

Name: rubygem-%{gem_name}
Version: 0.0.13
Release: 1%{?dist}
Summary: Filter plugin to ensure data is in the ViaQ common data model
Group: Development/Languages
License: ASL 2.0
URL: https://github.com/ViaQ/fluent-plugin-viaq_data_model
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 2.0.0
Requires: rubygem(fluentd) >= 0.12.0
# the following BuildRequires are development dependencies
BuildRequires: rubygem(rake)
BuildRequires: rubygem(bundler)
BuildRequires: rubygem(fluentd) >= 0.12.0
BuildRequires: rubygem(rr) >= 1.0
BuildRequires: rubygem(rr) < 2
BuildRequires: rubygem(test-unit)
BuildRequires: rubygem(test-unit-rr) >= 1.0
BuildRequires: rubygem(test-unit-rr) < 2
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Filter plugin to ensure data is in the ViaQ common data model.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

# Run the test suite
%check
pushd .%{gem_instdir}
rake test
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%license %{gem_instdir}/LICENSE
%{gem_instdir}/filter-viaq_data_model.conf
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/Vagrantfile
%{gem_instdir}/fluent-plugin-viaq_data_model.gemspec
%{gem_instdir}/test

%changelog
* Wed Dec 13 2017 Rich Megginson <rmeggins@redhat.com> - 0.0.13-1
- bug 1494612. Orphan records missing namespace_name and/or namespace_id

* Mon Nov 20 2017 Rich Megginson <rmeggins@redhat.com> - 0.0.12-1
- Bug 1514110 - Aggregated Logging replacing all log levels with
-   '3' and '6' after upgrade to 3.5 from 3.4
-   https://bugzilla.redhat.com/show_bug.cgi?id=1514110

* Thu Sep 28 2017 Rich Megginson <rmeggins@redhat.com> - 0.0.11-1
- added a test fix

* Thu Sep 28 2017 Rich Megginson <rmeggins@redhat.com> - 0.0.10-1
- add support for eventrouter

* Wed Sep 13 2017 Rich Megginson <rmeggins@redhat.com> - 0.0.9-1
- fix json-file and sys var log record handling

* Tue Sep  5 2017 Rich Megginson <rmeggins@redhat.com> - 0.0.8-1
- use test-unit-rr instead of flexmock

* Thu Aug 31 2017 Rich Megginson <rmeggins@redhat.com> - 0.0.7-1
- allow disabling processing for formatters and index names
- preserve @timestamp
- improve time handling

* Mon Aug 28 2017 Rich Megginson <rmeggins@redhat.com> - 0.0.6-1
- do viaq processing/formatting in ruby code; create index names

* Tue Jun 13 2017 Rich Megginson <rmeggins@redhat.com> - 0.0.5-1
- Fix bug that caused array values to be dropped

* Wed Feb 15 2017 Rich Megginson <rmeggins@redhat.com> - 0.0.3-1
- Initial package
