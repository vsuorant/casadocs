

# Definition Synthesized Beam 

Definition of the Gaussian function that CASA uses for the synthesized beam

CASA uses the following zero-centered two dimensional elliptical Gaussian function or Gaussian beam:$$\begin{align} f(x,y) &= A \exp\left\lbrace -\left(\frac{4 \ln(2)}{d_1^2} (\cos(\theta) x + \sin(\theta) y)^2 + \frac{4 \ln(2)}{d_2^2} (-\sin(\theta) x + \cos(\theta) y)^2 \right)\right\rbrace, \label{eq:1} \end{align}$$where A is the amplitude (usually set to unity) and $\theta$ is the anti-clockwise angle from the x axis to the line that lies along the greatest width of $f(x,y)$ (the line and the x axis must be coplanar). The factors $d_1$ and $d_2$ are respectively the semi-major and semi-minor axis of the ellipse, which is formed by the cross-section that lies parallel to the $x, y$ plane, at a height so that $d_1$ is equal to the FWHM (full width at half maximum) distance of the one dimensional Gaussian which lies on the plane formed by the $z$ axis and $d_1$. Note that $d_1 \geqslant d_2 > 0$, since $d_1$ is the semi-major axis.

> <div>
>
> ![bd6ce30313654fc00a6d88e248e1ae0e864f1edf](media/bd6ce30313654fc00a6d88e248e1ae0e864f1edf.png)
>
> </div>
>
> <div>
>
>>Figure 1: Surface plot of a two dimensional elliptical Gaussian with $A = 1$, $d_1 = 3$, $d_2=1$ and $\theta = 30^\circ$.
>   
>
> </div>
>
> <div>
>
>  
>
> </div>
>
> <div>
>
> > <div>
> >
> > ![5cd15ffb3f39e942040ef35a229b1e5d3f11a9e1](media/5cd15ffb3f39e942040ef35a229b1e5d3f11a9e1.png)
> >
> > </div>
> >
> > <div>
> >
> >>Figure 2: Cross-section parallel to the $x, y$  plane of the two dimensional elliptical Gaussian from Fig. 1, where the resulting ellipse has a semi-major and semi-minor axis equal to $d_1$ and $d_2$, respectively.
> >   
> >
> > </div>
> >
> > <div>
> >
> >  
> >
> > > <div>
> > >
> > > ![79bf91cfc2367dde815f4b998c57847420f15018](media/79bf91cfc2367dde815f4b998c57847420f15018.png)
> > >
> > > </div>
> > >
> > > <div>
> > >
> > >>Figure 3: One dimensional Gaussian plot for $A = 1$, $y = 0$, $\theta  = 0$ and $d_1 = 1 = FWHM$.
> > >   
> > >
> > > </div>
> > >
> > > <div>
> > >
> > >  
> > >
> > > </div>
> >
> > </div>
>
> </div>

For calculating the Fourier transform of the two dimensional elliptical Gaussian, the above Equation can be re-written by grouping the $x$ and $y$ terms:$$\begin{align} f(x,y) &= A \exp\left[-\left(\alpha x^2 + \beta y x + \gamma y^2\right)\right], \label{eq:eg_2} \end{align}$$where$$\begin{align} \alpha &= 4 \ln(2) \left[ \frac{\cos^2(\theta)}{d_1^2} +\frac{ \sin^2(\theta)}{d_2^2} \right], \label{eq:a} \\ \beta &= 8 \ln(2) \left[ \frac{1}{d_1^2} - \frac{1}{d_2^2} \right] \sin(\theta) \cos(\theta) ,\\ \gamma &= 4 \ln(2) \left[ \frac{\sin^2(\theta)}{d_1^2} +\frac{ \cos^2(\theta)}{d_2^2} \right]. \label{eq:g} \end{align}$$

Converting from $\alpha, \beta, \gamma $ to $d_1, d_2, \theta$ can be done using the following set of equations:$$\begin{align} d_1 &= \sqrt{\frac{ 8 \ln(2) }{ (\alpha + \gamma) - \sqrt{\alpha^2 - 2\alpha\gamma + \gamma^2 + \beta^2} }}, \label{eq:d1} \\ d_2 &= \sqrt{\frac{ 8 \ln(2) }{ (\alpha + \gamma) + \sqrt{\alpha^2 - 2\alpha\gamma + \gamma^2 + \beta^2} }}, \label{eq:d2}\\ \theta &= 0.5 {\rm arctan2}(-\beta,\gamma-\alpha). \label{eq:t} \end{align}$$

 
