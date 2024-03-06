# Test Driven Development

Test-Driven Development (TDD) is a software development approach in which tests are written before the actual code that needs to be implemented. The TDD process typically follows these steps, often referred to as the "Red-Green-Refactor" cycle:

1. **Red: Write a Failing Test**
    - Before writing any code, you write a test that should validate a new feature. In the Pandora project that would be one of the features described in the issues. This initial test should fail (Most test suites output the failing test in red, hence Red) since the corresponding code hasn't been implemented yet.
    - [Commit](Conventional%20Commits) that test (test: add a test for feature X)
2. **Green: Write the Minimum Code to Pass the Test**
    - You then write the minimum amount of code necessary to make the test pass. The focus is on making the test successful.
    - commit your code (feat: implement feature X)
3. **Refactor: Improve Code Without Changing Functionality**
    - After the test has passed, you should refactor the code to improve its structure, readability, or performance without making the test fails (nor previous tests).
    - Commit the changes (e.g. refactor: improve feature X by skipping empty row or docs: add [Javadoc](Javadoc) to function Y)

Add the meaningful change to your [Changelog](Changelog), if your team feel that it has done enough change create a new [release](Semantic-Versioning#)

The primary benefits of TDD include:

- **Early Detection of Bugs:** Since tests are written before the code, any deviations from expected behavior are immediately identified, making it easier to catch and fix bugs early in the development process.
    
- **Code Confidence:** The comprehensive suite of tests provides a safety net, allowing developers to make changes and refactor code with confidence, knowing that existing functionality won't break unnoticed.
    
- **Improved Design:** TDD often leads to more modular and maintainable code as developers focus on writing code that is testable and easily adaptable.
    
- **Documentation:** The tests serve as executable documentation, providing insights into the expected behavior of the code.

While TDD can be a powerful approach, it requires discipline and a shift in mindset for developers. Writing tests before code can feel counterintuitive to some, but the benefits in terms of code quality, maintainability, and bug prevention can be significant. TDD is commonly associated with agile and iterative development methodologies.
