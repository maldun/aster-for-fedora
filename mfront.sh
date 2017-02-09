#########################
# mumps-stable
#########################

source "$(dirname "$0")"/variables.sh
export MFRONT_FULL=${MFRONT}-${MFRONT_SUB}

copy_pkg ${MFRONT} ${MFRONT_FULL} stable


QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-mfront.spec
