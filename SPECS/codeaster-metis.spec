%global version 4.0.3
%global aster_root /cad/app/aster
%global aster_libs lib
%define debug_package %{nil}


Name:           codeaster-metis
Version:        %{version}
Release:        1%{?dist}
Summary:        Serial Graph Partitioning and Fill-reducing Matrix Ordering; specifically for Code_Aster

License:        ASL 2.0 and BSD and LGPLv2+
URL:            http://code-aster.org/
Source0:        codeaster-metis-4.0.3.tar.gz

BuildRequires: cmake
BuildRequires: pcre-devel

%description
%description
METIS is a set of serial programs for partitioning graphs, 
partitioning finite element meshes, and producing fill reducing 
orderings for sparse matrices. 
The algorithms implemented in METIS are based on the multilevel 
recursive-bisection, multilevel k-way, and multi-constraint 
partitioning schemes developed in our lab.
METIS is distributed with OpenMP support.
This is the Code_Aster specific package, which provides the optimal metis lib for Code_Aster

%prep
%setup -q

%build
#Do out of tree builds
%global _prefix %{aster_root}/%{aster_libs}/metis-%{version}/
#Serial build
export CFLAGS='-std=gnu9x -fno-stack-protector -O2 -fPIC'
export CC=gcc
export CXX=g++
export F9X=gfortran
export LDFLAGS='-l%{aster_libs}/OpenBLAS/lib/libopenblas.a'
make

%install
make install prefix=%{buildroot}%{_prefix} 

%post

%preun

%files
%{_prefix}/lib/*
%{_prefix}/include/*
%{_prefix}/bin/*

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Feb 8 2017 Stefan Reiterer 4.0.3-1
- Adaption for centos (personal)
* Thu May 12 2016 Stefan Reiterer 4.0.3
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
