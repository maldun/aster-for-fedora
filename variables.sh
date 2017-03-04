#!/bin/bash

###################
# Variables       #
###################

###################
# aster           #
###################

export ASTER_BASE=/opt/aster
export ASTER_VER=12.7
export ASTER_SUB=${ASTER_VER}.0
export ASTER_FULL=aster-full-src-${ASTER_SUB}-1.noarch.tar.gz
export ASTER_ROOT=${ASTER_BASE}/${ASTER_VER}
export ASTER_LIBS=${ASTER_BASE}/public

###################
# aster-testing   #
###################

export ASTER_TESTING_VER=13.3
export ASTER_TESTING_SUB=${ASTER_TESTING_VER}.0
export ASTER_TESTING_FULL=aster-full-src-${ASTER_TESTING_SUB}-1.noarch.tar.gz

###################
# External libs   #
###################

export SYSTEM_LIBS=/usr/lib64
export SYSTEM_INCLUDE=/usr/include
export MPI_DIR=${SYSTEM_LIBS}/openmpi/
export EXTLIBS=${ASTER_BASE}/public/
export OPENBLAS_DIR=/usr/lib64
export OPENBLAS_LIB=${OPENBLAS_DIR}
export OPENBLAS_INC=${SYSTEM_INCLUDE}

###################
# Install dirs    #
###################

export DOWNL=${HOME}/Downloads
export BUILD_DIR=${HOME}/rpmbuild
export SOURCE_DIR=${BUILD_DIR}/SOURCES
export SPEC_DIR=${BUILD_DIR}/SPECS

###################
# Versions        #
###################

export HDF_VER=1.8.14
export MED_VER=3.2.0
export METIS_VER=4.0.3
export METIS_SUB=1
export FRONTEND_VER=1.13.9
export FRONTEND_SUB=1
export SCOTCH_VER=5.1.11
export SCOTCH_SUB=aster3
export MUMPS_STABLE_VER=4.10.0
export MUMPS_STABLE_SUB=aster3-2
export MFRONT_VER=2.0.3
export MFRONT_SUB=1
export ASTER_STABLE=12.7
export ASTER_STABLE_SUB=0
export HOMARD_VER=11.7
export HOMARD_SUB=1
export SCALAPACK=2.0.2
export SCALAPACK_INSTALLER=1.0.2
export PETSC_STABLE_VER=3.4.5

export METIS_TEST_VER=5.1.0
export METIS_TEST_SUB=aster1
export SCOTCH_TEST_VER=6.0.4
export SCOTCH_TEST_SUB=aster5
export MUMPS_TEST_VER=5.0.2

###################
# Packages        #
###################

export HDF=hdf5-${HDF_VER}
export MED=med-${MED_VER}
export METIS=metis-${METIS_VER}
export METIS_TEST=metis-${METIS_TEST_VER}
export SCOTCH=scotch-${SCOTCH_VER}
export SCOTCH_TEST=scotch-${SCOTCH_TEST_VER}
export MUMPS_STABLE=mumps-${MUMPS_STABLE_VER}
export MFRONT=mfront-${MFRONT_VER}
export PETSC_STABLE=petsc-${PETSC_STABLE_VER}
export SCALAPACK_MPI=scalapack-openmpi-${SCALAPACK}

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

function copy_pkg_type_mpi () {
   cd ${DOWNL}
   cd aster-full-src-${ASTER_SUB}/SRC

   tar -xvf $2.$4
   mv $1 codeaster-$3
   tar cvzf codeaster-$3.tar.gz codeaster-$3
   cp codeaster-$3.tar.gz ${SOURCE_DIR}
   cd ${SPEC_DIR}
}

function copy_pkg_type_testing () {
   cd ${DOWNL}
   cd aster-full-src-${ASTER_TESTING_SUB}/SRC

   tar -xvf $2.$4
   mv $1 codeaster-$3
   tar cvzf codeaster-$3.tar.gz codeaster-$3
   cp codeaster-$3.tar.gz ${SOURCE_DIR}
   cd ${SPEC_DIR}
}

