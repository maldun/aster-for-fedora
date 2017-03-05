%define version %{major_version}.%{sub_version}
%define debug_package %{nil}
%global _prefix %{aster_root}/%{major_version}
%global config_file codeaster_testing_fedora_gnu_config

Name:           codeaster-stable
Version:        %{version}
Release:        1%{?dist}
Summary:	    Code_Aster finite element method solver. Stable version.

License:        GPL2
URL:            http://www.code-aster.org
Source0:        codeaster-stable-%{version}.tar.gz
Source1:        %{config_file}.py

Requires:  codeaster-testing-metis codeaster-testing-scotch codeaster-frontend codeaster-mfront
Requires:  openblas openblas-static openblas-devel

%description
Code_Aster offers a full range of multiphysical analysisand modelling methods that go well beyond the standard
functions of a thermomechanical calculation code: from seismic analysis to
porous media via acoustics, fatigue, stochastic dynamics, etc. Its modelling, algorithms and solvers
are constantly under construction to improve and complete them (1,200,000 lines of code, 200 operators).
Resolutely open, it is linked, coupled and encapsulated in numerous ways.

This is the testing version.

%prep
%setup -q
cp %SOURCE1 wafcfg/
export PATH=%{aster_libs}/mfront-%{mfront_version}/bin:$PATH; export LD_LIBRARY_PATH=%{aster_libs}/mfront-%{mfront_version}/lib:$LD_LIBRARY_PATH; ./waf configure --use-config-dir=wafcfg --use-config=%{config_file} --prefix=%{_prefix}

%build

%install
rm -rf %{buildroot}
./waf install --destdir=%{buildroot} -p
%post
echo "vers : %{major_version}:%{aster_root}/%{major_version}/share/aster" >> %{aster_root}/etc/codeaster/aster

%preun

%postun
sed --in-place '\|vers : %{major_version}:%{aster_root}/%{major_version}/share/aster|d' %{aster_root}/etc/codeaster/aster

%files
%{_prefix}/*

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Mar 3 2017 Stefan Reiterer 13.3
- Adaption for fedora (personal)
* Wed Feb 8 2017 Stefan Reiterer 12.7
- Adaption for centos (personal)
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
