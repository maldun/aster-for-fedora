source "$(dirname "$0")"/variables.sh

mkdir -p ${EXTLIBS}
cd ${EXTLIBS}
git clone https://github.com/xianyi/OpenBLAS.git OpenBLAS
cd OpenBLAS
make NO_AFFINITY=1 USE_OPENMP=1 FC=gfortran
