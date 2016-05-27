%global major_version 13.1
%global version %{major_version}.0
%global mfront_version 2.0.3

%global aster_root /opt/Code_Aster/aster_root
%global aster_libs /usr/lib64/codeaster/
%define debug_package %{nil}
%global _prefix %{aster_root}/%{major_version}

Name:           codeaster-testing-astest
Version:        %{version}
Release:        1%{?dist}
Summary:	    Code_Aster finite element method solver. Testing version.

License:        GPL2
URL:            http://www.code-aster.org
Source0:        codeaster-testing-astest-%{version}.tar.gz

BuildRequires:	codeaster-testing

%description
Code_Aster offers a full range of multiphysical analysisand modelling methods that go well beyond the standard
functions of a thermomechanical calculation code: from seismic analysis to
porous media via acoustics, fatigue, stochastic dynamics, etc. Its modelling, algorithms and solvers
are constantly under construction to improve and complete them (1,200,000 lines of code, 200 operators).
Resolutely open, it is linked, coupled and encapsulated in numerous ways.

This are the testcase for the testing version.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}/share/aster
cp -r astest %{buildroot}%{_prefix}/share/aster/tests
%post

%preun

%postun

%files
%{_prefix}/share/aster/tests/*

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
