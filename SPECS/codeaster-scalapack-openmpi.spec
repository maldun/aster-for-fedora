%global version 2.0.2
%global aster_root /cad/app/aster
%global aster_libs %{aster_root}/public
%define debug_package %{nil}
%global openblasdir %{aster_libs}/OpenBLAS/lib
%global mpidir /cad/app/openmpi/1.10.5
%global _prefix %{aster_libs}/scalapack-openmpi-%{version}/

Name:           codeaster-scalapack-openmpi
Version:        %{version}
Release:        1%{?dist}
Summary:	    A subset of LAPACK routines redesigned for heterogeneous computing; specifically for Code_Aster

License:        Public Domain
URL:            http://www.netlib.org/scalapack/
Source0:        codeaster-scalapack-openmpi-%{version}.tar.gz


#BuildRequires: lapack-devel, blas-devel, openblas
BuildRequires: gcc-gfortran, glibc-devel
#BuildRequires: mpich-devel-static
#BuildRequires: openmpi-devel

%description
%description
The ScaLAPACK (or Scalable LAPACK) library includes a subset 
of LAPACK routines redesigned for distributed memory MIMD 
parallel computers. It is currently written in a 
Single-Program-Multiple-Data style using explicit message 
passing for inter-processor communication. It assumes 
matrices are laid out in a two-dimensional block cyclic 
decomposition.

ScaLAPACK is designed for heterogeneous computing and is 
portable on any computer that supports MPI or PVM.

Like LAPACK, the ScaLAPACK routines are based on 
block-partitioned algorithms in order to minimize the frequency 
of data movement between different levels of the memory hierarchy. 
(For such machines, the memory hierarchy includes the off-processor 
memory of other processors, in addition to the hierarchy of registers, 
cache, and local memory on each processor.) The fundamental building 
blocks of the ScaLAPACK library are distributed memory versions (PBLAS) 
of the Level 1, 2 and 3 BLAS, and a set of Basic Linear Algebra 
Communication Subprograms (BLACS) for communication tasks that arise 
frequently in parallel linear algebra computations. In the ScaLAPACK 
routines, all inter-processor communication occurs within the PBLAS and the 
BLACS. One of the design goals of ScaLAPACK was to have the ScaLAPACK 
routines resemble their LAPACK equivalents as much as possible. 

This is the Code_Aster specific package, which provides the optimal scalapck lib for Code_Aster.
The repackaging was necessary to be compatible with the codeaster-mumps-openmpi library.

%prep
%setup -q

%build

%install
cd scalapack_installer_1.0.2
mkdir -p %{buildroot}%{_prefix}
./setup.py --lapacklib=%{openblasdir}/libopenblas.a --mpicc=%{mpidir}/bin/mpicc --mpif90=%{mpidir}/bin/mpif90 --mpiincdir=%{mpidir}/include --ldflags_c=-fopenmp --ldflags_fc=-fopenmp --notesting --prefix=%{buildroot}%{_prefix}

%post


%preun

%files
%{_prefix}/lib/*
%{_prefix}/include

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
