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
export EXTLIBS=${ASTER_BASE}/lib/

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
export METIS=metis-4.0.3-1

###################
# functions        #
###################

function copy_pkg () {
   cd ${DOWNL}
   cd aster-full-src-${ASTER_SUB}/SRC

   tar -xvf $1.tar.gz
   mv $1 codeaster-$1
   tar cvzf codeaster-$1.tar.gz codeaster-$1
   cp codeaster-$1.tar.gz ${SOURCE_DIR}
   cd ${SPEC_DIR}
}
