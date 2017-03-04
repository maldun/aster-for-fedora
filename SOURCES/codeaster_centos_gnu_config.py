# encoding: utf-8

"""
Fichier de configuration WAF pour version séquentielle sur Centos 7:
- Compilateur : GNU
- BLAS        : OpenBLAS
"""
import os
from os import environ as envr
aster_libdir = envr['ASTER_LIBS'] + os.sep 
def configure(self):
    opts = self.options
    self.env.append_value('CFLAGS', ['-std=gnu9x'])
    self.env.prepend_value('PATH',[aster_libdir + '/' + envr['MFRONT'] + '/bin/'])
    self.env.append_value('LDFLAGS', ['-Wl,--no-as-needed','-ldl'])
    

    self.env.append_value('LIBPATH', [
        aster_libdir+ envr['HDF'] + '/lib',
        aster_libdir+ envr['MED'] + '/lib64',
        aster_libdir+ envr['METIS'] + '/lib',
        aster_libdir+ envr['SCOTCH'] + '/lib',
        aster_libdir+envr['MUMPS_STABLE'] + '/lib',
        aster_libdir+ envr['MFRONT'] + '/lib',
        envr['OPENBLAS_DIR'] + '/lib',
        envr['SYSTEM_LIBS'],
        ])

    self.env.append_value('INCLUDES', [
        aster_libdir+ envr['HDF'] + '/include',
        aster_libdir+ envr['MED'] + '/include',
        aster_libdir+ envr['METIS'] + '/include',
        aster_libdir+ envr['SCOTCH'] + '/include',
        #aster_libdir+'/mumps-4.10.0/include_seq',
        #aster_libdir+'/mumps-4.10.0/include',
        aster_libdir+ envr['MFRONT'] + '/include',
        envr['OPENBLAS_DIR'] + '/include',
        envr['SYSTEM_INCLUDE'],
        ])

    opts.maths_libs = 'openblas'
    opts.embed_math = True

    opts.enable_med = True
    opts.hdf5_libs  = 'hdf5 z'
    opts.embed_hdf5 = True
    opts.med_libs  = 'med stdc++'
    opts.embed_med  = True
    
    opts.enable_mumps  = True
    opts.mumps_version = '4.10.0'
    opts.mumps_libs = 'dmumps zmumps smumps cmumps mumps_common pord metis openblas esmumps scotch scotcherr'

    opts.enable_petsc = False

    opts.enable_scotch = True
    opts.embed_scotch  = True

    opts.embed_aster    = True
    opts.embed_fermetur = True

    self.options.enable_mfront = True
