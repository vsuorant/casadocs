

# Introduction to CASA Documentation 

General information about CASA Documentation

\--CASA Developer\--

# Introduction

CASA documentation exists in multiple locations, each designed to address a specific need.  Before adding content to any of the locations, ensure you have chosen the correct site for your type of documentation:

-   CASA Docs: The CASA Docs are maintained on two servers: the [CASA Docs production](https://casa.nrao.edu/casadocs/) server and the [CASA Docs development](https://casa.nrao.edu/casadocs-devel/) server.  Contributions to the documentation should always be made on the development server.  A static copy of this documentation is maintained for each release on the production server.  Please respect the [style guide](https://casa.nrao.edu/casadocs-devel/stable/casa-development-team/documentation/style-guide) when adding to the CASA Docs.  The CASA Docs include the following types of content:    -   End-user information on how to use CASA, the theoretical background behind CASA algorithms, as well as documentation on tasks and tools,
    -   Developer-oriented information on various aspects of the CASA system; this information is intended for CASA team developers as well as developers outside the CASA team, and
    -   Information on processes followed by the CASA Development team.
-   Inline Help: Available using the help() command at the CASA prompt, the inline help documents tasks and tools and is derived from XML stored in the CASA code repository. (Note that the parameter description in the inline help is parsed to the \"Parameter\" pages of the Global Task List in CASA Docs)
-   [CASA Guides](https://casaguides.nrao.edu/):  This site includes walk-through like guides for processing data in CASA.  These guides are mostly maintained by the ALMA and VLA user support groups.
-   [CASA Twiki](https://safe.nrao.edu/wiki/bin/view/Software/CASA/WebHome "CASA Twiki"): This site is used to record some administrative information such as meeting minutes and committee reports.  The Twiki predates Confluence and also includes historical project documentation.  The [CASAIndex](https://safe.nrao.edu/wiki/bin/view/Software/CasaIndex) is an even older wiki, but may still contain useful information.
-   [Confluence](https://open-confluence.nrao.edu/display/CASA/CASA+Home): This site is used to record CASA team planning information regarding releases and team projects.  The site also includes a team calendar that is integrated with JIRA.

 

# CASA Docs

The [CASA Docs](https://casa.nrao.edu/casadocs/) are stored on the NRAO CASA Docs server, and can be accessed in CASA with the doc() command.  The CASA Docs were first released with CASA 5.0 as a replacement for the [CASA Cookbook](http://casa.nrao.edu/docs/cookbook/index.html), [Task Reference](http://casa.nrao.edu/docs/TaskRef/TaskRef.html), [Toolkit Manual](http://casa.nrao.edu/docs/CasaRef/CasaRef.html), and other miscellaneous CASA documentation.  The CASA Docs were incomplete at the time of the 5.0 release, including only a subset of CASA tasks and tools. As per CASA 5.3, all tasks have been included in CASA Docs. The tools will be added in future releases.

CASA Docs Plone accounts are created either automatically based on the NRAO Windows Active Directory (AD) system, or by a Plone administrator manually creating a new account.  All NRAO staff have a Windows AD account and therefore have an account on the CASA Doc Plone system.  In addition to having an account, all CASA Docs contributors must be added to the \"Content Creators\" group in Plone.

The CASA Docs Plone server has been set up to allow for 3 page states: Private, Internal, and Public.  The state of any page can be changed in the left-side Plone tool bar, visible after logging into the CASA Doc Plone system.

-   The **Private** state is the default state for a new page.  Pages in the private state are only visible by members of the Content Creators group.  New CASA Docs content should remain in the Private state until it is validated by the CASA validation team.
-   **Internal** pages are visible by any person logged into the Plone system, whether or not they are in the Content Creators group.  The Internal state was created for CASA documentation that should be visible to observatory staff but should not be visible to the world.  This includes some information about the CASA build and test system.
-   **Public** pages are visible to the world.  Pages are made public after being validated.

In addition to the page state, all pages contain two additional flags: the developer flag, and the subtopic flag.  Both flags can be set when editing a page.

-   The **developer flag** marks the page as being visible only in developer mode.  Developer mode can be toggled on and off using the right-side tool bar.  Look for the icon with the \<\> brackets.  By default developer mode is off and all developer pages are hidden from the Plone navigation.  When turned on, the developer pages become visible in the Plone navigation, and are appended by \"(developer)\".
-   The **subtopic flag** marks a page as containing a subsection of the previous page.  This allows for an additional level of hierarchical organization without using an additional Plone folder.  Subtopic pages, like all pages, must be organized manually using the \"Contents\" view, available from the left-side Plone toolbar.

## CASA Docs Contribution Process

Contributions to the CASA Docs should follow the process described here.  All CASA Docs changes should be recorded in a JIRA ticket (unless the change is very minor; e.g. grammatical corrections); the JIRA ticket will follow the same basic process used for software development work. 

The author should be familiar with the CASA Docs Style Guide before adding content.  After adding all the new content to Plone, the JIRA ticket should be moved to the Ready to Verify state and assigned to the CASA Scientific Testing Lead (currently Jen Donovan Meyer).  Jen will assign the ticket to a style reviewer who will verify that the new content conforms to the Style Guide.  The style reviewer may make changes to the page to bring it into conformance with the style guide.  After passing style review, the JIRA ticket will be moved to the Ready to Validate state and Jen will assign the ticket to a content reviewer.  (Currently, we are only performing content reviews for pages that are not in developer mode.)  The content reviewer may make small changes directly to the document.  Requests for extensive changes will be returned to the author, at which point the JIRA ticket will go through the Verification and Validation process again.  After passing validation, Jen will mark the associated Plone page(s) as public and resolve the JIRA ticket.  The documentation changes will then become public during the next weekly update of the prerelease documentation on the CASA Docs production server.

## Task and Tool Documentation

Each task folder contains a parameters page that includes documentation on each parameter in the task.  This parameter documentation is derived from XML files that are stored in the CASA source code.  You can find the task XML files in your CASA source code under casa/gcwrap/tasks/.  Likewise, tool methods are documented using XML files that are stored under casa/gcwrap/tools/.

<div class="alert alert-warning">
Do not edit the content of task parameter pages or tool method pages in Plone!  This content is dynamically generated from the XML files.  The XML files should be edited instead.
</div>

As described in the CASA Docs Style Guide, task and tool names should be written in bold text.  The Plone system has been designed to automatically link bold task/tool names to the corresponding task/tool folder.  To enable this autolinking for a new task or tool, notify the CASA Docs web developer.  This notification is currently being done via JIRA ticket [CAS-9596](https://open-jira.nrao.edu/browse/CAS-9596). 

## Development and Production

The CASA Docs development server is here: <https://casa.nrao.edu/casadocs-devel/>.  This is where contributors should add and edit CASA Docs content.  The version of the CASA documentation on the development server should very closely follow the BitBucket master branch.  Some discrepancies may exist when developers are waiting for a pull request to be serviced.  However, developers should aim to add content to the CASA Docs development version only when they believe the corresponding code will be pulled into the master branch imminently.  Special care should be taken around the time of feature and code freezes.

The CASA Docs production server is here: <https://casa.nrao.edu/casadocs/>.  The production server hosts CASA Documentation for each major release and patch beginning with CASA 5.0.  The CASA Docs production server also contains documentation for the latest CASA prerelease, which is updated on a weekly basis from the development server.  All documentation on the production server can be updated by Plone administrators, and, when necessary, by other Plone account holders. 

When a new release branch is created in BitBucket, a permanent snapshot of the development documentation is made on the production server.  After creating the snapshot, the development documentation continues to follow the BitBucket master branch toward the subsequent CASA release.  In the case of a CASA patch, the CASA Docs web developer will copy the appropriate documentation tree to create a new documentation tree for the patch.  For example, if a 5.0.1 patch is planned for release, the 5.0.0 tree should be copied and renamed 5.0.1.  A plone administrator should then update the new tree based on the content of the patch.

## Packaging

When a new CASA build is created, the appropriate CASA Docs tree is copied off of the production server using a wget script.  Only public pages are included in the packaged documentation.  The packaged documentation can be accessed using the doc() command from the CASA command line.  The doc() command accepts string arguments that open the documentation to specific CASA Doc pages.  The mapping between the string arguments and CASA Doc pages is contained in the toc.xml file:

```
/home/casa.nrao.edu/content/PloneResource/stable/toc.xml
```

This file contains an \<entry\> block for each task and tool.  Each entry block contains a \<visibility\> block with value \"internal\" or \"external\".  All tasks that have been made public in CASA Docs should have visibility value \"external\".  As new tasks are added to the CASA Docs, new \<entry\> blocks should be created with all relevant information.

<div class="alert alert-warning">
From CASA 5.5 onward, the CASA Docs are no longer packaged with each CASA Release, and \"doc(\'taskname\')\" will instead point to the online CASA Docs.
</div>

 
