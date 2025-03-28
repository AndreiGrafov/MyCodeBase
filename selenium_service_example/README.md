# **Service Example**
## **Overview**
Occasionally, I received requests to perform **non-standard automation tasks**. To handle these cases, I developed a **universal framework** that allows flexible automation solutions **without burdening a project with excessive test dependencies**.

Since such services are often integrated into **CI/CD pipelines**, this folder contains:

- **Small utility scripts** for quick execution.
- **Dockerfile** – Typically created by the service developers and modified by DevOps specialists for server adaptation.
## **Repository Structure**
### src/
- **Page classes** – Standard folder containing web pages.
- **Base class** – Includes action methods such as click, scroll, refresh, etc.
- **Locators** – Defined and stored within the application class.
- **Application class** – Replaces the usual conftest file for service configuration.
### check\_site.py
- This is the **runner file** for executing the service.
- Originally, the service was designed to check various website components.
### controller.py
- Acts as a **transitional class** where additional functionality can be extended.
### scraper.py
- The **core logic of the service** resides here.
- The current implementation is **somewhat bulky** and could be logically split for better structure.
- However, at the time of development, the **priority was rapid implementation over refinement**.

This repository serves as a reference for building **flexible automation services** that can be integrated into **CI/CD workflows** while maintaining adaptability and efficiency.

