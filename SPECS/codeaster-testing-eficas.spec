%global aster_version 13.1
%global version 2015.2
%global mfront_version 2.0.3

%global aster_root /opt/Code_Aster/aster_root
%global aster_libs /usr/lib64/codeaster/
%define debug_package %{nil}
%global _prefix %{aster_root}/public/
%global bindir /usr/bin/

Name:           codeaster-testing-eficas
Version:        %{version}
Release:        1%{?dist}
Summary:	    Eficas is an graphical editor for Code_Aster command files.

License:        GPL2
URL:            http://www.code-aster.org
Source0:        codeaster-testing-eficas-%{version}.tar.gz

BuildRequires:	codeaster-frontend

%description
Eficas is an graphical editor for Code_Aster command files.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{aster_root}/outils

cp -r eficas-%{version} %{buildroot}%{_prefix}
rm -f %{buildroot}%{_prefix}/eficas-%{version}/.branches

cd %{buildroot}%{_prefix}
ln -sf %{_prefix}/eficas-%{version}/eficasQt %{buildroot}%{aster_root}/outils/eficasQt
ln -sf %{aster_root}/outils/eficasQt %{buildroot}%{aster_root}/outils/eficas

mkdir -p ${RPM_BUILD_ROOT}%{bindir}
ln -sf %{_prefix}/eficas-%{version}/eficasQt %{buildroot}/%{bindir}
ln -sf %{_prefix}/eficas-%{version}/eficasQt %{buildroot}/%{bindir}/eficas
%post

%preun

%postun

%files
%{_prefix}/eficas-%{version}/*
%{aster_root}/outils/eficasQt
%{aster_root}/outils/eficas
%{bindir}/eficasQt
%{bindir}/eficas

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
