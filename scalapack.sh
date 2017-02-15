#########################
# SCALAPACK
#########################

source "$(dirname "$0")"/variables.sh
cd ${DOWNL}
tar -xvf scalapack_installer.tgz
tar cvzf codeaster-scalapack-openmpi-${SCALAPACK}.tar.gz scalapack_installer
cp codeaster-scalapack-openmpi-${SCALAPACK}.tar.gz ${SOURCE_DIR}
cd ${SPEC_DIR}

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-scalapack-openmpi.spec
