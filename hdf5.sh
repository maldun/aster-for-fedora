#########################
# HDF 5
#########################

source "$(dirname "$0")"/variables.sh

copy_pkg ${HDF} ${HDF}
QA_SKIP_BUILD_ROOT=1 rpmbuild --define "aster_root $ASTER_BASE" -ba codeaster-hdf5.spec
