#########################
# SCOTCH
#########################

source "$(dirname "$0")"/variables.sh
export SCOTCH_FULL=${SCOTCH}-${SCOTCH_SUB}

copy_pkg ${SCOTCH} ${SCOTCH_FULL}

QA_RPATHS=$[0x0001|0x0002] QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-scotch.spec --define "version $SCOTCH_VER" --define "aster_libs $ASTER_LIBS" --define "aster_root $ASTER_BASE" --define "openblas_dir $OPENBLAS_DIR"
