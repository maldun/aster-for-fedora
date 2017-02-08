%global aster_root /cad/app/aster
%global aster_libs %{_libdir}/codeaster
%global metis_version 4.0.3
%define debug_package %{nil}


Name:           codeaster-frontend
Version:        1.13.9
Release:        1%{?dist}
Summary:        The Code_Aster-Frontend Package/Structure

License:        GPLv2
URL:            https://bitbucket.org/code_aster/codeaster-frontend
Source0:        https://bitbucket.org/code_aster/codeaster-frontend/codeaster-frontend-1.13.9.tar.gz
Source1:        codeaster_asrun
Source2:        codeaster_profile_local.sh


BuildRequires: python
BuildRequires: python-setuptools
BuildRequires: xterm, nedit
#BuildRequires: gmsh
BuildRequires: codeaster-metis
BuildRequires: grace

Requires(post): info
Requires(preun): info

%description
This is the Code_Aster Frontend package, which provides the program structure for a full Code_Aster installation

%prep
%setup -q

%build
%{__python} setup.py build

%install
%{__python} setup.py install --prefix=%{buildroot}/%{aster_root}
cp %SOURCE1 %{buildroot}%{aster_root}/etc/codeaster/asrun
cp %SOURCE2 %{buildroot}%{aster_root}/etc/codeaster/profile_local.sh

mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
ln -sf %{aster_root}/bin/astk %{buildroot}/%{_bindir}
ln -sf %{aster_root}/bin/as_run %{buildroot}/%{_bindir}

%global outils_dir %{aster_root}/outils
mkdir -p %{buildroot}/%{outils_dir} 
cd %{buildroot}/%{outils_dir}
#ln -sf %{_bindir}/gmsh gmsh
ln -sf %{_bindir}/xmgrace xmgrace
ln -sf %{_bindir}/xmgrace xmgrace
ln -sf %{aster_libs}/metis-%{metis_version}/bin/kmetis kmetis
ln -sf %{aster_libs}/metis-%{metis_version}/bin/kmetis pmetis

%post

%preun

%files
%defattr(-,root,root)
%doc README TODO
%{aster_root}/*
%{_bindir}/astk
%{_bindir}/as_run
%{outils_dir}/xmgrace
%{outils_dir}/gmsh
%{outils_dir}/*metis

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Thu May 12 2016 Stefan Reiterer 1.13.9-1
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
