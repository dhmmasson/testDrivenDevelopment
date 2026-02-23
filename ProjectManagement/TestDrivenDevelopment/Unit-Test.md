# Unit-Test

Unit tests are released into the code repository along with the code they test.  
 Unit Tests target individual units or components of the software often focusing on isolated functions or methods. The objective is to verify that each unit performs as expected in isolation, facilitating early detection of defects and supporting modular development practices. Unit Tests are crucial in TDD, acting as the building blocks for validating the correctness of the smallest units of code. Unit tests need to be integrated in the source code, generally as additional test classes in Java.

## Properties

1. A unit test executes fast — _blazing fast!_ Sub-millisecond, please.
2. A unit test can be executed concurrently without affecting other tests.
3. A unit test should not utilize resources from the outside world.
    - **No file system access**.
    - No web service calls.
    - No e-mails.
    - No cross-thread communication.
    - No cross-process communication.
    - No SQL and no database connectivity.
4. A unit tests verifies the _public behavior_ of that unit conforms to a requirement.

In the java project you can write them in the ```src/test/java/``` folder.
