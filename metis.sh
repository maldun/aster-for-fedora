#########################
# MED
#########################

source "$(dirname "$0")"/variables.sh
export METIS_FULL=${METIS}-${METIS_SUB}

copy_pkg ${METIS} ${METIS_FULL}

QA_RPATHS=$[0x0001|0x0002] QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-metis.spec --define "version $METIS_VER" --define "aster_libs $ASTER_LIBS" --define "aster_root $ASTER_BASE" --define "openblas_lib $OPENBLAS_LIB"
