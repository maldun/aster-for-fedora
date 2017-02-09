#########################
# mumps-stable
#########################

source "$(dirname "$0")"/variables.sh
export ASTER_STABLE_FULL=${ASTER_STABLE}.${ASTER_STABLE_SUB}

copy_pkg_type ${ASTER_STABLE_FULL} aster-${ASTER_STABLE_FULL} stable tgz


QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-stable.spec
