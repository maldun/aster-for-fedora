#########################
# MED
#########################

source "$(dirname "$0")"/variables.sh

cd ${DOWNL}
cd aster-full-src-${ASTER_SUB}/SRC
export METIS_FULL=${METIS}-${METIS_SUB}

tar -xvf ${METIS_FULL}.tar.gz
mv ${METIS} codeaster-${METIS}
tar cvzf codeaster-${METIS_FULL}.tar.gz codeaster-${METIS}
cp codeaster-${METIS_FULL}.tar.gz ${SOURCE_DIR}
cd ${SPEC_DIR}

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-metis.spec
