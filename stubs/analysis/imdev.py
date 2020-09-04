#
# stub function definition file for docstring parsing
#

def imdev(imagename, outfile='', region='', box='', chans='', stokes='', mask='', overwrite=False, stretch=False, grid=[1, 1], anchor='ref', xlength='1pix', ylength='1pix', interp='cubic', stattype='sigma', statalg='classic', zscore=-1, maxiter=-1):
    r"""
Create an image that can represent the statistical deviations of the input image.

Parameters
   - **imagename** (string) - Input image name [1]_
   - **outfile** (string='') - Output image file name. If left blank (the default), no image is written but a new image tool referencing the collapsed image is returned. [2]_
   - **region** ({string, record}='') - Region selection. Default is to use the full image. [3]_
   - **box** (string='') - Rectangular region(s) to select in direction plane. Default is to use the entire direction plane. [4]_
   - **chans** (string='') - Channels to use. Default is to use all channels. [5]_
   - **stokes** (string='') - Stokes planes to use. Default is to use all Stokes planes. [6]_
   - **mask** (string='') - Mask to use. Default setting is none.  [7]_
   - **overwrite** (bool=False) - Overwrite (unprompted) pre-existing output file? Ignored if "outfile" is left blank.  [8]_
   - **grid** (intArray=[1, 1]) - x,y grid spacing. Array of exactly two positive integers. [10]_
   - **anchor** ({string, intArray}='ref') - x,y anchor pixel location. Either "ref" to use the image reference pixel, or an array of exactly two integers. [11]_
   - **xlength** ({string, int}='1pix') - Either x coordinate length of box, or diameter of circle. Circle is used if ylength is empty string. [12]_
   - **ylength** ({string, int}='1pix') - y coordinate length of box. Use a circle if ylength is empty string. [13]_
   - **interp** (string='cubic') - Interpolation algorithm to use. One of "nearest", "linear", "cubic", or "lanczos". Minimum match supported. [14]_
   - **stattype** (string='sigma') - Statistic to compute. See full description for supported statistics. [15]_
   - **statalg** (string='classic') - Statistics computation algorithm to use. Supported values are "chauvenet" and "classic", Minimum match is supported. [16]_

      .. raw:: html

         <details><summary><i> statalg = chauvenet </i></summary>

      - **zscore** (double=-1) - For chauvenet, this is the target maximum number of standard deviations data may have to be included. If negative, use Chauvenet"s criterion. Ignored if algorithm is not "chauvenet". [17]_
      - **maxiter** (int=-1) - For chauvenet, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, iterate until the zscore criterion is met. Ignored if algortihm is not "chauvenet". [18]_

      .. raw:: html

         </details>


Description
   This application creates an image that reflects the statistics
   around specified grid points of the input image. The output image
   has the same dimensions and coordinate system as the (selected
   region in the) input image. The *grid* parameter describes how
   many pixels apart the grid pixels are from one another and the
   statistics are computed around each grid pixel. Grid pixels are
   limited to the direction plane only (typically RA and dec);
   independent statistics are computed for each direction plane
   (i.e., at each frequency/stokes pixel should the input image
   happen to have such additional axes).

   Using the *xlength* and *ylength* parameters, one may specify
   either a rectangular or circular region around each grid point
   that defines which surrounding pixels are used in the statistic
   computation for individual grid points. If the *ylength* parameter
   is the empty string, then a circle of diameter provided by
   *xlength* centered on the grid point is used. If *ylength* is not
   empty, then a rectangular box of dimensions *xlength* x *ylength*
   centered on the grid pixel is used. These two parameters may be
   specified in pixels, using either numerical values or valid
   quantities with "pix" as the unit (e.g., "4pix"). Otherwise, they
   must be specified as valid angular quantities, with recognized
   units (e.g., "4arcsec"). As with other region selections in CASA,
   full pixels are included in the computation even if the specified
   region includes only a fraction of that pixel.

   .. warning:: **WARNING**: Beware of machine precision issues because you may
      get a smaller number of pixels included in a region than you
      expect if you specify, e.g., an integer number of pixels. In
      such cases, you probably want to specify that number plus a
      small epsilon value (e.g., "2.0001pix" rather than "2pix") to
      mitigate machine precision issues when computing region
      extents.

   The output image is formed by putting the statistics calculated at
   each grid point at the corresponding grid point in the output
   image. Interpolation of these output values is then used to
   compute values at non-grid-point pixels. The user may specify
   which interpolation algorithm to use for this computation using
   the *interp* parameter. The input image pixel mask is copied to
   the output image. If interpolation is performed, output pixels are
   masked where the interpolation fails.

   .. rubric:: ANCHORING THE GRID
      

   The user may choose at which pixel to *anchor* the grid. For
   example, if one specifies *grid=[4,4]* and *anchor=[0,0]*, grid
   points will be located at pixels [0,0], [0,4], [0,8] ... [4,0],
   [4,4], etc. This is exactly the same grid that would be produced
   if the user specified *anchor=[4,4]* or *anchor=[20,44]*. The
   value "ref", which is the default, indicates that the reference
   pixel of the input image should be used to anchor the grid. The x
   and y values of this pixel will be rounded to the nearest integer
   if necessary.

   .. rubric:: SUPPORTED STATISTICS AND STATISTICS ALGORITHMS
      

   One may specify which statistic should be represented using the
   *stattype* parameter. The following values are recognized (minimum
   match supported):

   -  'iqr' - inner quartile range (q3 - q1)
   -  'max' - maximum
   -  'mean' - mean
   -  'medabsdevmed' or 'madm' - median absolute deviation from the
      median
   -  'median' - median
   -  'min' - minimum
   -  'npts' - number of points
   -  'q1' - first quartile
   -  'q3' - third quartile
   -  'rms' - rms
   -  'sigma' or 'std' - standard deviation
   -  'sumsq' - sum of squares
   -  'sum' - sum
   -  'var' - variance
   -  'xmadm' - median absolute deviation from the median converted
      to an RMS-equivalent value. Result is MADM multipied by x,
      where x is the reciprocal of :math:`Phi^{-1}*(3/4)` and
      :math:`Phi^{-1}` is the reciprocal of the quantile function.
      Numerically, x = 1.482602218505602. See
      `here <https://en.wikipedia.org/wiki/Median_absolute_deviation#Relation_to_standard_deviation>`__
      for an example.

   Using the *statalg* parameter, one may also select whether to use
   the default Classical ("classic", which uses the "framework"
   statistics method) or Chauvenet/ZScore ("chauvenet") statistics
   algorithm to compute the desired statistic (see the help for
   **ia.statistics** or **imstat** for a full description of these
   algorithms; see `this
   page <https://casa.nrao.edu/casadocs-devel/stable/imaging/image-analysis/mathematical-operation-on-images-and-image-statistics>`__
   for further information on Operations and Statistics on CASA
   images).

   

   .. rubric:: Parameter descriptions
      

   .. rubric:: *imagename*
      

   The name of the input image that **imdev** will use.

   .. rubric:: *outfile*
      

   Output image file name. If left blank (the default), no image is
   written but a new image tool referencing the collapsed image is
   returned.

   .. rubric:: *region*
      

   Region selection. Default is to use the full image.

   .. rubric:: *box*
      

   Rectangular region(s) to select in direction plane. Default is to
   use the entire direction plane.

   .. rubric:: *chans*
      

   Channels from the input image to use. Default is to use all
   channels.

   .. rubric:: *stokes*
      

   Stokes planes to use. Default is to use all Stokes planes.

   .. rubric:: *mask*
      

   Mask to use. Default setting is none.

   .. rubric:: *mask* expandable parameters
      

   .. rubric:: *stretch*
      

   Stretch the mask if necessary and possible. Default value is
   False.

   

   .. rubric:: *overwrite*
      

   Overwrite (unprompted) pre-existing output file. Ignored if
   *outfile* is left blank.

   .. rubric:: *grid*
      

   x,y grid spacing. Array of exactly two positive integers.

   .. rubric:: *anchor*
      

   x,y anchor pixel location. Either "ref" to use the image reference
   pixel, or an array of exactly two integers.

   .. rubric:: *xlength*
      

   Either x coordinate length of box, or diameter of circle. Circle
   is used if *ylength* is empty string.

   .. rubric:: *ylength*
      

   y coordinate length of box. Use a circle if *ylength* is empty
   string.

   .. rubric:: *interp*
      

   Interpolation algorithm to use. One of "nearest", "linear",
   "cubic", or "lanczos". Minimum match supported.

   .. rubric:: *stattype*
      

   Statistic to compute. Accepted values discussed in the section
   above.

   .. rubric:: *statalg*
      

   Statistics computation algorithm to use. Supported values are
   "chauvenet" and "classic", Minimum match is supported.

   .. rubric:: *statalg='chauvenet'* expandable parameters
      

   .. rubric:: *zscore*
      

   This is the target maximum number of standard deviations data may
   have to be included. If negative, use Chauvenet"s criterion.

   .. rubric:: *maxiter*
      

   This is the maximum number of iterations to attempt. Iterating
   will stop when either this limit is reached, or the *zscore*
   criterion is met. If negative, iterate until the *zscore*
   criterion is met.




Details
   Explanation of each parameter

.. [1] 
   **imagename** (string)
      | Input image name
.. [2] 
   **outfile** (string='')
      | Output image file name. If left blank (the default), no image is written but a new image tool referencing the collapsed image is returned.
.. [3] 
   **region** ({string, record}='')
      | Region selection. Default is to use the full image.
.. [4] 
   **box** (string='')
      | Rectangular region(s) to select in direction plane. Default is to use the entire direction plane.
.. [5] 
   **chans** (string='')
      | Channels to use. Default is to use all channels.
.. [6] 
   **stokes** (string='')
      | Stokes planes to use. Default is to use all Stokes planes.
.. [7] 
   **mask** (string='')
      | Mask to use. Default setting is none.
.. [8] 
   **overwrite** (bool=False)
      | Overwrite (unprompted) pre-existing output file? Ignored if "outfile" is left blank.
.. [9] 
   **stretch** (bool=False)
      | Stretch the mask if necessary and possible? Default value is False.
.. [10] 
   **grid** (intArray=[1, 1])
      | x,y grid spacing. Array of exactly two positive integers.
.. [11] 
   **anchor** ({string, intArray}='ref')
      | x,y anchor pixel location. Either "ref" to use the image reference pixel, or an array of exactly two integers.
.. [12] 
   **xlength** ({string, int}='1pix')
      | Either x coordinate length of box, or diameter of circle. Circle is used if ylength is empty string.
.. [13] 
   **ylength** ({string, int}='1pix')
      | y coordinate length of box. Use a circle if ylength is empty string.
.. [14] 
   **interp** (string='cubic')
      | Interpolation algorithm to use. One of "nearest", "linear", "cubic", or "lanczos". Minimum match supported.
.. [15] 
   **stattype** (string='sigma')
      | Statistic to compute. See full description for supported statistics.
.. [16] 
   **statalg** (string='classic')
      | Statistics computation algorithm to use. Supported values are "chauvenet" and "classic", Minimum match is supported.
.. [17] 
   **zscore** (double=-1)
      | For chauvenet, this is the target maximum number of standard deviations data may have to be included. If negative, use Chauvenet"s criterion. Ignored if algorithm is not "chauvenet".
.. [18] 
   **maxiter** (int=-1)
      | For chauvenet, this is the maximum number of iterations to attempt. Iterating will stop when either this limit is reached, or the zscore criterion is met. If negative, iterate until the zscore criterion is met. Ignored if algortihm is not "chauvenet".

    """
    pass
