#########################
# SCALAPACK
#########################

source "$(dirname "$0")"/variables.sh
export SCOTCH_FULL=${SCOTCH}-${SCOTCH_SUB}

copy_pkg ${SCOTCH} ${SCOTCH_FULL}

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-scotch.spec
