#!/bin/bash

source "$(dirname "$0")"/variables.sh


################
# Paths        #
################

mkdir -p ${ASTER_BASE}
mkdir -p ${EXTLIBS}

#########################
# Downloads
#########################

cd ${DOWNL}
#wget http://www.code-aster.org/FICHIERS/aster-full-src-${ASTER_FULL}
#wget http://code-aster.org/FICHIERS/aster-full-src-12.7.0-1.noarch.tar.gz
#wget http://ftp.tu-chemnitz.de/pub/linux/dag/redhat/el7/en/x86_64/rpmforge/RPMS/rpmforge-release-0.5.3-1.el7.rf.x86_64.rpm
wget http://www.netlib.org/scalapack/scalapack_installer.tgz
wget http://ftp.mcs.anl.gov/pub/petsc/release-snapshots/petsc-3.4.5.tar.gz

################
# yum packages #
################
#yum -y install glibc-static zlib zlib-static krb5-devel python2-devel libstdc++-static blas lapack flex tk numpy
#rpm -Uvh rpmforge-release*rpm

#########################
# Unpack
#########################

#tar -xvf ${ASTER_FULL}
#cd aster-full-src-${ASTER_SUB}/SRC

