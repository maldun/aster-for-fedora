#########################
# petsc-openmpi
#########################

source "$(dirname "$0")"/variables.sh
export PETSC_TEST=petsc-${PETSC_TEST_VER}
export PETSC_TEST_MPI=testing-petsc-openmpi-${PETSC_TEST_VER}
export PATH=${MPI_DIR}/bin:$PATH

cd ${DOWNL}
mv ${PETSC_TEST}.tar.gz aster-full-src-${ASTER_TESTING_SUB}/SRC/

copy_pkg_type_testing ${PETSC_TEST} ${PETSC_TEST} ${PETSC_TEST_MPI} tar.gz


QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-testing-petsc-openmpi.spec --define "version $PETSC_TEST_VER" --define "scalapack_version $SCALAPACK" --define "aster_libs $ASTER_LIBS" --define "aster_root $ASTER_BASE" --define "openblasdir $OPENBLAS_DIR" --define "mpidir $MPI_DIR" --define "metis_lib $METIS_TEST" --define "scotch_lib $SCOTCH_TEST" --define "mumps_lib $MUMPS_TEST"
