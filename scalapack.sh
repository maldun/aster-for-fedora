#########################
# SCALAPACK
#########################

source "$(dirname "$0")"/variables.sh

copy_pkg_type scalapack scalapack_installer openmpi-${SCALAPACK}

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-scalapack-openmpi.spec
