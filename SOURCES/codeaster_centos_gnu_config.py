# encoding: utf-8

"""
Fichier de configuration WAF pour version séquentielle sur Fedora 23:
- Compilateur : GNU
- BLAS        : OpenBLAS
"""
aster_libdir = '/cad/app/aster/public'
def configure(self):
    opts = self.options
    self.env.append_value('CFLAGS', ['-std=gnu9x'])
    self.env.prepend_value('PATH',[aster_libdir + '/mfront-2.0.3/bin/'])

    self.env.append_value('LIBPATH', [
        aster_libdir+'/hdf5-1.8.14/lib',
        aster_libdir+'/med-3.2.0/lib64',
        aster_libdir+'/metis-4.0.3/lib',
        aster_libdir+'/scotch-5.1.11/lib',
        aster_libdir+'/mumps-4.10.0/lib',
        aster_libdir+'/mfront-2.0.3/lib',
        aster_libdir+'/OpenBLAS/lib',
        '/usr/lib64',
        #public + 'metis-4.0.3/lib/',
        ])

    self.env.append_value('INCLUDES', [
        aster_libdir+'/hdf5-1.8.14/include',
        aster_libdir+'/med-3.2.0/include',
        aster_libdir+'/metis-4.0.3/include',
        aster_libdir+'/scotch-5.1.11/include',
        aster_libdir+'/mumps-4.10.0/include_seq',
        aster_libdir+'/mumps-4.10.0/include',
        aster_libdir+'/mfront-2.0.3/include',
        aster_libdir+'/OpenBLAS/include',
        '/usr/include',
        #'/home/maldun/Salome_Meca/devel/aster_root/public/metis-4.0.3/include/',
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
