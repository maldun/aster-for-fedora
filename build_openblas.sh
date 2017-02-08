source "$(dirname "$0")"/variables.sh

mkdir -p ${EXTLIBS}
cd ${DOWNL}
git clone https://github.com/xianyi/OpenBLAS.git OpenBLAS
cd OpenBLAS
make NO_AFFINITY=1 USE_OPENMP=1 FC=gfortran
make PREFIX=${EXTLIBS}/OpenBLAS install
echo /opt/OpenBLAS/lib | sudo tee -a /etc/ld.so.conf.d/openblas.conf
sudo ldconfig

