%global version 4.10.0
%global scalapack_version 2.0.2
%global aster_root /cad/app/aster
%global aster_libs %{aster_root}/public
%global metis_ver 4.0.3
%global scotch_ver 5.1.11
%define debug_package %{nil}
%global _optflags -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic
%global _prefix %{aster_libs}/mumps-%{version}-openmpi/
%global libdir /usr/lib64
%global mpidir %{libdir}/openmpi
%global scalapackdir %{aster_libs}/scalapack-openmpi-%{scalapack_version}/

Name:           codeaster-mumps-openmpi
Version:        %{version}
Release:        1%{?dist}
Summary:	    Graph, mesh and hypergraph partitioning library; specifically for Code_Aster

License:        CeCILL-C
URL:            http://mumps.enseeiht.fr/
Source0:        codeaster-mumps-openmpi-%{version}.tar.gz
Source1:        wscript-mumps-openmpi

BuildRequires:	codeaster-metis codeaster-scotch codeaster-scalapack-openmpi
#BuildRequires:  openblas openblas-static openblas-devel openmpi openmpi-devel

%description
%description
MUMPS implements a direct solver for large sparse linear systems, with a particular focus on symmetric positive definite matrices. It can operate on distributed matrices e.g. over a cluster. It has Fortran and C interfaces, and can interface with ordering tools such as Scotch.
This is the Code_Aster specific package, which provides the optimal mumps lib for Code_Aster

%prep
%setup -q
LIBPATH="%{scalapackdir}/lib %{mpidir}/lib %{aster_libs}scotch-%{scotch_ver}/lib  %{aster_libs}metis-%{metis_ver}/lib/ %{libdir}" INCLUDES="%{scalapackdir}/include %{aster_libs}scotch-%{scotch_ver}/include/ %{aster_libs}metis-%{metis_ver}/include %{mpidir}/include/" ./waf configure --enable-mpi --maths-libs="openblas scalapack" --embed-maths --install-tests --prefix=%{buildroot}%{_prefix}
# patch for build
cp %SOURCE1 wscript
./waf build
mv Makefile.inc Makefile.inc.old
sed 's|LIBPAR =|SCALAP = %{scalapackdir}/lib/libscalapack.a %{libdir}/libopenblas.a\nLIBPAR = $(SCALAP)  -L%{mpidir}/lib/ -lmpi #-lmpi_f77|' < Makefile.inc.old > Makefile.inc

%build
make all

%install
rm -rf %{buildroot}
rm lib/.place_holder
mkdir -p %{buildroot}%{_prefix}include_seq
cp -r include %{buildroot}%{_prefix}/
cp -r lib %{buildroot}%{_prefix}/
cp libseq/mpi.h %{buildroot}%{_prefix}include_seq/
cp libseq/mpif.h %{buildroot}%{_prefix}include_seq/

%post

%preun

%files
%{_prefix}/lib/*
%{_prefix}/include/*
%{_prefix}/include_seq/*

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
