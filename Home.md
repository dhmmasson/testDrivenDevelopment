# Advanced Programming

This is the wiki for the Estia Advanced Programming class.

# Updates

Latest news here: [CHANGELOG](CHANGELOG)

> **Outline**

- [Advanced Programming](#advanced-programming)
  - [Educational Goals of the class](#educational-goals-of-the-class)
- [Pandora - a flight data recorder analyser](#pandora---a-flight-data-recorder-analyser)
  - [Project description](#project-description)
    - [Flight data records](#flight-data-records)
    - [Flight Analysis](#flight-analysis)
    - [Features to develop](#features-to-develop)

***

## Educational Goals of the Class

- Start and manage a software development project following some Agile project management and [Test-Driven-Development](Test-Driven-Development) principles
  - Organize [features](Features) to be developed
  - Set up [milestones](./project-management:Milestones) to reach  
- Use of a version control system

# Evaluation

You will be automatically evaluated based on

- Group Grade: How many functionalities you have developed:
	- **Minimum Required: 3 validated milestones**, meaning on the ```release``` branch at least 80% of the the tests for at least three milestones.
- Group Grade: Test Driven development:
	- **Minimum required:** On the ```release``` branch, the file ```test/testSuite.json``` contains valid tests for at least 3 milestones
- Group Grade: Number of Successful [Release](Release):
- Individual Contribution: You have made a meaningful and
	- **Minimum required:** At least 10% of the commits of your groups, at least 50% of them (excluding Merge commits) follow [Conventional Commits](Conventional%20Commits)

You can check by yourself how many tests your program passed or failed every time you [Release](Release) commit your current version on GitHub.  
A Continuous Integration is set up in your git repository. This means that the tests will check if your new version passes new tests, but also previous ones (to prevent regression). The tests simply consist in a text-based comparison between:

 - The output your program generates (e.g. java -jar pandora.jar -o avgAltitude file1.dfr ==> 1234.56) and,
 - The output of our program for the same test.

If it is different, someone has an error. Make sure to follow the [instructions](Constants). If you think our version is having a problem, do not hesitate to [open an issue](https://github.com/Estia-advanced-programming/pandora-public/issues) so that we can investigate further.

# Pandora - a Flight Data Recorder Analyzer

Pandora is a tool to analyze flight record data to provide summary and high-level information based on low-level sensor data (e.g., fighter jet position).

## Project Description

Planes are equipped with [Flight Recorder](https://en.wikipedia.org/wiki/Flight_recorder) or **black box** to track many parameters during a flight to help during the investigation of accident. This project aims to emulate a software that would read and extract information from the flight data recorder.  
We will in this class take some liberties on how the data are stored and extracted to simplify the process.

### Flight Data Records

Records about a flight will be stored in a text file. Specifications can be found [here](Flight-Records)

### Flight Analysis

The tool will produce multiple flight analyses depending on the `output` option it receives as a Command Line Option. It can:

- Compute and display a single value (e.g., average altitude during the whole flight), as well as multiple values (e.g., a full report)
- Consider a `single file` (e.g., the average altitude of a given flight), `several files` (e.g., the average altitude of each flight), and `multiple files` (e.g., the maximum average altitude of a flight among others).

### Features to Develop

Features are represented by issues open in your git repository. They are organized according to milestones. A list of features and milestones can be found [here](Features)

## First Steps

1. \<group action\> Copy the [Issues](Issues) corresponding to the [Features](Features) to implement on your Github repository.
2. Clone the project locally on each member computer
3. Open the project with your java editor of choice [Eclipse](Eclipse) or [vscode](vscode) and run the maven build script to compile the bare version of the project (a program that output "pandora@v1.0.0")
4. Read the wiki documentation about
	1. what is [Test-Driven-Development](Test-Driven-Development)
	2. What are conventional Commits
