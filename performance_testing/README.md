# **Performance Testing**
## **Overview**
Performance testing was not my primary focus in projects; however, I was occasionally tasked with preparing tests to evaluate various metrics. For Python-based performance testing, **Locust** proved to be a highly suitable tool.
## **Testing Process**
The testing workflow typically involved:

- **User login**
- **Triggering various API calls**
- **Cleaning up test-generated data** (if applicable)

To effectively measure performance, the process needed to be executed in parallel with **hundreds or even thousands** of concurrent users.
## **Repository Structure**
This repository contains essential code snippets that helped implement such tests.
### config.py
- Stores constant values used across tests.
### generate\_users.py
- Uses API calls to create a test user database.
- Automating this step was crucial, as manually creating accounts would have been extremely tedious.
### several\_accounts.py
- Contains the base test logic.
- Initially designed to run with a **single user** before scaling to multiple users.
- The provided code is a **non-executable** example, as it uses fictional API endpoints and test data.

This repository serves as a reference for setting up performance tests with **Locust** and implementing scalable testing strategies.

