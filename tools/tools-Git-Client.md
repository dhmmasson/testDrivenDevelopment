
# Pandora Java Project and Git

## Account and Git Client

* Create a user account on [GitHub](#https://github.com/)

* **important** Make sure to disable notifications in your settings. We will create more than 100 issues that you will have to take care of (i.e. implement features, functionalities) and mark them as complete. During the creation, you might get an email for each one of them if you don't disable the notifications!

* Install a git client (e.g., [GitHub Desktop](#https://desktop.github.com/))

![alt text](img1.png "Desktop client")
> _Fig.1_ A basic Git Desktop client

* Click on "clone a repository from the internet”

![alt text](img2.png "Clone a repo")
> _Fig.2_ Cloning a repository

* Select the project that has been created for your group project. The url is something like https://github.com/Estia-advanced-programming/pandora-2020-group1-GROUPENAME.git

* Select the location you want the download to happen on your computer. Remember this location, you will need it to import the project in [Eclipse](tools-Eclipse.md) later.

* Click "clone"


## EGit, the Eclipse Git Plugin

Another possibility is to get everything in one place! (Repository, code, issues, tasks, etc). Check out [this tutorial](https://eclipsesource.com/blogs/2012/08/28/tips-and-tricks-using-eclipse-with-github/).
Basically, you need to understand that Git can be used with several projects, not only Java and Eclipse. If you understood that, then we can start to look at how some tools (e.g., Eclipse, Visual Studio, etc) integrates Git tools.

For Eclipse, it is called EGit. It can be useful to have a quick access to milestones and issues (Fig.3 - 1) or the branches history (Fig.3 - 2). You can quickly open / close issues, switch branches, commit, push, pull, go back to a previous version just by right-clicking on the project (or just one file), finding the `Team` menu item, and browsing the options.

![alt text](views.png "Git in Eclipse")
> _Fig.3_ Git in Eclipse

If you already have Git in Eclipse, you should have the `Team` option when right-clicking on your project (and see some yellow icons to indicate that the project is under version control). If this is the case, just go to the [configuration](#configuration) section. Otherwise, perform the install.

### Install

1. In Eclipse, click `Help` and `Install new software...`

1. Click `Add` source (Fig.4 - 1), then `name` it `egit` (or whatever) and write the `location` to `http://download.eclipse.org/egit/updates` (Fig.4 - 2)

![alt text](add_egit.png "Adding an install")
> _Fig.4_ Adding an install source in Eclipse

1. Now select this newly added items, check all packages, and continue the installation.


### Configuration

Egit should already know what is going on in your repository: the tool looks into your .git folder, where everything is already configured (remote repository, etc). You might only need to input your login/password the first few times you will trigger commands.

For the task view, you need an additional package.

1. As in the [install](#install) section, add a new package repository with a name (e.g., `mylin`)  and this location `http://download.eclipse.org/egit/github/updates`.

1. Finish the installation of the package

1. Then, you can finally set up your tasks repository (or issues, etc) by following this [tutorial](https://eclipsesource.com/blogs/2012/08/28/tips-and-tricks-using-eclipse-with-github/) 





# Branches

When working with git, you can create, add, delete special tags, which will in turn create what is call branching: your next progress will be identified by this tag. In then end, these tags are useful to track which progress (`commit`) depend on which previous ones. 
This branching is mainly used to develop a feature, a functionality, or anything else that is a little topic on its own. It allows the developer to implement, test, and work on the feature without interfering with the other branches. 

To learn more on Git Branching: [see this link](https://learngitbranching.js.org/)


## Master Branch

The master branch is usually the one where everything works fine. This is the branch we will use to test your program.
It is common to merge and push your current work on 'Master' only when you are sure that:

1- There is no conflict

Make sure you Pull the master branch before trying to push your work. Resolve every potential conflicts locally. With this in mind, you will always push a clean version that any new comers could clone and run.

2- Your current task is complete

It is usually not every 5 minutes that people push on the Master branch. You save your work locally (commit), and push on GitHub on your branch when you reached (or think your reached) a consequent step. You can then merge the branch you were working on with Master when the task at hand is completed. You can then ask your team to review your code and accept the merging via a Pull request.



## Pull Request





# Summary

* Create a branch **locally**
	* Name it develop_yourName_NameOfTheFeature
* Code, code, code... Debug, code, code, code
* Commit locally every time that something run
* When the feature is done : Clean up, Comment
* Pull the remote code
* Resolve any conflict that you might have
* Commit, push, and do a pull request
* Continue




# Ressources

Some of the [ressources][github-guide] used to create this page,
[Git handbook][Git-handbook]

[Git-handbook]: https://guides.github.com/introduction/git-handbook/
[github-guide]:https://guides.github.com/
