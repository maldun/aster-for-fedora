%global version 4.10.0
%global aster_root /cad/app/aster
%global aster_libs %{aster_root}/lib
%define debug_package %{nil}
%global _optflags -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic
%global _prefix %{aster_libs}/mumps-%{version}/

Name:           codeaster-mumps
Version:        %{version}
Release:        1%{?dist}
Summary:	    Graph, mesh and hypergraph partitioning library; specifically for Code_Aster

License:        CeCILL-C
URL:            http://mumps.enseeiht.fr/
Source0:        codeaster-mumps-%{version}.tar.gz

BuildRequires:	codeaster-metis codeaster-scotch openblas openblas-static openblas-devel

%description
%description
MUMPS implements a direct solver for large sparse linear systems, with a particular focus on symmetric positive definite matrices. It can operate on distributed matrices e.g. over a cluster. It has Fortran and C interfaces, and can interface with ordering tools such as Scotch.
This is the Code_Aster specific package, which provides the optimal mumps lib for Code_Aster

%prep
%setup -q
LIBPATH="%{aster_libs}scotch-5.1.11/lib  %{aster_libs}metis-4.0.3/lib/ /usr/lib64/" INCLUDES="%{aster_libs}scotch-5.1.11/include/ %{aster_libs}metis-4.0.3/include" ./waf configure --maths-libs="openblas" --embed-maths --install-tests --prefix=%{buildroot}%{_prefix}


%build

%install
rm -rf %{buildroot}
./waf install -p
rm -rf %{buildroot}%{_prefix}/share

%post

%preun

%files
%{_prefix}/lib/*
%{_prefix}/include/*
%{_prefix}/include_seq/*

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Feb 8 2017 Stefan Reiterer 4.10.0-aster3
- Adaption for centos (personal)
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
