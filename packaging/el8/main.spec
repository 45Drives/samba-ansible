Name: ::package_name::
Version: ::package_version::
Release: ::package_build_version::%{?dist}
Summary: ::package_description_short::
License: ::package_licence::
URL: ::package_url::
Source0: %{name}-%{version}.tar.gz
BuildArch: ::package_architecture_el::
Requires: ::package_dependencies_el::

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
::package_title::
::package_description_long::

%prep
%setup -q

%build

%install
make DESTDIR=%{buildroot} install

%files
/usr/share/samba-ansible/*

%changelog
* Wed Jun 22 2022 Mark Hooper <mhooper@45drives.com> 1.1.2-5
- updated smd.conf.j2
* Thu Jun 09 2022 Mark Hooper <mhooper@45drives.com> 1.1.2-4
- removed kerberos_init.yml playbook
* Thu Jun 09 2022 Mark Hooper <mhooper@45drives.com> 1.1.2-3
- added a kerberos_init.yml playbook
* Wed Jun 08 2022 Mark Hooper <mhooper@45drives.com> 1.1.2-2
- removed krb5 packages as dependencies
- fixed incorrect logic when configuring idmap backend
- use shell module in firewalld validate task
- set executable option as /bin/bash in firewalld validate task
* Wed Jun 08 2022 Mark Hooper <mhooper@45drives.com> 1.1.1-4
- removed krb5 packages as dependencies
- fixed incorrect logic when configuring idmap backend
- use shell module in firewalld validate task
- set executable option as /bin/bash in firewalld validate task
* Thu Jun 02 2022 Brett Kelly <bkelly@45drives.com> 1.1.1-3
- fixed another syntax error
* Thu Jun 02 2022 Brett Kelly <bkelly@45drives.com> 1.1.1-2
- fixed syntax in net wrapper script
* Tue May 31 2022 Brett Kelly <bkelly@45drives.com> 1.1.1-1
- create cephx keyring when using cephfs as backend
* Thu May 19 2022 Brett Kelly <bkelly@45drives.com> 1.1.0-2
- set winbind as default join method
* Thu May 19 2022 Brett Kelly <bkelly@45drives.com> 1.1.0-1
- v1.1.0 release
* Thu May 19 2022 Brett Kelly <bkelly@45drives.com> 1.0.0-3
- fixed syntax error when cleaning sssd cache
- added log level and server string
* Wed May 18 2022 Brett Kelly <bkelly@45drives.com> 1.0.0-2
- added firewalld validation check
- updated anisble.cfg
* Wed Mar 30 2022 Brett Kelly <bkelly@45drives.com> 1.0.0-1
- initial pre-release build