%global version 2.0.3
%global aster_root /cad/app/aster
%global aster_libs %{aster_root}/public
%define debug_package %{nil}
%global _prefix %{aster_libs}/mfront-%{version}/
%global libdir /usr/lib64
%global mpidir %{libdir}/openmpi

Name:           codeaster-mfront
Version:        %{version}
Release:        1%{?dist}
Summary:	    Library for material modeling; specifically for Code_Aster

License:        GPL (GNU General Public License, version 3) and CeCILL-C
URL:            http://tfel.sourceforge.net/about.html
Source0:        codeaster-mfront-%{version}.tar.gz

BuildRequires:	cmake python boost boost-devel boost-python

%description
MFront is a code generator which translates a set of
closely related domain specific languages into plain C++ on top of the
TFEL library

%prep
%setup -q
cmake -DCMAKE_BUILD_TYPE=Release -Dlocal-castem-header=ON -Denable-fortran=ON -Ddisable-reference-doc=ON -Ddisable-website=ON -Denable-aster=ON -Denable-python=ON -Denable-python-bindings=ON -Denable-portable-build=ON -DCMAKE_INSTALL_PREFIX=%{_prefix}

%build
make

%install
make DESTDIR=%{buildroot} install

# create symlink for aster
cd %{buildroot}%{_prefix}/bin
ln -s mfront mfront-%{version}

%post

%preun

%files
%{_prefix}/lib/*
%{_prefix}/include/*
%{_prefix}/bin/*
%{_prefix}/share/*

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Feb 8 2017 Stefan Reiterer 2.0.3
- Adaption for centos (personal)
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
