#########################
# SCALAPACK
#########################

source "$(dirname "$0")"/variables.sh
cd ${DOWNL}
mkdir codeaster-scalapack-openmpi-${SCALAPACK}
tar -xvf scalapack_installer.tgz
mv scalapack_installer codeaster-scalapack-openmpi-${SCALAPACK}/scalapack_installer_${SCALAPACK_INSTALLER}
tar cvzf codeaster-scalapack-openmpi-${SCALAPACK}.tar.gz codeaster-scalapack-openmpi-${SCALAPACK}
cp codeaster-scalapack-openmpi-${SCALAPACK}.tar.gz ${SOURCE_DIR}
cd ${SPEC_DIR}

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-scalapack-openmpi.spec --define "version $SCALAPACK" --define "aster_libs $ASTER_LIBS" --define "aster_root $ASTER_BASE" --define "openblasdir $OPENBLAS_DIR" --define "mpidir $MPI_DIR" --define "installer_version $SCALAPACK_INSTALLER"
