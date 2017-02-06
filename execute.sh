#!/bin/bash

###################
# Variables       #
###################

export ASTER_BASE=/cad/app/aster
export ASTER_VER=12.7
export ASTER_SUB=${ASTER_VER}.0
export ASTER_FULL=aster-full-src-${ASTER_VER}0-1.noarch.tar.gz
export ASTER_ROOT=${ASTER_BASE}/${ASTER_VER}
export EXTLIBS=${ASTER_BASE}/extlibs/

export BUILD_DIR=${HOME}/rpmbuild
export SOURCE_DIR={BUILD_DIR}/SOURCES

################
# Paths        #
################

mkdir -p ${ASTER_BASE}
mkdir -p ${EXTLIBS}

################
# yum packages #
################
#yum -y install glibc-static zlib zlib-static krb5-devel python2-devel libstdc++-static blas lapack flex tk numpy


#########################
# Downloads
#########################

cd /tmp/
#wget http://www.code-aster.org/FICHIERS/aster-full-src-${ASTER_FULL}.noarch.tar.gz

#########################
# Unpack
#########################

tar -xvf aster-full-src-${ASTER_FULL}.noarch.tar.gz
cd aster-full-src-${ASTER_SUB}/SRC

#########################
# HDF 5
#########################

export HDF=hdf5-1.8.14
tar -xvf ${HDF}.tar.gz
mv ${HDF} codeaster-${HDF}
tar cvzf codeaster-${HDF}.tar.gz codeaster-${HDF}
mv codeaster-${HDF}.tar.gz ${SOURCE_DIR}
#QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-hdf5.spec
