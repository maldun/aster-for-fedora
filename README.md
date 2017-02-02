# aster-for-centos
Packages for Aster

Goal: 

  * Use as much packages from Centos as possible
  * Performance is more important than safety
  * Make The Building Process as Automatic as possible to avoid complicated repackaging cycles
  * Enable as much features of Code_Aster as possible
  * Don't care too much about License Restrictions (not at first)
  * 
 Stages:
 * 1) Make aster-full package obsolete in Centos, i.e. Make enough packages to build new versions of aster with only downloading aster-frontend and aster-src. Make outoconfig scripts
 * 2) make package for aster-sequential version
 * 3) make package for aster-parallel version
 
 ToDo:
 
   * PETSc still has no Hypre and ML support
   * gibi is missing
