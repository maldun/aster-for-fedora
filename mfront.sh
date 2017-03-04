#########################
# mumps-stable
#########################

source "$(dirname "$0")"/variables.sh
export MFRONT_FULL=${MFRONT}-${MFRONT_SUB}

copy_pkg ${MFRONT} ${MFRONT_FULL}


QA_RPATHS=$[0x0001|0x0002] QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-mfront.spec  --define "version $MFRONT_VER" --define "aster_libs $ASTER_LIBS" --define "aster_root $ASTER_BASE"
