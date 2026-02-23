# FAQ

> - [When and what to commit ?](#faq1)
> - [When and where should I push my commits to the remote repository (GitHub) ?](#faq2)
> - [When Should I Create a branch ?](#faq3)
> - [When should I not create a branch ?](#faq4)
> - [When to create a pull request ?](#faq5)
> - [My code is completly broken and I want some help](#faq6)

<a id="faq1"></a>

## When and what to Commit?

Regularly! You should make small commits that you could sum up in a few line. Remember that the first line of the commit will appears as a title, it should be significant and memorable to you and others. You can use a keyword in brackets [] to indicate if the commit add a new **Feature**, **Fix** a bug, **Clean** the code (fixing the indentation, using proper names for variables and methods), **Doc**ument or add some comment to your code.  
The code you commit should normally compile and run without to many issues. If you commit something that is broken it should be made extra clear for the other.

Some example of good commits:

- whenever you add a new methods: create a commit with a title like

  ```
    [Feature #28] Added method formatDuration to analysis.java

    Created a new function that format a duration to the format HH:mm:ss by dividing by 60 multiple time and taking the reminder.

    adding close and the issue number will automatically close the issue when the pull request is merged
    Close #28
    ```

- Correct a bug:

  ```
    [Fix] Removed bug in format in -o flightDuration

    flight duration was returned in seconds instead of HH:mm:ss
    ```

- Comment some code, clean some code
- Improve, optimize some code
- Move, remove some files. These operations are complicated to merge (e.g. if someone try to modify a file that has been removed)

<a id="faq2"></a>

## When and where Should I Push My Commits to the Remote Repository (GitHub)?

- You should push your commits when you want to share your contributions with the rest of the team or you want someone to review your code.
- You can push multiple commits at the same time.
- **You should never commit directly to the branch master**

In general you should push your commits to a branch that is named yourName/Feature, then create a pull request from your branch to the branch you want to merge into.

Some examples:  
Alice wants to work on flightDistance in the milestone 3. She create locally a branch that she names Alice/flightDistance. She adds some code to Computation.java, and runs it. She creates a commit locally.

```
  [Feature #28] Add methods to computation.java


  Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
```

She also adds some new test files to verify her code and commits that locally

```
  [Test] Add some new tests to validate flightDistance

  flight_distance101.frd is a flight with a distance of 101m
  flight_distance0.frd is a flight with a distance of 0m
```

She then **push** her local branch Alice/flightDistance to the **remote** (GitHub).  
On Github she creates a pull request named ```[WIP] flightDistance``` from her branch to the branch milestone3 to inform the other that she has been working on the feature flightDistance.

From the pull request, she can request reviews from the other, help from the teacher or merge into milestone3 if the others contributors agree.

<a id="faq3"></a>

## When Should I Create a Branch?

A branch is just a label that point to a particular commit. you can create branch locally and then push them to GitHub, you can also create branch on GitHub and pull them into your local repository.

You should create branches whenever you are starting something new or you want to test something:

- You are starting to work on a new feature, create a local branch ```yourName/featureX```
- You want to clean up some previous code, and intend to change multiple files.
- You want to prepare for the next release/milestone. Create a branch ```milestoneX``` on GitHub. Then merge feature branches with pull requests into it until you have a complete milestone. When you think your milestone branch is ready create a pull request against the master branch. This will trigger the auto-evaluation. You can see in the details of the *Milestone Assessement* there is an artifact named score-report.  

<a id="faq4"></a>

## When Should I not Create a Branch?

You are improving something, for instance you are adding some tests to a feature, you are adding some comments, you are cleaning  
<a id="faq5"></a>

## When to Create a Pull Request?

You want to share some progress: create a branch with

<a id="faq6"></a>

## My Code is Completely Broken and I want Some Help

- Create a branch with an appropriate name. ex: YouName/flightDuration
- Make a commit with an appropriate name tag: [Broken] NullPointerException with feature flightDuration on f201_ru.frd (or make multiple commits if you can)
- Create a pull Request with an appropriate name [WIP] flightDuration between your branch and
