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

###################
# Packages        #
###################

export HDF=hdf5-1.8.14
