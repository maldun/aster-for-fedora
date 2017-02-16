#########################
# petsc-openmpi
#########################

source "$(dirname "$0")"/variables.sh
export PETSC_STABLE=petsc-${PETSC_STABLE_VER}
export MUMPS_STABLE_MPI=stable-petsc-openmpi-${PETSC_STABLE_VER}
export PATH=/cad/app/openmpi/1.10.5/bin:$PATH

cd ${DOWNL}
mv ${PETSC_STABLE}.tar.gz aster-full-src-${ASTER_SUB}/SRC/

copy_pkg_type_mpi ${PETSC_STABLE} ${PETSC_STABLE} ${PETSC_STABLE_MPI} tar.gz


QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-stable-petsc-openmpi.spec
