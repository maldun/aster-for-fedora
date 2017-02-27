#########################
# mumps-stable
#########################

source "$(dirname "$0")"/variables.sh
export MUMPS_STABLE_FULL=${MUMPS_STABLE}-${MUMPS_STABLE_SUB}

copy_pkg_type ${MUMPS_STABLE} ${MUMPS_STABLE_FULL} stable tar.gz


QA_SKIP_BUILD_ROOT=1 rpmbuild -ba codeaster-stable-mumps.spec --define "version $MUMPS_STABLE_VER" --define "aster_libs $ASTER_LIBS" --define "aster_root $ASTER_BASE" --define "openblas_dir $OPENBLAS_DIR" --define "scotch_version $SCOTCH_VER" --define "metis_version $METIS_VER"
