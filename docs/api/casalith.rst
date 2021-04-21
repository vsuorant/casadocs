casalith
====================

CASA monolithic environment bundling Python and library dependencies into a single download package.

executables
^^^^^^^^^^^

The following executable applications are located in the <casa release>/bin directory of the expanded monolithic CASA tarball:

- python3 (version 3.6.7)
- pip3 (version 9.0.1)
- 2to3 (version undefined)
- casa (versioned by this package)
- mpicasa (versioned by this package)
- casaviewer (versioned by this package)
- buildmytasks (versioned by this package, see casashell)


python libraries
^^^^^^^^^^^^^^^^

The following third party libraries are included in the python distribution of monolithic casa and available as imports:

::

almatasks==1.1.17
attrs==19.3.0
auditwheel==3.1.1
backcall==0.1.0
cachetools==4.1.1
casadata==2021.4.19
casampi==0.4.2
casaplotms==1.1.16
casaplotserver==1.0.5
casashell @ file:///wheeldirectory/casashell-6.2.0.115-py3-none-any.whl
casatasks @ file:///wheeldirectory/casatasks-6.2.0.115-py3-none-any.whl
casatelemetry==1.2.3
casatestutils @ file:///wheeldirectory/casatestutils-6.2.0.115-py3-none-any.whl
casatools @ file:///wheeldirectory/casatools-6.2.0.115-cp36-cp36m-manylinux2010_x86_64.whl
casaviewer==1.1.8
certifi==2020.12.5
cycler==0.10.0
decorator==4.4.2
google-api-core==1.22.1
google-api-python-client==1.10.0
google-auth==1.20.1
google-auth-httplib2==0.0.4
google-auth-oauthlib==0.4.1
googleapis-common-protos==1.52.0
grpcio==1.26.0
importlib-metadata==1.6.0
ipython==7.15.0
ipython-genutils==0.2.0
jedi==0.17.0
kiwisolver==1.2.0
matplotlib==3.2.1
more-itertools==8.3.0
mpi4py==3.0.3
numpy==1.18.4
oauthlib==3.1.0
packaging==20.4
parso==0.7.0
pexpect==4.8.0
pickleshare==0.7.5
pluggy==0.13.1
prompt-toolkit==3.0.5
protobuf==3.12.2
ptyprocess==0.6.0
py==1.8.1
pyelftools==0.26
pyfits==3.5
Pygments==2.6.1
pyparsing==2.4.7
pytest==5.4.2
python-dateutil==2.8.1
pytz==2020.1
requests-oauthlib==1.3.0
scipy==1.4.1
six==1.15.0
traitlets==4.3.3
uritemplate==3.0.1
wcwidth==0.2.2
zipp==3.1.0


The definition is provided here in pip compatible format such that one could save the preceding list to a list.txt file and
recreate using:

::

   pip install -r list.txt


