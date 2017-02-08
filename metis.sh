#########################
# MED
#########################

source "$(dirname "$0")"/variables.sh

copy_pkg ${METIS}

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-metis.spec
