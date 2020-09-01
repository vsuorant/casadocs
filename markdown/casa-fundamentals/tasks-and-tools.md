

# CASA Tasks & Tools 

Summary of CASA tasks and tools

Originally, CASA consisted of a collection of tools, combined in the so-called toolkit. The current toolkit still contains the full functionality of CASA, though most data reduction steps bundle a number of tools together to create the more familiar CASA tasks. That is to say, a task makes calls to a number of tools. 

While running CASA, you will have access to and be interacting with tasks, either indirectly by providing parameters to a task, or directly by running a task. Each task has a well defined purpose, and a number of associated parameters, the values of which are to be supplied by the user. 

The following subpages describe the [CASA Tasks](https://casa.nrao.edu/casadocs-devel/stable/old-pages/casa-tasks-and-tools/casa-tasks) (also listed in the [Global Task List](https://casa.nrao.edu/casadocs-devel/stable/global-task-list)) and [CASA Tools](https://casa.nrao.edu/casadocs-devel/stable/old-pages/casa-tasks-and-tools/casa-tools) (listed in the [CASA Tool List](https://casa.nrao.edu/casadocs-devel/stable/global-tool-list)) in more detail. 

 

## Experimental tasks and algorithms

Some tasks and algorithms in CASA are labelled in CASA Docs as \"Experimental\" or \"Unverified\", and users are warned to used these tasks and algorithms at their own descretion. Such tasks and algorithms may still be added to official CASA releases, either because they enhance user capabilities, or because they are required for specific pipeline use.

The label \"Experimental\" or \"Unverified\" means that the task/algorithm falls under the following disclaimers:

-   Only a subset of modes have been incorporated into CASA unit/regression tests. These are documented in CASA Docs. Other options/modes may be run, and might work just fine, but they are not part of what has been tested carefully.
-   Some parameters have been tested for specific use cases (as part of the algorithm development, publication, and CASA test programs), but we have not yet established best practices for all different situations. This information will build over time and will be incorporated into our documentation as appropriate.
-   Experimental tasks and algorithms may have Known Issues, representing CASA\'s current understanding of the state of the code. These [Known Issues](https://casa.nrao.edu/casadocs-devel/stable/introduction/known-issues) are clearly defined as part of CASA Docs.
-   Parameter names and task structure can change, based on feedback and improved understanding of usability.

It is expected that ALMA and VLA pipelines will begin using experimental tasks only after they have stabilized for stand-alone use.
