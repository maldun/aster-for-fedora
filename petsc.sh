#########################
# petsc-openmpi
#########################

source "$(dirname "$0")"/variables.sh
export PETSC_STABLE=petsc-${PETSC_STABLE_VER}
export PETSC_STABLE_MPI=stable-petsc-openmpi-${PETSC_STABLE_VER}
export PATH=${MPI_DIR}/bin:$PATH

cd ${DOWNL}
mv ${PETSC_STABLE}.tar.gz aster-full-src-${ASTER_SUB}/SRC/

copy_pkg_type_mpi ${PETSC_STABLE} ${PETSC_STABLE} ${PETSC_STABLE_MPI} tar.gz


QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-stable-petsc-openmpi.spec --define "version $PETSC_STABLE_VER" --define "scalapack_version $SCALAPACK" --define "aster_libs $ASTER_LIBS" --define "aster_root $ASTER_BASE" --define "openblasdir $OPENBLAS_DIR" --define "mpidir $MPI_DIR"
