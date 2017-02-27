#########################
# HDF 5
#########################

source "$(dirname "$0")"/variables.sh

copy_pkg ${HDF} ${HDF}
QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-hdf5.spec --define "aster_root $ASTER_BASE" --define "aster_libs $ASTER_LIBS" --define "openblas_dir $OPENBLAS_DIR"
