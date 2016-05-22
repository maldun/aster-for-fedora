%global version 2.0.3
%global aster_root /opt/Code_Aster/aster_root
%global aster_libs /usr/lib64/codeaster/
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

BuildRequires:	cmake python boost-python

%description
MFront is a code generator which translates a set of
closely related domain specific languages into plain C++ on top of the
TFEL library

%prep
%setup -q
cmake -DCMAKE_BUILD_TYPE=Release -Dlocal-castem-header=ON -Denable-fortran=ON -Ddisable-reference-doc=ON -Ddisable-website=ON -Denable-aster=ON -Denable-python=ON -Denable-python-bindings=ON -Denable-portable-build=ON -DCMAKE_INSTALL_PREFIX=%{buildroot}%{_prefix}

%build
make

%install
make install

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
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
