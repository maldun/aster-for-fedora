#########################
# mumps-stable
#########################

source "$(dirname "$0")"/variables.sh
export MUMPS_STABLE_FULL=${MUMPS_STABLE}-${MUMPS_STABLE_SUB}

copy_pkg ${MUMPS_STABLE} ${MUMPS_STABLE_FULL}

cd ${SOURCE_DIR}
#mv codeaster-${MUMPS_STABLE} codeaster-stable-${MUMPS_STABLE}
cd ${SPEC_DIR}

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-stable-mumps.spec
