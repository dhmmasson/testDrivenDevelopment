# Advanced Programming

This is the wiki for the Estia Advanced Programming class.

# Educational Goals of the Class

- Start and manage a software development project following some Agile project management 
  - Organize [features](Pandora/Features.md) to be developed
  - Set up milestones to reach
- Follow a [Test-Driven-Development](ProjectManagement/TestDrivenDevelopment/Test-Driven-Development.md) approach to develop software
  - Write tests before writing the code to implement a feature
  - Make sure that all tests are passing before releasing a new version of the software
  - Make sure that all code is covered by tests
- Use of a version control system

# Evaluation

You must implement **Pandora v2** according to the [man page](Pandora/Pandora.md) and the [Features](Pandora/Features.md) specification.

## Group Grade

### Implementation (tests)

Your program will be run against the teacher's test suite. Grading is based on:

- **How many tests you pass**: there are multiple tests per feature and CLI option. Each test consists in a text-based comparison between your program's output and the reference output.  
  Make sure to follow the [output format instructions](Pandora/Constants.md) precisely.
- **Performance**: your program will be run against long flight record files and must execute as fast as possible. Avoid unnecessary computation and I/O.
- **Code quality**: no dead code. Test coverage should reach the vast majority of your codebase.

### Development Process

You are graded on the quality of your development workflow:

- Use of [Conventional Commits](ProjectManagement/Versioning/Conventional-Commits.md) for all commits
- Proper [Semantic Versioning](ProjectManagement/Versioning/Semantic-Versioning.md) for each release tag
- A maintained [CHANGELOG](ProjectManagement/Versioning/Keep-A-Changelog.md) following the Keep a Changelog format

### Test-Driven Development

You must produce a test suite (`test/testSuite.json`) that:

- **Validates your own implementation**: at least one test per feature and per CLI option
- **Discriminates other projects**: other groups' programs will be run against your test suite. Your results should agree with the teacher's — if a team passes or fails a feature, your test suite should detect it consistently
- **Covers your code**: your tests should exercise most of your implementation

## Individual Grade

- Contribute at least **30% of the group's commits**
- At least **50% of your commits** (excluding merge commits) follow [Conventional Commits](ProjectManagement/Versioning/Conventional-Commits.md)
- **QCM during the last session** — individual written assessment on the course content

# Pandora - a Flight Data Recorder Analyzer

Pandora is a tool to analyze flight record data to provide summary and high-level information based on low-level sensor data (e.g., fighter jet position).

## Project Description

Planes are equipped with [Flight Recorder](https://en.wikipedia.org/wiki/Flight_recorder) or **black box** to track many parameters during a flight to help during the investigation of accident. This project aims to emulate a software that would read and extract information from the flight data recorder.  
We will in this class take some liberties on how the data are stored and extracted to simplify the process.

### Flight Data Records

Records about a flight will be stored in a text file. Specifications can be found [here](Pandora/Flight-Records.md)

### Flight Analysis

The tool will produce multiple flight analyses depending on the `output` option it receives as a Command Line Option. It can:

- Compute and display a single value (e.g., average altitude during the whole flight), as well as multiple values (e.g., a full report)
- Consider a `single file` (e.g., the average altitude of a given flight), `several files` (e.g., the average altitude of each flight), and `multiple files` (e.g., the maximum average altitude of a flight among others).

### Features to Develop

Features are represented by issues open in your git repository. They are organized according to milestones. A list of features and [here](Pandora/Features.md)

## First Steps

1. \<group action\> Copy the [Issues](ProjectManagement/Issues.md) corresponding to the [Features](Pandora/Features.md) to implement on your Github repository.
2. Clone the project locally on each member computer
3. Open the project with your java editor of choice [Eclipse](tools/Eclipse.md) or [vscode](tools/vscode.md) and run the maven build script to compile the bare version of the project (a program that output "pandora@v1.0.0")
4. Read the wiki documentation about
	1. what is [Test-Driven-Development](ProjectManagement/TestDrivenDevelopment/Test-Driven-Development.md)
	2. What are conventional Commits
