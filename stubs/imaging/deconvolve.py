#
# stub function definition file for docstring parsing
#

def deconvolve(imagename, model='', psf=[''], alg='clark', niter=10, gain=0.1, threshold=0.0, mask='', scales=[0, 3, 10], sigma=0.0, targetflux=1.0, prior=''):
    r"""
Image based deconvolver

Parameters
   - **imagename** (string) -  [1]_
   - **model** (string='') -  [2]_
   - **psf** (stringArray=['']) -  [3]_
   - **alg** (string='clark') -  [4]_

      .. raw:: html

         <details><summary><i> alg = multiscale </i></summary>

      - **scales** (intArray=[0, 3, 10]) -  [9]_

      .. raw:: html

         </details>

      .. raw:: html

         <details><summary><i> alg = mem </i></summary>

      - **sigma** (double=0.0) -  [10]_
      - **targetflux** (double=1.0) -  [11]_
      - **prior** (string='') -  [12]_

      .. raw:: html

         </details>
   - **niter** (int=10) -  [5]_
   - **gain** (double=0.1) -  [6]_
   - **threshold** (double=0.0) -  [7]_
   - **mask** (string='') -  [8]_


Description
   **deconvolve** performs minor cycle deconvolution directly on a
   dirty image. No MS is required.

   .. warning:: **ALERT:** **deconvolve** is currently defunct. We plan to
      replace the task with **tclean**code. For the moment use
      **tclean** (although **tclean** requires an MS at this stage),
      or please use**deconvolve** in an older version of CASA
      (v4.7.2 or earlier).

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *imagename*
      

   The input dirty image that will be deconvolved.

   .. rubric:: m *odel*
      

   The output cleaned image containing a deconvolved point model.

   .. rubric:: *psf*
      

   Can be either be an image (e.g., a psf that **tclean** has
   calculated), or a list of values that define a Gaussian,
   e.g.,*psf=['3arcsec', '2.5arcsec', '10deg']* defines a Gaussian
   with '3arcsec' as the major axis, '2.5arcsec' as the minor axis,
   and a position angle of 10 degrees.

   .. rubric:: *alg*
      

   The clean algorithm to use by **deconvolve**. Several algorithms
   are available to deconvolve an image with a known psf (dirty
   beam), or a Gaussian beam. The algorithms are 'clark' (default)
   and 'hogbom' clean, 'multiscale' clean and a Maximum Entropy 'mem'
   clean. Details on the algorithms are given in the `Synthesis
   Imaging <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging>`__
   chapter in the page describing`Deconvolution
   Algorithms. <https://casa.nrao.edu/casadocs-devel/stable/imaging/synthesis-imaging/deconvolution-algorithms>`__

   .. rubric:: *alg='multiscale'* expandable parameters
      

   .. rubric:: *scales*
      

   A list of scales in units of pixels (see the **deconvolve**
   examples tab).

   .. rubric:: *alg='mem'* expandable parameters
      

   .. rubric:: *sigma*
      

   This parameter allows the user to input an expected noise value,
   which will allow for a faster convergence.

   .. rubric:: *targetflux*
      

   The estimated total flux in the image.

   .. rubric:: *prior*
      

   A starting model to be used by **deconvolve**. If no*prior* is
   provided, a flat image will be used.

   

   .. rubric:: *niter*
      

   The number of iterations to perform on the image. Default: 10

   .. rubric:: *gain*
      

   Sets the CLEAN gain parameter. Default: 0.1

   .. rubric:: *threshold*
      

   Sets the lower level below which sources will not be deconvolved.

   .. rubric:: *mask*
      

   The image mask to limit the region of deconvolution.




Details
   Explanation of each parameter

.. [1] 
   **imagename** (string)
      | Input image to deconvolve
.. [2] 
   **model** (string='')
      | Output image containing deconvolved point model
.. [3] 
   **psf** (stringArray=[''])
      | Point spread function (dirty beam)
.. [4] 
   **alg** (string='clark')
      | Algorithm to use (clark, hogbom, multiscale, mem)
.. [5] 
   **niter** (int=10)
      | number of iteration in deconvolution process
.. [6] 
   **gain** (double=0.1)
      | CLEAN gain parameter
.. [7] 
   **threshold** (double=0.0)
      | level below which sources will not be deconvolved
.. [8] 
   **mask** (string='')
      | image mask to limit region of deconvolution
.. [9] 
   **scales** (intArray=[0, 3, 10])
      | scale sizes (pixels) to deconvolve
.. [10] 
   **sigma** (double=0.0)
      | mem parameter: Expected noise in image
.. [11] 
   **targetflux** (double=1.0)
      | mem parameter: Estimated total flux in image
.. [12] 
   **prior** (string='')
      | mem parameter: prior image for mem search

    """
    pass
