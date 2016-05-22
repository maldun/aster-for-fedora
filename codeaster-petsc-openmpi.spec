%global version 3.4.5
%global scalapack_version 2.0.2
%global aster_root /opt/Code_Aster/aster_root
%global aster_libs /usr/lib64/codeaster/
%define debug_package %{nil}
%global _optflags -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic
%global _prefix %{aster_libs}/petsc-%{version}/
%global libdir /usr/lib64
%global includedir /usr/include
%global mpidir %{libdir}/openmpi
%global scalapackdir %{aster_libs}/scalapack-openmpi-%{scalapack_version}/

Name:           codeaster-petsc-openmpi
Version:        %{version}
Release:        1%{?dist}
Summary:        Portable Extensible Toolkit for Scientific Computation

License:        MIT
URL:            http://www.mcs.anl.gov/petsc/
Source0:        codeaster-petsc-openmpi-%{version}.tar.gz

BuildRequires:	codeaster-metis codeaster-scotch openblas openblas-static openblas-devel openmpi openmpi-devel codeaster-scalapack-openmpi codeaster-hdf5
BuildRequires:  gcc-c++ gcc-gfortran
BuildRequires:  openblas-devel openssl-devel zlib-devel hypre-openmpi-devel

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
PETSC_ARCH=arch-linux2-c-opt ./config/configure.py --with-mpi-dir=%{mpidir} --with-blas-lapack-lib=%{libdir}/libopenblas.a  --download-hypre=no --download-ml=no --with-debugging=0 COPTFLAGS=-O2 CXXOPTFLAGS=-O2 FOPTFLAGS=-O2 --configModules=PETSc.Configure --optionsModule=PETSc.compilerOptions  --with-x=0   --with-scalapack=1 --with-scalapack-dir=%{scalapackdir} --with-shared-libraries=0 --prefix=%{_prefix}

make V=1

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}
make install DESTDIR=%{buildroot}%{_prefix}

mv %{buildroot}%{_prefix}/bin/mpiexec.prun %{buildroot}%{_prefix}/bin/mpiexec.prun.old
sed -e 's|^#![\t]*#!/usr/local/bin/bash|#!/usr/bin/bash|' < %{buildroot}%{_prefix}/bin/mpiexec.prun.old > %{buildroot}%{_prefix}/bin/mpiexec.prun
mv %{buildroot}%{_prefix}/bin/mpiexec.poe %{buildroot}%{_prefix}/bin/mpiexec.poe.old
sed -e 's|^#![\t]*#!/usr/local/bin/bash|#!/usr/bin/bash|' < %{buildroot}%{_prefix}/bin/mpiexec.poe.old > %{buildroot}%{_prefix}/bin/mpiexec.poe
mv %{buildroot}%{_prefix}/bin/mpiexec.llrun %{buildroot}%{_prefix}/bin/mpiexec.llrun.old
sed -e 's|^#![\t]*#!/usr/local/bin/bash|#!/usr/bin/bash|' < %{buildroot}%{_prefix}/bin/mpiexec.llrun.old > %{buildroot}%{_prefix}/bin/mpiexec.llrun
rm %{buildroot}%{_prefix}/bin/mpiexec.*.old
%post

%preun

%files
%{_prefix}/*

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
