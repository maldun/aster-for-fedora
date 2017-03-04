#########################
# MED
#########################

source "$(dirname "$0")"/variables.sh

copy_pkg ${MED} ${MED}

QA_RPATHS=$[0x0001|0x0002] QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-med.spec --define "version $MED_VER" --define "hdf5_version $HDF_VER" --define "aster_libs $ASTER_LIBS" --define "aster_root $ASTER_BASE"
