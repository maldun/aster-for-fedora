#########################
# SCOTCH
#########################

source "$(dirname "$0")"/variables.sh
export SCOTCH_TEST_FULL=${SCOTCH_TEST}-${SCOTCH_TEST_SUB}

copy_pkg_type_testing ${SCOTCH_TEST} ${SCOTCH_TEST_FULL} testing-${SCOTCH_TEST} tar.gz

QA_RPATHS=$[0x0001|0x0002] QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-testing-scotch.spec --define "version $SCOTCH_TEST_VER" --define "aster_libs $ASTER_LIBS" --define "aster_root $ASTER_BASE" --define "openblas_dir $OPENBLAS_DIR"
