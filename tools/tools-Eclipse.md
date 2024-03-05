
# Pandora Java Project


## Eclipse

You already cloned the application skeleton on your computer. This means you are ready to start working on a local version of the program.

* First, open Eclipse
* Select 'File', and 'import...'
* Select the 'existing maven project' under the 'maven' directory
* Locate the project you cloned from GitHub

And everything should (nearly) be ready to run.

## Running Pandora

In order to run, the program expects some arguments. For instance, the command `java -jar pandora.jar -o flightDuration ./src/test/resources/flightReport_fl12.frd` will output the total flight duration logged in the flightReport_fl12.frd file (dummy example).

In order to do so via Eclipse, you should:
* Click on `run configuration` (menu when clicking on the right of the little `run` green icon) (Fig. 1 - 1)
* Select the `Java Application` (Fig. 1 - 2) and click on the 'New' icon (Fig. 1 -3)
* Name it, and click on the `arguments` tab (Fig. 1 -4)
* Type `./src/test/resources/0_201_MiG-23MLD.frd `
* Click `run`

You should see the program running!

![alt text](screen_eclipse.png "Running configuration")
> _Fig. 1 Eclipse screenshot for running configuration_


It can be cumbersome to run several configurations. You can of course save your configuration, but also create `launch group` in which you can include as many configuration you set up in sequential order. Otherwise, you can also omit the output option parameter `-o`. In this case **every output** will be printed.

At this point, note that there is nothing else implemented.
A list of options (more than 100) to implement is [available](Features.md), and this is your job to complete the program.


## Running multiple tests in one go

It can be cumbersome to change the Eclipse run settings every time you want to run Pandora on a new file or a new feature.
We hence provide a second main method in the `fr.estia.pandora.test` package: **MultiTest.java**.

To use it, simply 

1- Create a custom test file  
1- Add the test command line and expected output in the `./src/test/resources/custom/multitest.config` file.


### Example

Let's imagine we want to try our `maxAlt` feature (issue #5) with a file `my-test-alt-1.csv` that contains only 1 line.
This line has the Altitude value set to `42`.
We then:

* Add our `my-test-alt-1.csv` file in the `./src/test/resources/custom/feature5/` folder

* Edit the multitest.config file to add our test:

```
# this line is a comment
# useful to know what the test is about!
# test 1: simple example for the maxAlt feature
cmd: -o maxAlt ./src/test/resources/custom/feature5/my-test-alt-1.csv
output:
42
---

```

* Run the MultiTest main program and check its outputs


### Config file

The goal is to complete this file as the project goes forward.
This is a simple solution to see if any new changes involve previous tests failure.
In the end, with an average of 5 tests / feature, this file should contain around 500 tests blocks.

A test is simply a series of lines including:

* a comment (starting with `#`)

* the command line to send to Pandora (starting with `cmd: `)

* the expected output (starting with `output:` and the output line(s) on a new line)

* an ending block `---`

```
# test X: a comment
cmd: -o <featureName> <file>
output:
<expected_output>
---

# test X+1: a comment
cmd: -o <featureName> <file>
output:
<expected_output>
---

etc.

```