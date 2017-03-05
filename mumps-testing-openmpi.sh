#########################
# mumps-testing
#########################

source "$(dirname "$0")"/variables.sh
export MUMPS_TEST_FULL=${MUMPS_TEST}-${MUMPS_TEST_SUB}

copy_pkg_type_testing ${MUMPS_TEST} ${MUMPS_TEST_FULL} testing-${MUMPS_TEST} tar.gz


QA_RPATHS=$[0x0001|0x0002] QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-testing-mumps.spec --define "version $MUMPS_TEST_VER" --define "aster_libs $ASTER_LIBS" --define "aster_root $ASTER_BASE" --define "openblas_lib $OPENBLAS_LIB" --define "openblas_inc $OPENBLAS_INC" --define "scotch_version $SCOTCH_TEST_VER" --define "metis_version $METIS_TEST_VER"
