# **Automation Testing**
## **Overview**
This folder contains various code implementations for **UI and API automation testing**, collected over several years of hands-on experience in multiple projects.
## **API Testing**
For API testing, the **Requests** library was used. The test structure is divided into two parts:

- **APIs** – Request implementation.
- **api\_tests** – Test execution.

All implementations are based on an abstract example: **"kitchen"**.
## **UI Testing**
The UI test structure follows the **Page Object Model (POM)** pattern and includes:
### POM/
- **Setup files** – Test data setup via API.
- **Page classes** – Representations of web pages under test.
- **Locator file** – Centralized repository for element locators.
- **Base class (base.py)** – Contains common interaction methods (click, read, close, etc.).
### tests/
- **Executable test files** – Concise sequences of test execution steps.
- **Configuration file (conftest.py)** – Defines test execution parameters:
  - Window settings
  - Resolution
  - Plugins usage
  - Authentication details
## **Configuration**
The config.py file stores:

- Constants with test data
- URLs of tested pages
- Other configuration settings

**Important:** In real projects, sensitive test data should be stored in an **encrypted database** instead of plain configuration files.

