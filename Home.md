# Advanced Programming
This is the wiki for the Estia Advanced Programming class.
> **Outline**
- [Advanced Programming](#advanced-programming)
  * [Educational Goals of the class](#educational-goals-of-the-class)
- [Pandora - a flight data recorder analyser](#pandora---a-flight-data-recorder-analyser)
  * [Project description](#project-description)
    + [Flight data records](#flight-data-records)
    + [Flight Analysis](#flight-analysis)
    + [Features to develop](#features-to-develop)

***
## Educational Goals of the class
* Start and manage a software development project following some Agile project management principles
  * Organize [features](./Features) to be developed
  * set up [milestone](./project-management:Milestones) to reach  
* Use of a version control system.

## Evaluation
You will be automatically evaluated based on how many functionalities you developed and how many milestones you managed to complete.
Fairly simple: To get a passing grade (E), you need to complete at least 2 milestones. The more milestones you complete after that, the better your grade.

You can check by yourself how many tests your program passed or failed every time you will commit your current version on GitHub.
A Continuous Integration is set up in your git repository. This means that the tests will check if your new version passes new tests, but also previous ones (to prevent regression). The tests simply consist in a text-based comparison between: 
 
 * The output your program generates (e.g. java -jar pandora.jar -o avgAltitude file1.dfr ==> 1234.56) and,
 * The output of our program for the same test. 

If it is different, someone has an error. Make sure to follow the [instructions](./Instructions)




# Pandora - a flight data recorder analyzer
Pandora is a tool to analyze flight record data to provide information to the operating company.

## Project description

Planes are equipped with [Flight Recorder](https://en.wikipedia.org/wiki/Flight_recorder) or **black box** to track many parameters during a flight to help during the investigation of accident. This project aims to emulate a software that would read and extract information from the flight data recorder.
We will in this class take some liberties on how the data are stored and extracted to simplify the process.

### Flight data records
Records about a flight will be store in a text file. Specifications can be found [here](./Flight-Records)
### Flight Analysis  
the tool will produce multiple flight analyses depending on the input flight records it is working on.
* Basic Flight Analysis
* Incident Flight Analysis  
*

### Features to develop
A list of complete features to be integrated can be found [here](./Features)
