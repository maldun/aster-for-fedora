# encoding: utf-8

"""
Fichier de configuration WAF pour version parallèle sur Fedora 23:
- Compilateur : GNU
- MPI         : système (OpenMPI, Fedora 23)
- BLAS        : OpenBLAS
- Scalapack   : Self built V 3.2.0
- PETSc       : 
"""

import os.path as osp
import sys

aster_root='/cad/app/aster'
aster_libdir = aster_root + 'public'
mpi_dir = '/cad/app/openmpi/1.10.5/'
#extlibs_intel = osp.expanduser("~/Salome_Meca/Code_Aster/Intel/extlibs/")

# import auto_config
#import aster_full_config

def configure(self):
    #from Options import options as opts
    #auto_config.configure(self)
    #aster_full_config.configure(self)
    opts = self.options
    

    self.env['FC'] = 'mpif90'
    self.env['CC'] = 'mpicc'
    self.env['CXX'] = 'mpicxx'
    
    self.env.append_unique('LINKFLAGS', ['-Wl,--allow-multiple-definition','-Wl,--no-as-needed','-ldl'])

    self.env['LINKFLAGS_MATH'] = ['-lscalapack',
                                  '-lopenblas',]


    
    self.env.prepend_value('PATH',[aster_libdir + 'mfront-2.0.3/bin/'])
    self.options.enable_mfront = True
    self.env.prepend_value('LIBPATH', [
        #'/usr/lib64/python3.4/',
        mpi_dir+'lib',
        aster_libdir + 'mumps-5.0.1-openmpi/lib',
        aster_libdir + 'scalapack-openmpi-2.0.2/lib',
        aster_libdir + 'scotch-5.1.11_esmumps/lib/',
        #extlibs + 'ParMetis-3.2.0',
        aster_libdir + 'petsc-3.4.5/lib',
        aster_libdir + 'hdf5-1.8.10/lib',
        #public + 'zlib-1.2.8',
        aster_libdir + 'med-3.0.8/lib64',
        #'/usr/lib64/',
        aster_libdir + 'mfront-2.0.3/lib',
        aster_libdir + 'metis-4.0.3/lib',
        #'/opt/Parmetis/parmetis-4.0.3/build/Linux-x86_64/libmetis/',
        ])

    self.env.prepend_value('INCLUDES', [
        mpi_dir+'include',
        '/usr/lib64/openmpi/include/hypre/',
        aster_libdir + 'mumps-5.0.1-openmpi/include',
        #extlibs + 'ParMetis-3.2.0',
        #extlibs + 'ParMetis-3.2.0/METISLib',
        #aster_libdir + 'petsc-3.4.5/arch-linux2-c-opt/include',
        aster_libdir + 'petsc-3.4.5/include',
        aster_libdir + 'scalapack-openmpi-2.0.2/include',
        aster_libdir + 'scotch-5.1.11_esmumps/include/',
        aster_libdir + 'hdf5-1.8.10/include',
        aster_libdir + 'med-3.0.8/include',
        aster_libdir + 'metis-4.0.3/include',
        #'/opt/Parmetis/parmetis-4.0.3/build/Linux-x86_64/metis/include/',
        aster_libdir + 'mfront-2.0.3/include',
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
    opts.mumps_version = '5.0.1'
    #opts.mumps_libs    = 'dmumps zmumps smumps cmumps mumps_common pord metis scalapack'
    #opts.mumps_libs    = 'dmumps zmumps smumps cmumps mumps_common pord parmetis metis openblas'
    #opts.scotch_libs   = 'ptesmumps ptscotch ptscotcherr'
    opts.mumps_libs = 'dmumps zmumps smumps cmumps mumps_common pord metis scalapack openblas esmumps scotch scotcherr'
    
    opts.enable_petsc = True
    opts.petsc_libs='petsc'
    opts.embed_petsc = True

    # currently mfront makes trouble
    opts.enable_mfront = True
