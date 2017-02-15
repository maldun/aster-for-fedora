#########################
# SCALAPACK
#########################

source "$(dirname "$0")"/variables.sh
cd ${DOWNL}
mkdir codeaster-scalapack-openmpi-${SCALAPACK}
tar -xvf scalapack_installer.tgz
mv scalapack_installer codeaster-scalapack-openmpi-${SCALAPACK}/scalapack_installer-${SCALAPACK_INSTALLER}
tar cvzf codeaster-scalapack-openmpi-${SCALAPACK}.tar.gz codeaster-scalapack-openmpi-${SCALAPACK}
cp codeaster-scalapack-openmpi-${SCALAPACK}.tar.gz ${SOURCE_DIR}
cd ${SPEC_DIR}

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-scalapack-openmpi.spec
