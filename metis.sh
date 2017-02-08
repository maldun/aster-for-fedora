#########################
# MED
#########################

source "$(dirname "$0")"/variables.sh
export METIS_FULL=${METIS}-${METIS_SUB}

copy_pkg ${METIS} ${METIS_FULL}

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-metis.spec
