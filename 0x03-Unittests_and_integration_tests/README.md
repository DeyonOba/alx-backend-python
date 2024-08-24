# 0x03. Unittests and Integration Tests


The [`unittest`][1] unit test is python framework that was originally inspired by JUnit and has a similar flavor as major other unit testing frameworks in other languages. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.


Here a some object-oriented way [`unittest`][1] is been support in Python.

- **test fixture**:
> A test fixture represents the preparation needed to perform one or more tests, and any associated cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.
- **test case**:
> A test case is the individual unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.
- **test suite**:
> A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.
**test runner**:
> A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests.

[1]: <https://docs.python.org/3/library/unittest.html> "Python unittest documentation"

## Classes and functions

This section describes in depth the API of [`unitest`][1].

[**Test Cases**][2]:

`class unittest.TestCase(methodName='runTest')`

[TestCase][2] represents the logical test units in the `unittest` universe. This class is intended to be used as a base class, with specific tests being implemented by concrete subclasses. This class implements the interface needed by gthe test runner to allow it to drive the tests, and methods that the test code can use to check for and report various kinds of failure.

Each [TestCase][2] instance will run a single base method called `methodName`, with the default `methodName` been `runTest()` method.

[`TestCase`][2] instances provides three groups of methods: one group used to run the test, another used by the test implementation to check conditions and report failures, and some inquiry methods allowing information about the test itself to be gathered.


[2]: <https://docs.python.org/3/library/unittest.html#unittest.TestCase> ("Python test cases documentation")
