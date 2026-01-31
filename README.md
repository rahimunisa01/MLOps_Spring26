# MLOps Lab 01
This repository contains my solution for Lab 01 of the MLOps Spring 2026 course. The purpose of this lab was to get comfortable with writing basic Python code, adding unit tests, and setting up automated testing using GitHub Actions.

#What this project does
The project implements a small calculator module with a few basic arithmetic operations. While the logic itself is simple, the main focus of this lab was on:
organizing the project properly,
writing tests using different testing frameworks, and
making sure tests run automatically whenever code is pushed to GitHub.


#Project structure
```
MLOps_Spring26/
├── src/
│   └── calculator.py
├── test/
│   ├── test_pytest.py
│   └── test_unittest.py
├── .github/workflows/
│   ├── pytest_action.yml
│   └── unittest_action.yml
├── requirements.txt
└── README.md
```

#Calculator functions
The calculator.py file includes four functions:
fun1(x, y) adds two numbers
fun2(x, y) subtracts y from x
fun3(x, y) multiplies x and y
fun4(x, y) returns the combined result of the above three functions

#Testing
This project uses two testing frameworks:
Pytest – tests are written as simple functions using assert
Unittest – tests are written using classes and assertEqual
All calculator functions are tested using both frameworks.
To run tests locally:

```
pytest
python -m unittest test.test_unittest
```

#GitHub Actions
GitHub Actions is used to automatically run tests whenever code is pushed to the main branch.
There are two workflows:
one for pytest
one for unittest
This ensures that any changes pushed to the repository are tested in a clean environment and that broken code does not go unnoticed.

#Final status
All tests pass locally
All GitHub Actions workflows pass successfully
The repository follows basic MLOps and CI best practices
