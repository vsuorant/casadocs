

# User tips on installing CASA on unsupported OSs 

This document provide tips from users on how to install CASA on unsupported operating systems, like LINUX Ubuntu, Debian, and Fedora.

***Disclaimer: the information in this document is provided by users and not verified by the CASA team. The information does not reflect official CASA recommendations and should be used at your own risk. ***

 

CASA officially supports certain versions of LINUX Redhat and Mac OSX. See the [CASA Download page](https://casa.nrao.edu/../casa_obtaining.shtml) for more information.

We realize that many users wish to try and run CASA on different operating systems. Below are some tips from the user community on installing CASA on unsupported platforms. CASA will not run on Windows.

 

#### Ubuntu or Debian

Please see the following PDF: [Installing CASA on Unbuntu or Debian](https://casa.nrao.edu/casadocs-devel/stable/memo-series/casa-knowledgebase/installing_casa_ubuntu_debian.pdf)

 

#### Fedora

Fedora 32 may cause CASA to crash on startup with the error *\"code for hash md5 was not found\"*. This is caused by changes to libssl.so in the compat-openssl10 package, which prevents the CASA supplied version of this library from loading. An easy fix is to replace the CASA version of libssl.so.10 with the OS version in /lib64 (i.e., libssl.so.1.0.2o).
