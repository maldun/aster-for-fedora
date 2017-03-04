#########################
# MED
#########################

source "$(dirname "$0")"/variables.sh
export METIS_TEST_FULL=${METIS_TEST}-${METIS_TEST_SUB}

copy_pkg_type_testing ${METIS_TEST} ${METIS_TEST_FULL} testing-${METIS_TEST} tar.gz

QA_RPATHS=$[0x0001|0x0002] QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-testing-metis.spec --define "version $METIS_TEST_VER" --define "aster_libs $ASTER_LIBS" --define "aster_root $ASTER_BASE" --define "openblas_lib $OPENBLAS_LIB"
