#########################
# mumps-stable
#########################

source "$(dirname "$0")"/variables.sh
export ASTER_STABLE_FULL=${ASTER_STABLE}.${ASTER_STABLE_SUB}

cd ${DOWNL}
cd aster-full-src-${ASTER_SUB}/SRC

#tar -xvf aster-${ASTER_STABLE_FULL}.tgz
#mv aster-${ASTER_STABLE_FULL} codeaster-stable-openmpi-${ASTER_STABLE_FULL}
#tar cvzf codeaster-stable-openmpi-${ASTER_STABLE_FULL}.tar.gz codeaster-stable-openmpi-${ASTER_STABLE_FULL}
#cp codeaster-stable-openmpi-${ASTER_STABLE_FULL}.tar.gz ${SOURCE_DIR}
cd ${SPEC_DIR}

export LD_LIBRARY_PATH=/cad/app/openmpi/1.10.5/lib:/cad/app/aster/public/mfront-2.0.3/lib:$LD_LIBRARY_PATH
export PATH=/cad/app/openmpi/1.10.5/bin:/cad/app/aster/public/mfront-2.0.3/bin:$PATH

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-stable-openmpi.spec
