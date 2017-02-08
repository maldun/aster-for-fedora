%global version 5.1.11
%global aster_root /cad/app/aster
%global aster_libs public
%define debug_package %{nil}
%global _optflags -O2 -g -pipe -Wall -Wp,-D_FORTIFY_SOURCE=2 -fexceptions --param=ssp-buffer-size=4 -grecord-gcc-switches -m64 -mtune=generic

Name:           codeaster-scotch
Version:        %{version}
Release:        1%{?dist}
Summary:	    Graph, mesh and hypergraph partitioning library; specifically for Code_Aster

License:        CeCILL-C
URL:            http://www.labri.fr/perso/pelegrin/scotch/
Source0:        codeaster-scotch-5.1.11.tar.gz
Source1:        scotch-Makefile.inc.in

BuildRequires:	flex bison mpich-devel zlib-devel bzip2-devel openblas lzma-devel

%description
%description
Scotch is a software package for graph and mesh/hypergraph partitioning and
sparse matrix ordering. 
This is the Code_Aster specific package, which provides the optimal scotch lib for Code_Aster

%prep
%setup -q
sed 's|@CFLAGS@|%{_optflags} -fno-stack-protector -fPIC|'< %SOURCE1 > src/Makefile.inc.old
sed 's|@LDFLAGS@|-L%{aster_root}/%{aster_libs}/OpenBLAS/lib/ -lopenblas|' < src/Makefile.inc.old > src/Makefile.inc
rm -f src/Makefile.inc.old

%build
#Do out of tree builds
%global _prefix %{aster_root}/%{aster_libs}/scotch-%{version}/
#Serial build
cd src/
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
cd src/
make install prefix=%{buildroot}%{_prefix} 
rm -rf %{buildroot}%{_prefix}/share

%post


%preun

%files
%{_prefix}/lib/*
%{_prefix}/include/*
%{_prefix}/bin/*

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Feb 8 2017 Stefan Reiterer 5.1.11-aster3
- Adaption for centos (personal)
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
