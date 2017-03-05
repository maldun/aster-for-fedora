#########################
# mumps-stable
#########################

source "$(dirname "$0")"/variables.sh
export ASTER_TEST_FULL=${ASTER_TESTING_VER}.${ASTER_TESTING_SUB_VER}

copy_pkg_type_testing aster-${ASTER_TEST_FULL} aster-${ASTER_TEST_FULL} testing-openmpi-${ASTER_TEST_FULL} tgz

#cd ${SPEC_DIR}

export LD_LIBRARY_PATH=${MPI_DIR}/lib:${ASTER_LIBS}/${MFRONT}/lib:$LD_LIBRARY_PATH
export PATH=${MPI_DIR}/bin:${ASTER_LIBS}/${MFRONT}/bin:$PATH

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-testing-openmpi.spec --define "major_version $ASTER_TESTING_VER" --define "sub_version $ASTER_TESTING_SUB_VER" --define "mfront_version $MFRONT_VER" --define "aster_root $ASTER_BASE" --define "aster_libs $ASTER_LIBS" --define "mpidir $MPI_DIR"
