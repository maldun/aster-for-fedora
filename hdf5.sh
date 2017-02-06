#########################
# HDF 5
#########################

source variables.sh

cd aster-full-src-${ASTER_SUB}/SRC

tar -xvf ${HDF}.tar.gz
mv ${HDF} codeaster-${HDF}
tar cvzf codeaster-${HDF}.tar.gz codeaster-${HDF}
mv codeaster-${HDF}.tar.gz ${SOURCE_DIR}
#QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-hdf5.spec
