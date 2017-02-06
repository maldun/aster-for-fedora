#!/bin/bash

###################
# Variables       #
###################

export ASTER_BASE=/cad/app/aster
export ASTER_VER=12.7
export ASTER_SUB=${ASTER_VER}.0
export ASTER_FULL=aster-full-src-${ASTER_SUB}-1.noarch.tar.gz
export ASTER_ROOT=${ASTER_BASE}/${ASTER_VER}
export EXTLIBS=${ASTER_BASE}/extlibs/

export HDF=hdf5-1.8.14

################
# Paths        #
################

mkdir -p ${ASTER_BASE}
mkdir -p ${EXTLIBS}

################
# yum packages #
################
yum -y install glibc-static zlib zlib-static krb5-devel python2-devel libstdc++-static blas lapack flex tk numpy


#########################
# Downloads
#########################

cd /tmp/
#wget http://www.code-aster.org/FICHIERS/aster-full-src-${ASTER_FULL}.noarch.tar.gz

#########################
# Unpack
#########################

tar -xvf ${ASTER_FULL}
cd aster-full-src-${ASTER_SUB}/SRC
tar -xvf ${HDF}.tar.gz
mv ${HDF} codeaster-${HDF}
tar cvzf codeaster-${HDF}.tar.gz codeaster-${HDF}
#QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-hdf5.spec
