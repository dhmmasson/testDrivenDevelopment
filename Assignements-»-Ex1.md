# Exercice 1 

Learn how to change something in the project and publish the change to the world.

## Create a github account - Download Git

Go to github and create an account, or login to an existing account. You may use any address to use GitHub for Free. If you use your @net.estia.fr you will be eligible for a student Developer Pack, which offers free access to tools and services used by professional developers. If you already have an account you can link it to your estia address.

To use git on your computer, you'll need a client:

* https://desktop.github.com/

* Settings modification remove emails spam

[Checkout the tutorial](./Tutorial-»-Git-Client)


## Create repositories

There are two ways to start a Git project. You could start locally to track change of a project and at some point decide to share it with collaborators, creating a remote repository onto which you would push your history.
Or you can start by creating a non empty remote repository and clone it locally ( either by starting with a template repository, or by forking ( duplicating ) someone else project ).

you will start from a template repository created specifically for this class.  

### Create remote repository
In a normal setting you would go to your github page to create a repository and then share it with collaborators. For this course will use the following [link][classroomAssignement] that will create a repository for your team, and populate it with a starter code. Once the repository created go to the home page and bookmark it for future reference.

Before we create our local repositories will look around the github user interface.

### Create a project

From the github page of your project, click on the menu Projects. Projects are boards ( like trello or planner ) to organize your team task. 

- [ ] Create a new project 
  - Call it project management
  - Set a description : Project board for the pandora project
  - Set it to : Automatic Kanban

In the background, a special task for the project has been created :  it will create more than an hundred issues (it may take some times). Each issue is related to a task you have to do in this project. Most of them are [Features](./Pandora-»-Features) to implement, some relate to the start up exercices. Having a lot of issues makes it hard to find the ones you care about. Milestones, labels, and assignees allows to filter and categorize issues. 

- [ ] Discover the milestone for the start up exercices 
  - From the Github project page, click on the menu Issues 
  - Find the issues related to the exercice 1, 2, 3. 
    - They should have the label good first issues 
    - They should be part of the milestone Initiation to Git. 
  - Open the Exercice 1 issue, read it and from the menu on the right 
    - [ ] Assign Members to the Issues. 
    - [ ] Add them to the project 

### Create local repositories

Each member will need is own local repository to contribute. In a DVCS ( Distributed Version Control System ) like git, each contributor as a local copy of the revision tree that they synchronize with the remote repository.  

## Be the change that you wish to see in the world.

One member will make some change to the project and publish them for the rest of the group to see.

1. Open with a text editor of your choice the file README.md.
2. Add the following
    ```markdown
    # Group Members

    - < Firstname LastName of first member of the group >
    - < Firstname LastName of second member of the group >
    - < Firstname LastName of third member of the group >
    ```
1. Go to github desktop.
1. Stage the change : Select the modifications you want to add to the next commit. 
1. Commit with a message explaining your change ( e.g. Added project members to the README ) 
1. Push your commit to the remote repository.

## Discover change

- On the github webpage
    - Go to the Code tab ( the home page )
    - Click on the menu Commits ( in the Code menu bar, located below the main menu ) to see the commits
- propagate the change with a pull from the other local repositories ( member2 and 3 )
    - On each github desktop pull changes

## Close the issue

Go back to your `project management` project page on github, close the issue and move it to Done.

You now know :

- [ ] How to create a group repository
- [ ] How to create a local repository
* [ ] How to make and stage your modifications
* [ ] How to commit your progress with a message
- [ ] How to push your commit to a group repository

# Next exercice :
[ Ex2 ]( ./Assignements%3A-Ex2 )

[//]: # (Reference for this page)
[classroomAssignement]: https://classroom.github.com/g/XH2huM0G
