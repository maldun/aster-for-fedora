%global aster_root /opt/Code_Aster/aster_root
%define debug_package %{nil}


Name:           codeaster-frontend
Version:        1.13.7
Release:        1%{?dist}
Summary:        The Code_Aster-Frontend Package/Structure

License:        GPLv2
URL:            https://bitbucket.org/code_aster/codeaster-frontend
Source0:        https://bitbucket.org/code_aster/codeaster-frontend/codeaster-frontend-1.13.7.tar.gz


BuildRequires: python
BuildRequires: bash
BuildRequires: python-setuptools

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

%post

%preun

%files
# %defattr(-,root,root)
%doc README TODO
%{aster_root}/*

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Thu May 12 2016 Stefan Reiterer 1.13.7-1
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
