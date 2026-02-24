# Test Driven Development

Test-Driven Development (TDD) is a software development approach in which tests are written before the actual code that needs to be implemented. The TDD process typically follows these steps, often referred to as the "Red-Green-Refactor" cycle:

1. **Red: Write a Failing Test**
    - Before writing any code, you write a test that should validate a new feature. In the Pandora project that would be one of the features described in the issues. This initial test should fail (Most test suites output the failing test in red, hence Red) since the corresponding code hasn't been implemented yet.
    - [Commit](../Versioning/Conventional-Commits.md) that test (test: add a test for feature X)
2. **Green: Write the Minimum Code to Pass the Test**
    - You then write the minimum amount of code necessary to make the test pass. The focus is on making the test successful.
    - commit your code (```feat: implement feature X```)
3. **Refactor: Improve Code Without Changing Functionality**
    - After the test has passed, you should refactor the code to improve its structure, readability, or performance without making the test fail (nor previous tests).
    - Commit the changes (e.g. ```refactor: improve feature X by skipping empty row``` or ```docs: add [Javadoc](../Javadoc.md) to function Y```)

Add the meaningful change to your [Keep-A-Changelog](../Versioning/Keep-A-Changelog.md), if your team feel that it has done enough change create a new [release](../Versioning/Semantic-Versioning.md)

There are several strategies and kind of tests you could develop to test your project:

**Black Box Testing:** Black Box Testing is a fundamental testing methodology in Test-Driven Development (TDD) that centers on evaluating the external functionality of a software application without delving into its internal code structure. In this approach, you treat the software as an opaque entity, focusing solely on inputs and observing outputs, akin to a "black box" where the internal workings remain concealed. The primary objective of Black Box Testing is to validate that the software behaves according to specified requirements and meets its intended functionality.

**White Box Testing:** In contrast to Black Box Testing, White Box Testing, also known as clear box or structural testing, delves into the internal logic and code structure of the software. You write these tests after you have written the code, based on what kind of data structure or code logic you have written. (e.g. you have used an array, and you index ```i, i+1 and i+2``` you deduce that your current code works only if there are at least three elements, you write a new test convering the edge case (for example a case where there are two elements, you are now in the red))

In addition to White Box and Black Box Testing, you can also classify tests in two categories Unit Tests and Integration Tests.

**[Unit Test](Unit-Test.md)s:** Unit Tests target individual units or components of the software often focusing on isolated functions or methods. The objective is to verify that each unit performs as expected in isolation, facilitating early detection of defects and supporting modular development practices. Unit Tests are crucial in TDD, acting as the building blocks for validating the correctness of the smallest units of code. Unit tests need to be integrated in the source code, generally as additional test classes in Java.

**Integration Tests:** Integration Tests assess the collaboration and interaction between different components or modules within a software system. These tests ensure that various units work seamlessly together when integrated, revealing potential issues that may arise during the assembly of different parts. Integration Tests play a pivotal role in validating the overall system architecture and its ability to function cohesively as a unified whole. In our case it means testing the system from an outside perspective once it is compiled, answering the question of does pandora.jar behaves as expected.

Read more about Test-Driven-Development on the[ wikipedia page](https://en.wikipedia.org/wiki/Test-driven_development)

# In the Pandora Project

For the Pandora project you are encouraged to experiment as much as possible with Test-Driven-Development.

- Your final grade is influenced by Black Box Integration Tests. When you do a [Release](../Versioning/Release.md), the teacher team will pull your project and run the test suite.

## Automated Tests

Running tests manually quickly becomes impractical. Instead, you should automate them from the start using the `test/autograder.py` script provided in the starter pack.

There are **no automated tests on GitHub** — no CI pipeline, no GitHub Actions. Instead, the teacher team will **regularly pull your repository** and run:

- the **teacher's own test suite** against your `pandora.jar`
- **your test suite** against other teams' `pandora.jar`

This means the quality and coverage of `test/testSuite.json` is part of your final evaluation. A test suite that catches real bugs in other teams' projects is rewarded.

### Running Tests Locally

Use `test/autograder.py` for all features. See the [TestSuite & Autograder](TestSuite.md) page for the full usage, all options, and how to write your `test/testSuite.json`.

```bash
python test/autograder.py -t test/testSuite.json -m manifest.json target/pandora.jar
```

# See Also

An interesting discussion on stackexchange about unit-tests that sparks a lot of discussion on tests and test driven development:  
<https://softwareengineering.stackexchange.com/questions/452449/how-do-unit-tests-facilitate-refactoring-without-introducing-regressions>
