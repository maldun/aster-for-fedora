#########################
# aster testing
#########################

source "$(dirname "$0")"/variables.sh
export ASTER_TESTING_FULL=${ASTER_TESTING_VER}.${ASTER_TESTING_SUB}

cd ${DOWNL}
cd aster-full-src-${ASTER_SUB}/SRC

tar -xvf aster-${ASTER_TESTING_FULL}.tgz
mv aster-${ASTER_TESTING_FULL} codeaster-stable-${ASTER_TESTING_FULL}
tar cvzf codeaster-stable-${ASTER_TESTING_FULL}.tar.gz codeaster-stable-${ASTER_TESTING_FULL}
cp codeaster-stable-${ASTER_TESTING_FULL}.tar.gz ${SOURCE_DIR}
cd ${SPEC_DIR}

export LD_LIBRARY_PATH=${ASTER_LIBS}/${MFRONT}/lib:$LD_LIBRARY_PATH
export PATH=${ASTER_LIBS}/${MFRONT}/bin:$PATH

QA_RPATHS=$[0x0001|0x0002] QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-testing.spec --define "major_version $ASTER_TESTING_VER" --define "sub_version $ASTER_TESTING_SUB" --define "mfront_version $MFRONT_VER" --define "aster_root $ASTER_BASE" --define "aster_libs $ASTER_LIBS" 
