#!/bin/bash

source variables.sh


################
# Paths        #
################

mkdir -p ${ASTER_BASE}
mkdir -p ${EXTLIBS}

################
# yum packages #
################
#yum -y install glibc-static zlib zlib-static krb5-devel python2-devel libstdc++-static blas lapack flex tk numpy


#########################
# Downloads
#########################

cd /tmp/
#wget http://www.code-aster.org/FICHIERS/aster-full-src-${ASTER_FULL}.noarch.tar.gz

#########################
# Unpack
#########################

tar -xvf ${ASTER_FULL}
cd aster-full-src-${ASTER_SUB}/SRC

