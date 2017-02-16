#########################
# mumps-stable-openmpi
#########################

source "$(dirname "$0")"/variables.sh
export MUMPS_STABLE_FULL=${MUMPS_STABLE}-${MUMPS_STABLE_SUB}
export MUMPS_STABLE_MPI=stable-mumps-openmpi-${MUMPS_STABLE_VER}
export PATH=/cad/app/openmpi/1.10.5/bin:$PATH

copy_pkg_type_mpi ${MUMPS_STABLE} ${MUMPS_STABLE_FULL} ${MUMPS_STABLE_MPI} tar.gz


QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-stable-mumps-openmpi.spec
