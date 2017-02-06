#########################
# HDF 5
#########################

source variables.sh

cd aster-full-src-${ASTER_SUB}/SRC

export HDF=hdf5-1.8.14
tar -xvf ${HDF}.tar.gz
mv ${HDF} codeaster-${HDF}
tar cvzf codeaster-${HDF}.tar.gz codeaster-${HDF}
mv codeaster-${HDF}.tar.gz ${SOURCE_DIR}
#QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-hdf5.spec
