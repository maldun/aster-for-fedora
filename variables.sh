#!/bin/bash

###################
# Variables       #
###################

###################
# aster       #
###################

export ASTER_BASE=/cad/app/aster
export ASTER_VER=12.7
export ASTER_SUB=${ASTER_VER}.0
export ASTER_FULL=aster-full-src-${ASTER_SUB}-1.noarch.tar.gz
export ASTER_ROOT=${ASTER_BASE}/${ASTER_VER}
export EXTLIBS=${ASTER_BASE}/public/

###################
# Install dirs    #
###################

export DOWNL=/tmp/
export BUILD_DIR=${HOME}/rpmbuild
export SOURCE_DIR=${BUILD_DIR}/SOURCES
export SPEC_DIR=${BUILD_DIR}/SPECS

###################
# Packages        #
###################

export HDF=hdf5-1.8.14
export MED=med-3.2.0
export METIS=metis-4.0.3
export METIS_SUB=1
export FRONTEND_VER=1.13.9
export FRONTEND_SUB=1
export SCOTCH=scotch-5.1.11
export SCOTCH_SUB=aster3
export MUMPS_STABLE=mumps-4.10.0
export MUMPS_STABLE_SUB=aster3-2
export MFRONT=mfront-2.0.3
export MFRONT_SUB=1
export ASTER_STABLE=12.7
export ASTER_STABLE_SUB=0
export SCALAPACK=2.0.2
export SCALAPACK_INSTALLER=1.0.2

###################
# functions        #
###################

function copy_pkg () {
   cd ${DOWNL}
   cd aster-full-src-${ASTER_SUB}/SRC

   tar -xvf $2.tar.gz
   mv $1 codeaster-$1
   tar cvzf codeaster-$1.tar.gz codeaster-$1
   cp codeaster-$1.tar.gz ${SOURCE_DIR}
   cd ${SPEC_DIR}
}

function copy_pkg_type () {
   cd ${DOWNL}
   cd aster-full-src-${ASTER_SUB}/SRC

   tar -xvf $2.$4
   mv $1 codeaster-$3-$1
   tar cvzf codeaster-$3-$1.tar.gz codeaster-$3-$1
   cp codeaster-$3-$1.tar.gz ${SOURCE_DIR}
   cd ${SPEC_DIR}
}
