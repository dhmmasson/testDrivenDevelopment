# Git

# Version Control

## The problem

How have you saving your modifications while working on a project until now ? Have you named the same file:  `internship_report.pdf`, `internship_report_v1.pdf`, `internship_report_v2.pdf`, `internship_report_v2_Final.pdf` ? Have send this file to Alice Martin to received `internship_report_v2_Final_AM.pdf` and went on having `internship_report_v1_Final_AM_2.pdf`, ... `internship_report_v1_Final_AM_2_Finale.pdf`...

Maybe you have used google drive, or Microsoft OneDrive to manage the diferent version of a file. You have shared a file in the cloud that automagically save all the change made by you and your contributors. Maybe you know about the revision system that tracks individual change and you came back on a previous version. But working concurrently on a same section or on different files is not easy.

All the previous systems ( saving backups, using cloud solutions ) are version control system, albeit not very good one for software development project.  

> *From the [Git handbook][git-handbook]:*
>
> A version control system, or VCS, is a system that tracks the history of changes as people and teams collaborate on a project together.  As the project evolves, teams can run tests, fix bugs, and contribute new code with the confidence that any version can be recovered at any time. Developers can review project history to find out:
> - Which changes were made?
> - Who made the changes?
> - When were the changes made?
> - Why were changes needed?

A distributed version control system (DVCS) is a type of version control where the complete codebase — including its full version history — is mirrored on **every developer's computer**. It's abbreviated DVCS.

> *From the [Git handbook][git-handbook]:*
>
> Git is an example of a distributed version control system (DVCS) commonly used for open source and commercial software development. DVCSs allow full access to every file, branch, and iteration of a project, and allows every user access to a full and self-contained history of all changes. Unlike once popular centralized version control systems, DVCSs like Git don’t need a constant connection to a central repository. Developers can work anywhere and collaborate asynchronously from any time zone.

# Install

TODO: integrate William Tutorial.

# Branches

What is a branch,
## master, develop ...

master
: The master 

## Pull requests


# Create a feature

* Create a branch **locally**
  * name it develop_yourName_NameOfTheFeature
* Code, code, code...
* Commit locally every time that something run
* When the feature is done : Clean up, Comment
*

# Ressources

Some of the [ressources][github-guide] used to create this page,
[Git handbook][Git-handbook]

[Git-handbook]: https://guides.github.com/introduction/git-handbook/
[github-guide]:https://guides.github.com/
