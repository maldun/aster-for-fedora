#########################
# FRONTEND
#########################

source "$(dirname "$0")"/variables.sh
export FRONTEND_FULL_VER=${FRONTEND_VER}-${FRONTEND_SUB}
export FRONTEND=codeaster-frontend-${FRONTEND_VER}

cd ${DOWNL}
cd aster-full-src-${ASTER_SUB}/SRC

#Rename package
tar -xvf astk-${FRONTEND_FULL_VER}.tar.gz
mv astk-${FRONTEND_VER} ${FRONTEND}
tar cvzf ${FRONTEND}.tar.gz ${FRONTEND}

cp ${FRONTEND}.tar.gz ${SOURCE_DIR}
cd ${SPEC_DIR}

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-frontend.spec
