# Runnable_test

This directory contains a working version of the code with a demonstration test.

## Test Description

The test demonstrates basic form filling, option selection, and verifies the success of the test by checking the alert text.

## Prerequisites

* Python 3.x
* pytest
* Selenium WebDriver (e.g., ChromeDriver for Chrome)

## Installation

1. Clone the repository.
2. Navigate to the `runnable_test` directory.

## Running the Tests

1. Change the current directory to the `test` directory:

   ```bash
   cd test

2. Run the tests using pytest:

   ```bash
   pytest test_example.py

**Running in Headless Mode**

To run the tests in headless mode (without opening a browser window), modify the headless variable in the conftest.py file:

1. Open the conftest.py file.
1. Change the value of headless to 1.
1. Run the tests as described above.

**Example**

The test performs the following steps:

1. Opens a web page.
1. Fills in form fields.
1. Selects options from dropdowns or radio buttons.
1. Submits the form.
1. Verifies the alert message for successful submission.

**Notes**

- Ensure that the necessary dependencies are installed before running the tests.
- The WebDriver path should be correctly configured in the conftest.py file.
- The test is designed for demonstration purposes and may need to be adapted for specific use cases.

