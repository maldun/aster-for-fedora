#########################
# FRONTEND
#########################

source "$(dirname "$0")"/variables.sh
export FRONTEND_FULL_VER=${FRONTEND_VER}-${FRONTEND_SUB}

cd ${DOWNL}
cd aster-full-src-${ASTER_SUB}/SRC

#Rename package
tar -xvf astk-${FRONTEND_FULL_VER}.tar.gz
mv astk-${FRONTEND_VER} codeaster-frontend-${FRONTEND_VER}
tar cvzf codeaster-${FRONTEND_VER}.tar.gz codeaster-frontend-${FRONTEND_VER}

cp codeaster-${FRONTEND_VER}.tar.gz ${SOURCE_DIR}
cd ${SPEC_DIR}

QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-frontend.spec
