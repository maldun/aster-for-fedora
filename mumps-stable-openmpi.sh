#########################
# mumps-stable-openmpi
#########################

source "$(dirname "$0")"/variables.sh
export MUMPS_STABLE_FULL=${MUMPS_STABLE}-${MUMPS_STABLE_SUB}
export MUMPS_STABLE_MPI=stable-mumps-openmpi-${MUMPS_STABLE_VER}
export PATH=${MPI_DIR}/bin:$PATH

copy_pkg_type_mpi ${MUMPS_STABLE} ${MUMPS_STABLE_FULL} ${MUMPS_STABLE_MPI} tar.gz


QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-stable-mumps-openmpi.spec --define "version $MUMPS_STABLE_VER" --define "scalapack_version $SCALAPACK" --define "aster_root $ASTER_BASE" --define "aster_libs $ASTER_LIBS" --define "openblas_dir $OPENBLAS_DIR" --define "openblas_inc $OPENBLAS_DIR" --define "scotch_version $SCOTCH_VER" --define "metis_version $METIS_VER" --define "mpidir $MPI_DIR" --define "libdir $SYSTEM_LIBS"

