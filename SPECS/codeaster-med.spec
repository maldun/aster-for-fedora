%define debug_package %{nil}
%global hdf5_path %{aster_libs}/hdf5-%{hdf5_version}
%global _prefix %{aster_libs}/med-%{version}/


Name:           codeaster-med
Version:        %{version}
Release:        1%{?dist}
Summary:        med lib specific for Code_Aster

License:        LGPLv3+
URL:            http://www.code-aster.org/outils/med/
Source0:        codeaster-med-%{version}.tar.gz


BuildRequires:  codeaster-hdf5
BuildRequires:  gcc-gfortran
BuildRequires:  swig
BuildRequires:  python2-devel
BuildRequires:  zlib-devel

%description
This is the Code_Aster Frontend package, which provides the optimal med library for Code_Aster

%prep
%setup -q

# Fix file not utf8
iconv --from=ISO-8859-1 --to=UTF-8 ChangeLog > ChangeLog.new && \
touch -r ChangeLog ChangeLog.new && \
mv ChangeLog.new ChangeLog

%build
# To remove rpath
autoreconf -ivf

export CFLAGS='-std=gnu9x -fno-stack-protector -O2 -fPIC'
%configure --with-hdf5=%{hdf5_path} --disable-mesgerr --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

# Remove configuration summary file
rm -f %{_prefix}/bin/libmed3.settings

# Remove test-suite files
rm -rf %{buildroot}%{_prefix}/bin/testc
rm -rf %{buildroot}%{_prefix}/bin/usescases
rm -rf %{buildroot}%{_prefix}/bin/unittests
rm -rf %{buildroot}%{_prefix}/bin/testf
rm -rf %{buildroot}%{_prefix}/bin/testpy
rm -rf %{buildroot}%{_prefix}/share

# Fix symlinks to point to correct path
ln -sf %{_bindir}/mdump3 %{buildroot}%{_bindir}/mdump
ln -sf %{_bindir}/xmdump3 %{buildroot}%{_bindir}/xmdump
%post
rm -rf %{_prefix}/share

%preun

%check

%files
%{_prefix}/lib64/*
%{_prefix}/include/*
%{_prefix}/bin/*

%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Feb 8 2017 Stefan Reiterer 3.2.0
- Adaption for centos (personal)
* Thu May 12 2016 Stefan Reiterer 3.0.8
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
