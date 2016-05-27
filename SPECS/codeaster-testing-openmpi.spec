%global major_version 13.1
%global version %{major_version}.0
%global mfront_version 2.0.3

%global aster_root /opt/Code_Aster/aster_root
%global aster_libs /usr/lib64/codeaster/
%define debug_package %{nil}
%global _prefix %{aster_root}/%{major_version}mpi
%global config_file codeaster_fedora_gnu_mpi_pack

Name:           codeaster-testing-openmpi
Version:        %{version}
Release:        1%{?dist}
Summary:	    Code_Aster finite element method solver. Testing version. With OpenMPI support.

License:        GPL2
URL:            http://www.code-aster.org
Source0:        codeaster-testing-openmpi-%{version}.tar.gz
Source1:        %{config_file}.py

AutoReqProv: no

BuildRequires:	codeaster-metis codeaster-scotch openblas openblas-static openblas-devel codeaster-frontend codeaster-mfront openmpi openmpi-devel codeaster-petsc-openmpi

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
export PATH=%{aster_libs}/mfront-%{mfront_version}/bin:$PATH; export LD_LIBRARY_PATH=%{aster_libs}/mfront-%{mfront_version}/lib:$LD_LIBRARY_PATH; ./waf configure --use-config-dir=wafcfg --use-config=%{config_file} --prefix=%{buildroot}%{_prefix}

%build

%install
rm -rf %{buildroot}
./waf install -p
cp -r astest %{buildroot}%{_prefix}
%post
echo "vers : %{major_version}mpi:%{aster_root}/%{major_version}mpi/share/aster" >> %{aster_root}/etc/codeaster/aster

%preun

%files
%{_prefix}/*

%postun
sed --in-place '\|vers : %{major_version}mpi:%{aster_root}/%{major_version}mpi/share/aster|d' %{aster_root}/etc/codeaster/aster

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
