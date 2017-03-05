#########################
# aster testing
#########################

source "$(dirname "$0")"/variables.sh
export ASTER_TESTING_FULL=${ASTER_TESTING_VER}.${ASTER_TESTING_SUB_VER}

#copy_pkg_type_testing aster-${ASTER_TESTING_FULL} aster-${ASTER_TESTING_FULL} testing-${ASTER_TESTING_VER} tgz
cd ${SPEC_DIR}
export LD_LIBRARY_PATH=${ASTER_LIBS}/${MFRONT}/lib:$LD_LIBRARY_PATH
export PATH=${ASTER_LIBS}/${MFRONT}/bin:$PATH

QA_RPATHS=$[0x0001|0x0002] QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-testing.spec --define "major_version $ASTER_TESTING_VER" --define "sub_version $ASTER_TESTING_SUB_VER" --define "mfront_version $MFRONT_VER" --define "aster_root $ASTER_BASE" --define "aster_libs $ASTER_LIBS" 
