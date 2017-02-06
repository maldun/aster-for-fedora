%global version 1.8.14
%global aster_root /cad/app/aster
%global aster_libs codeaster
%define debug_package %{nil}


Name:           codeaster-hdf5
Version:        %{version}
Release:        1%{?dist}
Summary:        hdf5 lib specific for Code_Aster

License:        BSD
URL:            http://code-aster.org/
Source0:        codeaster-hdf5-1.8.14.tar.gz


BuildRequires: krb5-devel, openssl-devel, zlib-devel, gcc-gfortran, time
BuildRequires: openblas-openmp
# For patches/rpath
BuildRequires: automake
BuildRequires: libtool
# Needed for mpi tests
BuildRequires: openssh-clients

%description
This is the Code_Aster hdf5 package, which provides the optimal hdf5 lib for code_aster

%prep
%setup -q

%build
#Do out of tree builds
%global _prefix %{_libdir}/%{aster_libs}/hdf5-%{version}/
%global _configure ./configure
#Common configure options
%global configure_opts \\\
   --disable-silent-rules \\\
   --enable-fortran \\\
   --enable-fortran2003 \\\
   --enable-hl \\\
   --enable-shared \\\
%{nil}
# --enable-cxx and --enable-parallel flags are incompatible
# --with-mpe=DIR          Use MPE instrumentation [default=no]
# --enable-cxx/fortran/parallel and --enable-threadsafe flags are incompatible
mkdir -p %{buildroot}%{_prefix}

#Serial build
export CFLAGS='-std=gnu9x -fno-stack-protector -O2 -fPIC'
export CC=gcc
export CXX=g++
export F9X=gfortran
export LDFLAGS='-L/usr/lib64/ -lopenblas'
%{_configure} %{configure_opts} --enable-cxx --prefix=%{_prefix}
make

%install
make install DESTDIR=%{buildroot}
rm $RPM_BUILD_ROOT/%{_prefix}/lib/*.la
%post

%preun

%files
%{_prefix}/bin/gif2h5
%{_prefix}/bin/h52gif
%{_prefix}/bin/h5copy
%{_prefix}/bin/h5debug
%{_prefix}/bin/h5diff
%{_prefix}/bin/h5dump
%{_prefix}/bin/h5import
%{_prefix}/bin/h5jam
%{_prefix}/bin/h5ls
%{_prefix}/bin/h5mkgrp
%{_prefix}/bin/h5perf_serial
%{_prefix}/bin/h5repack
%{_prefix}/bin/h5repart
%{_prefix}/bin/h5stat
%{_prefix}/bin/h5unjam
%{_prefix}/lib/*.so.7*
%{_prefix}/lib/*.so
%{_prefix}/lib/*.a
%{_prefix}/lib/libhdf5.settings
%{_prefix}/include/*.h
%{_prefix}/include/*.mod
%{_prefix}/bin/h5c++
%{_prefix}/bin/h5cc
%{_prefix}/bin/h5fc
%{_prefix}/bin/h5redeploy
%{_prefix}/share/hdf5_examples/*


%clean
#rm -rf $RPM_BUILD_ROOT

%changelog
* Thu May 12 2016 Stefan Reiterer 1.13.7-1
- Initial version of the package
- Build with QA_SKIP_BUILD_ROOT=1 rpmbuild -ba name.spec
