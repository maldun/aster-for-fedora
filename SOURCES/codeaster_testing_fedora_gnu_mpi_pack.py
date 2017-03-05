# encoding: utf-8

"""
Fichier de configuration WAF pour version parallèle sur Centos 7:
- Compilateur : GNU
- MPI         : système (OpenMPI, Centos 7)
- BLAS        : OpenBLAS
- Scalapack   : Self built V 3.2.0
- PETSc       : 
"""
import os
from os import environ as envr
import os.path as osp
import sys

aster_root=envr['ASTER_BASE'] + os.sep
aster_libdir = envr['ASTER_LIBS'] + os.sep 
mpi_dir = envr['MPI_DIR'] + os.sep 

def configure(self):
    opts = self.options
    
    self.env['FC'] = 'mpif90'
    self.env['CC'] = 'mpicc'
    self.env['CXX'] = 'mpicxx'
    
    self.env.append_unique('LINKFLAGS', ['-Wl,--allow-multiple-definition','-Wl,--no-as-needed','-ldl'])

    self.env['LINKFLAGS_MATH'] = ['-lscalapack',
                                  '-lopenblas',]


    
    self.env.prepend_value('PATH',[aster_libdir + '/' + envr['MFRONT'] + '/bin/'])
    
    self.env.prepend_value('LIBPATH', [
        aster_libdir+ envr['HDF'] + '/lib',
        aster_libdir+ envr['MED'] + '/lib64',
        aster_libdir+ envr['METIS_TEST'] + '/lib',
        aster_libdir+ envr['SCOTCH_TEST'] + '/lib',
        aster_libdir+envr['MUMPS_TEST'] + '-openmpi/lib',
        aster_libdir+ envr['MFRONT'] + '/lib',
        envr['OPENBLAS_DIR'] + '/lib',
        envr['SYSTEM_LIBS'],
        mpi_dir+'lib',        
        aster_libdir + envr['PETSC_STABLE'] + '/lib',
        aster_libdir + envr['SCALAPACK_MPI'] + '/lib',
        #'/opt/Parmetis/parmetis-4.0.3/build/Linux-x86_64/libmetis/',
        ])

    self.env.prepend_value('INCLUDES', [
        mpi_dir+'include',
        #aster_libdir +'/mumps-4.10.0-openmpi/include',
        aster_libdir+ envr['HDF'] + '/include',
        aster_libdir+ envr['MED'] + '/include',
        aster_libdir+ envr['METIS_TEST'] + '/include',
        aster_libdir+ envr['SCOTCH_TEST'] + '/include',
        #aster_libdir+'/mumps-4.10.0/include_seq',
        aster_libdir+envr['MUMPS_TEST'] + '-openmpi/include',
        aster_libdir+ envr['MFRONT'] + '/include',
        envr['OPENBLAS_DIR'] + '/include',
        envr['SYSTEM_INCLUDE'],
        aster_libdir + envr['PETSC_STABLE'] + '/include',
        aster_libdir + envr['SCALAPACK_MPI'] + '/include',
        ])
    
    self.env.append_value('LIB', ('X11',))

    opts.maths_libs = 'openblas'
    opts.embed_math = True

    opts.enable_med = True
    opts.hdf5_libs  = 'hdf5 z'
    opts.embed_hdf5 = True
    opts.med_libs  = 'med stdc++'
    opts.embed_med  = True

    opts.parallel = True

    opts.enable_mumps  = True
    opts.mumps_version = '5.0.2'
    #opts.mumps_libs    = 'dmumps zmumps smumps cmumps mumps_common pord metis scalapack'
    #opts.mumps_libs    = 'dmumps zmumps smumps cmumps mumps_common pord parmetis metis openblas'
    #opts.scotch_libs   = 'ptesmumps ptscotch ptscotcherr'
    opts.mumps_libs = 'dmumps zmumps smumps cmumps mumps_common pord metis scalapack openblas esmumps scotch scotcherr'
    
    opts.enable_petsc = True
    opts.petsc_libs='petsc'
    opts.embed_petsc = True

    self.options.enable_mfront = True
