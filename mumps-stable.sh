#########################
# mumps-stable
#########################

source "$(dirname "$0")"/variables.sh
export MUMPS_STABLE_FULL=${MUMPS_STABLE}-${MUMPS_STABLE_SUB}

copy_pkg stable-${MUMPS_STABLE} ${MUMPS_STABLE_FULL}

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-mumps-stable.spec
