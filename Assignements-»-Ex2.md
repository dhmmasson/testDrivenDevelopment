# Exercice 2

# Description 

In this exercice all member will edit the same file on their local repository to learn about conflict resolution. Decide among yourself who will play each member and read the instructions accordingly. 

# Member 1 

You have decided to update the team members information. You will modify the README and add some information about yourself. 
1. Make sure that your local copy is up to date, if not pull any modification from the remote repository. 
1. Modify the README file, add some elements about yourself in the team member section.
1. Commit your modification
1. If you are not first in the list move yourself up.
1. Commit your modification
1. WAIT for the other to have commited their change locally
1. push your commit(s) to the remote 
1. WAIT 

# Member 2 

You have decided to change the title of the README page ( and only that ) 
1. Make sure that your local copy is up to date, if not pull any modification from the remote repository. 
1. Modify the README file, add some elements about yourself in the team member  
1. If you are not first in the list move yourself up.
1. Commit your modification
1. Wait for Member 1 to push its commit to the remote 
1. Your local branch is now behind the remote - you must **pull** the commits before pushing onto the remote 
1. Git will merge your modification with member1. If the modification are in different files, or far apart in a file it will create a new commit directly that is the union of your changes.


# Member 3 

You have decided to update the team members information. You will modify the README and add some information about yourself. 
1. Make sure that your local copy is up to date, if not pull any modification from the remote repository. 
1. Modify the README file, add some elements about yourself in the team member  
1. If you are not first in the list move yourself up.
1. Commit your modification
1. Wait for Member 1 to push its commit to the remote 
1. Your local branch is now behind the remote - you must **pull** the commits before pushing onto the remote 
1. Git will merge your modification with member1. If the modification are in different files, or far apart in a file it will create a new commit directly that is the union of your changes.
1. If not you will be left with files that have modifications to be done
1. Open README.md you will find lines that look like that  
  ```
  <<<<<<< HEAD
  your modification
  =======
  other member modification
  >>>>>>> branch-a

1. Replace the whole block by you modification followed by the other member modifications 
1. Commit the new file and push your commit(s) to the remote 

## Close the issue

You are done, go back to your `project management` project page on github, close the issue and move it to Done.

# Task

- [ ] Member1 modify `README.md` and create a commit locally
- [ ] Member2 modify `README.md` and create a commit locally
- [ ] Member3 modify `README.md` and create a commit locally
- [ ] Member1 *push* their commit to the remote repository
- [ ] Member2 and 3
          - Pull the commit from member1
          - Merge the modification into their local repository
          - Commit
- [ ] Member2  *push* their commit to the remote repository
- [ ] Member2 and 3
          - Pull the commit from member1
          - Merge the modification into their local repository
          - Commit  
