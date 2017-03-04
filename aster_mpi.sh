#########################
# mumps-stable
#########################

source "$(dirname "$0")"/variables.sh
export ASTER_STABLE_FULL=${ASTER_STABLE}.${ASTER_STABLE_SUB}

cd ${DOWNL}
cd aster-full-src-${ASTER_SUB}/SRC

tar -xvf aster-${ASTER_STABLE_FULL}.tgz
mv aster-${ASTER_STABLE_FULL} codeaster-stable-openmpi-${ASTER_STABLE_FULL}
tar cvzf codeaster-stable-openmpi-${ASTER_STABLE_FULL}.tar.gz codeaster-stable-openmpi-${ASTER_STABLE_FULL}
cp codeaster-stable-openmpi-${ASTER_STABLE_FULL}.tar.gz ${SOURCE_DIR}
cd ${SPEC_DIR}

export LD_LIBRARY_PATH=${MPI_DIR}/lib:${ASTER_LIBS}/${MFRONT}/lib:$LD_LIBRARY_PATH
export PATH=${MPI_DIR}/bin:${ASTER_LIBS}/${MFRONT}/bin:$PATH

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-stable-openmpi.spec --define "major_version $ASTER_STABLE" --define "sub_version $ASTER_STABLE_SUB" --define "mfront_version $MFRONT_VER" --define "aster_root $ASTER_BASE" --define "aster_libs $ASTER_LIBS" --define "mpidir $MPI_DIR"
