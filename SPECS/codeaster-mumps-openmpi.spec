%global version 4.10.0
%global scalapack_version 2.0.2
%global aster_root /cad/app/aster
%global aster_libs %{aster_root}/public
%define debug_package %{nil}
%global _optflags -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic
%global _prefix %{aster_libs}/mumps-%{version}-openmpi/
%global libdir /usr/lib64
%global mpidir /cad/app/openmpi/10.0.5
%global scalapackdir %{aster_libs}/scalapack-openmpi-%{scalapack_version}/

Name:           codeaster-mumps-openmpi
Version:        %{version}
Release:        1%{?dist}
Summary:	    Graph, mesh and hypergraph partitioning library; specifically for Code_Aster

License:        CeCILL-C
URL:            http://mumps.enseeiht.fr/
Source0:        codeaster-mumps-%{version}-openmpi.tar.gz
Source1:        wscript-mumps-openmpi

BuildRequires:	codeaster-metis codeaster-scotch openblas openblas-static openblas-devel openmpi openmpi-devel codeaster-scalapack-openmpi

%description
%description
MUMPS implements a direct solver for large sparse linear systems, with a particular focus on symmetric positive definite matrices. It can operate on distributed matrices e.g. over a cluster. It has Fortran and C interfaces, and can interface with ordering tools such as Scotch.
This is the Code_Aster specific package, which provides the optimal mumps lib for Code_Aster

%prep
%setup -q
LIBPATH="%{scalapackdir}/lib %{mpidir}/lib %{aster_libs}scotch-5.1.11_esmumps/lib  %{aster_libs}metis-4.0.3/lib/ %{libdir}" INCLUDES="%{scalapackdir}/include %{aster_libs}scotch-5.1.11_esmumps/include/ %{aster_libs}metis-4.0.3/include %{mpidir}/include/" ./waf configure --enable-mpi --maths-libs="openblas scalapack" --embed-maths --install-tests --prefix=%{buildroot}%{_prefix}
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
* Sat Mar 3 2017 Stefan Reiterer 5.0.2-aster
- Adaption for fedora (personal)
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
