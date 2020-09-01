

# VLA Weather Information 

About plotweather

Weather data for the VLA can be displayed with the task **plotweather**. This task will also calculate opacities based on the weather data taken at the time of the observation, or from a seasonal model. 

Inputs are: 

```
# plotweather :: Plot elements of the weather table; estimate opacity.
vis = ''              # MS name
seasonal_weight = 0.5 # weight of the seasonal model
doPlot = True         # set this to True to create a plot
plotName = ''         # (Optional) the name of the plot file
```

The amount of seasonal data can be set by the parameter *seasonal_weight*, where a value of 1 will only use the seasonal model and a value of 0 will only use the actual weather data to calculate opacities. 

Typical output of **plotweather** looks like below:

![a36812b09ef65bbf1d85a367204f1070b66a1a2b](media/a36812b09ef65bbf1d85a367204f1070b66a1a2b.png)

>Typical output from plotweather. The panel at the top displays the following properties as a fiunction of time across the observation: elevation of the sun, wind speed and direction, temperature and dew point, and precipitable water vapor (pwv). The bottom panel shows the calculated zenith opacity as a function of  frequency. The opacities calculated from the actual weather data, from a seasonal model and the specified mix of both are shown in the PWV and Tau plots. 
  

The methods used in this task are described [EVLA Memo 143](http://library.nrao.edu/public/memos/evla/EVLAM_143.pdf), [VLA Test Memo 232](http://library.nrao.edu/public/memos/vla/test/VLAT_232.pdf), and [VLA Scientific Memo 176](http://library.nrao.edu/public/memos/vla/sci/VLAS_176.pdf).  The wind direction aligns with the meteorological definition, i.e., north is up (0deg) with the angle increasing clockwise E, S, W (e.g., a vector pointing to the right indicates westerly winds with an angle of 270deg).   

 

Allowed output plot formats are those supported by matplotlib, currently emf, eps, pdf, png, ps, raw, rgba, svg, and svgz.

 

<div class="alert alert-warning">
Alert: **plotweather** accesses the WEATHER table in the MS. The task may therefore also work for non-VLA data as long as such a table is present. The plots and calculations, however, have been tailored for the VLA, so non-VLA data may or may not be interpreted correctly.   
</div>

 

 

 

 
