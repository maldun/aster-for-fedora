%global version 11.4
%global aster_root /opt/Code_Aster/aster_root
%global aster_libs /usr/lib64/codeaster/
%define debug_package %{nil}
%global libdir /usr/lib64
%global mpidir /usr/lib64/openmpi
%global _prefix %{aster_root}/public/homard-%{version}/

Name:           codeaster-homard
Version:        %{version}
Release:        1%{?dist}
Summary:	    A subset of LAPACK routines redesigned for heterogeneous computing; specifically for Code_Aster

License:        Commercial. See below for more information
URL:            http://www.code-aster.org/outils/homard/menu_homard.en.htm
Source0:        codeaster-homard-%{version}.tar.gz


BuildRequires: codeaster-frontend
BuildRequires: python, python-setuptools

%description
The HOMARD software carries out the adaptation of 2D/3D finite element or
   finite volume meshes by refinement and unrefinement techniques.
   
This is the Code_Aster specific package, which provides the homard lib for Code_Aster.

The free downloading of HOMARD software is only allowed for coupling with Code_Aster. Please contact HOMARD project: homard[at]edf.fr
Visit the site: http://www.code-aster.org/outils/homard/menu_homard.en.htm for a description of HOMARD.
HOMARD is a trade mark of Electricité de France.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{aster_root}/outils
%{__python} setup_homard.py --prefix=%{buildroot}%{_prefix}
cd %{buildroot}%{_prefix}
rm -f homard
ln -sf ASTER_HOMARD/homard homard
ln -sf ASTER_HOMARD/homard ../../outils/homard

%post


%preun

%files
%{_prefix}/*
%{aster_root}/outils/homard

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Thu May 12 2016 Stefan Reiterer
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
