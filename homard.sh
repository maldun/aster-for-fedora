#########################
# mumps-stable
#########################

source "$(dirname "$0")"/variables.sh
export HOMARD_FULL=${HOMARD_VER}-${HOMARD_SUB}

copy_pkg_type_mpi homard-${HOMARD_VER} homard-${HOMARD_FULL} homard-${HOMARD_VER} tar.gz


QA_RPATHS=$[0x0001|0x0002] QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-homard.spec --define "major_version $HOMARD_VER" --define "sub_version $HOMARD_SUB" --define "aster_libs $ASTER_LIBS" --define "aster_root $ASTER_BASE" --define "openblas_dir $OPENBLAS_DIR" --define "openblas_inc $OPENBLAS_DIR" --define "scotch_version $SCOTCH_VER" --define "metis_version $METIS_VER"
