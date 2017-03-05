%define debug_package %{nil}
%global _optflags -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic
%global _prefix %{aster_libs}/petsc-%{version}/
%global scalapackdir %{aster_libs}/scalapack-openmpi-%{scalapack_version}/

Name:           codeaster-testing-petsc-openmpi
Version:        %{version}
Release:        1%{?dist}
Summary:        Portable Extensible Toolkit for Scientific Computation

License:        MIT
URL:            http://www.mcs.anl.gov/petsc/
Source0:        codeaster-testing-petsc-openmpi-%{version}.tar.gz

Requires:	codeaster-testing-metis codeaster-testing-scotch  codeaster-scalapack-openmpi codeaster-hdf5
Requires:  gcc-c++ gcc-gfortran
Requires:  openblas openblas-static openblas-devel openmpi openmpi-devel openblas-devel
BuildRequires:  openssl-devel zlib-devel
#BuildRequires:  hypre-openmpi-devel hypre-devel SuperLU-devel

%description
PETSc is the "Portable Extensible Toolkit for Scientific Computation",\
a suite of data structures and routines for the scalable (parallel)\
solution of scientific applications modeled by partial differential\
equations.  It employs the MPI standard for all message-passing\
communication.  Several sample scientific applications, as well as\
various papers and talks, demonstrate the features of the PETSc\
libraries.
This is the Code_Aster specific package, which provides the correct PETSc lib for Code_Aster

%prep
%setup -q

%build
PETSC_ARCH=arch-linux2-c-opt ./config/configure.py --LIBS="-L%{aster_libs}/%{scotch_lib}/lib -lesmumps -lscotch -lscotcherr -lscotcherrexit -lscotchmetis" --with-openmp=1 --with-metis-dir=%{aster_libs}/%{metis_lib} --with-mpi-dir=%{mpidir} --with-blas-lapack-lib=%{openblasdir}/libopenblas.a  --with-mumps-dir=%{aster_libs}/%{mumps_lib}-openmpi/ --download-hypre=no --download-ml=no --with-debugging=0 COPTFLAGS=-O2 CXXOPTFLAGS=-O2 FOPTFLAGS=-O2 --with-ssl=0 --configModules=PETSc.Configure --optionsModule=PETSc.compilerOptions  --with-x=0   --with-scalapack=1 --with-scalapack-dir=%{scalapackdir} --with-shared-libraries=0 --prefix=%{_prefix}

make V=1

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
make install DESTDIR=%{buildroot}%{_prefix}

# mv %{buildroot}%{_prefix}/bin/mpiexec.prun %{buildroot}%{_prefix}/bin/mpiexec.prun.old
# sed -e 's|^#![\t]*#!/usr/local/bin/bash|#!/usr/bin/bash|' < %{buildroot}%{_prefix}/bin/mpiexec.prun.old > %{buildroot}%{_prefix}/bin/mpiexec.prun
# mv %{buildroot}%{_prefix}/bin/mpiexec.poe %{buildroot}%{_prefix}/bin/mpiexec.poe.old
# sed -e 's|^#![\t]*#!/usr/local/bin/bash|#!/usr/bin/bash|' < %{buildroot}%{_prefix}/bin/mpiexec.poe.old > %{buildroot}%{_prefix}/bin/mpiexec.poe
# mv %{buildroot}%{_prefix}/bin/mpiexec.llrun %{buildroot}%{_prefix}/bin/mpiexec.llrun.old
# sed -e 's|^#![\t]*#!/usr/local/bin/bash|#!/usr/bin/bash|' < %{buildroot}%{_prefix}/bin/mpiexec.llrun.old > %{buildroot}%{_prefix}/bin/mpiexec.llrun
# rm %{buildroot}%{_prefix}/bin/mpiexec.*.old
%post

%preun

%files
%{_prefix}/*

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Sat Mar 3 2017 Stefan Reiterer 3.7.3
- Adaption for fedora (personal)
* Wed Feb 8 2017 Stefan Reiterer 3.4.5
- Adaption for centos (personal)
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
