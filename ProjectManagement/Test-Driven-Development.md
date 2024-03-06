# Test Driven Development

Test-Driven Development (TDD) is a software development approach in which tests are written before the actual code that needs to be implemented. The TDD process typically follows these steps, often referred to as the "Red-Green-Refactor" cycle:

1. **Red: Write a Failing Test**
    - Before writing any code, you write a test that should validate a new feature. In the Pandora project that would be one of the features described in the issues. This initial test should fail (Most test suites output the failing test in red, hence Red) since the corresponding code hasn't been implemented yet.
    - [Commit](Conventional%20Commits) that test (test: add a test for feature X)
2. **Green: Write the Minimum Code to Pass the Test**
    - You then write the minimum amount of code necessary to make the test pass. The focus is on making the test successful.
    - commit your code (```feat: implement feature X```)
3. **Refactor: Improve Code Without Changing Functionality**
    - After the test has passed, you should refactor the code to improve its structure, readability, or performance without making the test fail (nor previous tests).
    - Commit the changes (e.g. ```refactor: improve feature X by skipping empty row``` or ```docs: add [Javadoc](Javadoc) to function Y```)

Add the meaningful change to your [Changelog](ProjectManagement/Changelog.md), if your team feel that it has done enough change create a new [release](Semantic-Versioning#)

There are several strategies and kind of tests you could develop to test your project:

**Black Box Testing:** Black Box Testing is a fundamental testing methodology in Test-Driven Development (TDD) that centers on evaluating the external functionality of a software application without delving into its internal code structure. In this approach, you treat the software as an opaque entity, focusing solely on inputs and observing outputs, akin to a "black box" where the internal workings remain concealed. The primary objective of Black Box Testing is to validate that the software behaves according to specified requirements and meets its intended functionality.

**White Box Testing:** In contrast to Black Box Testing, White Box Testing, also known as clear box or structural testing, delves into the internal logic and code structure of the software. You write these tests after you have written the code, based on what kind of data structure or code logic you have written. (e.g. you have used an array, and you index ```i, i+1 and i+2``` you deduce that your current code works only if there are at least three elements, you write a new test convering the edge case (for example a case where there are two elements, you are now in the red))

In addition to White Box and Black Box Testing, you can also classify tests in two categories Unit Tests and Integration Tests.

**Unit Tests:** Unit Tests target individual units or components of the software often focusing on isolated functions or methods. The objective is to verify that each unit performs as expected in isolation, facilitating early detection of defects and supporting modular development practices. Unit Tests are crucial in TDD, acting as the building blocks for validating the correctness of the smallest units of code. Unit tests need to be integrated in the source code, generally as additional test classes in Java.

**Integration Tests:** Integration Tests assess the collaboration and interaction between different components or modules within a software system. These tests ensure that various units work seamlessly together when integrated, revealing potential issues that may arise during the assembly of different parts. Integration Tests play a pivotal role in validating the overall system architecture and its ability to function cohesively as a unified whole. In our case it means testing the system from an outside perspective once it is compiled, answering the question of does pandora.jar behaves as expected.

Read more about Test-Driven-Development on the[ wikipedia page](https://en.wikipedia.org/wiki/Test-driven_development)

# In the Pandora Project

For the Pandora project you are encouraged to experiment as much as possible with Test-Driven-Development.

- Your final grade is influenced by Black Box Integration Test that are run automatically on the code you push on Github when you do a [Release](Release.md).

**We require however that you produce Black Box Integration Tests for all the features you develop** by completing the file ```test/testSuite.json``` and adding corresponding flight records into the ```test/resources``` folder.

the **testSuite** should respect the following schema

```json 
[
	testDescription,
	...
	testDescription
]
```

a **test description** should respect the following schema

```json 
{
    "id": <uniqueId:number>,
    "feature": <feature:string>,
    "milestone": <milestone:number>,
    "mode": <"full"|"feature">,  
    "file": <flightRecordPath:Path>,
    "result": <expectedResult:number|string>
}
```

The fields of a test description are

- **id**: a unique number in your testSuite
- **feature**: the feature your are testing, this should be the exact name that is passed to the ```-o``` option. e.g. ```maxAlt```
- **milestone**: the number of the milestone corresponding to the feature you are testing. For Grouping purposes in the output
- **mode**:
	- feature: test with the -o set to the given feature
	- full: generate the full report and parse it to find the feature in the report
- **file**: the file passed to pandora, the path should be relative to the overall project ```test/resources/.../flight.frd```
- **result**: the expected result. Currently, the autograder is in strict comparison.
