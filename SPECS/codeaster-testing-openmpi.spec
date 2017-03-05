%define version %{major_version}.%{sub_version}

%define debug_package %{nil}
%global _prefix %{aster_root}/%{major_version}mpi
%global config_file codeaster_testing_fedora_gnu_mpi_pack

Name:           codeaster-testing-openmpi
Version:        %{version}
Release:        1%{?dist}
Summary:	    Code_Aster finite element method solver. Testing version. With OpenMPI support.

License:        GPL2
URL:            http://www.code-aster.org
Source0:        codeaster-testing-openmpi-%{version}.tar.gz
Source1:        %{config_file}.py

AutoReqProv: no

Requires:	codeaster-testing-metis codeaster-testing-scotch codeaster-frontend codeaster-mfront codeaster-stable-petsc-openmpi libX11-devel
Requires:  openblas openblas-static openblas-devel openmpi openmpi-devel

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
export PATH=%{mpidir}/bin:%{aster_libs}/mfront-%{mfront_version}/bin:$PATH; export LD_LIBRARY_PATH=%{mpidir}/include:%{aster_libs}/mfront-%{mfront_version}/lib:$LD_LIBRARY_PATH; ./waf configure --use-config-dir=wafcfg --use-config=%{config_file} --prefix=%{_prefix}

%build

%install
rm -rf %{buildroot}
./waf install --destdir=%{buildroot} -p
%post
echo "vers : %{major_version}mpi:%{aster_root}/%{major_version}mpi/share/aster" >> %{aster_root}/etc/codeaster/aster

echo "MPI_DIR=%{mpidir}" >> %{aster_root}/etc/codeaster/profile_local.sh
echo "LD_LIBRARY_PATH=\$MPI_DIR/lib:\$LD_LIBRARY_PATH" >> %{aster_root}/etc/codeaster/profile_local.sh
echo "PATH=\$MPI_DIR/bin:\$PATH" >> %{aster_root}/etc/codeaster/profile_local.sh


%preun

%files
%{_prefix}/*

%postun
sed --in-place '\|vers : %{major_version}mpi:%{aster_root}/%{major_version}mpi/share/aster|d' %{aster_root}/etc/codeaster/aster
sed --in-place '\|MPI_DIR=%{mpidir}|d' %{aster_root}/etc/codeaster/profile_local.sh
sed --in-place '\|LD_LIBRARY_PATH=$MPI_DIR/lib:$LD_LIBRARY_PATH|d' %{aster_root}/etc/codeaster/profile_local.sh
sed --in-place '\|PATH=$MPI_DIR/bin:$PATH|d' %{aster_root}/etc/codeaster/profile_local.sh
%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Feb 8 2017 Stefan Reiterer 12.7
- Adaption for centos (personal)
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
