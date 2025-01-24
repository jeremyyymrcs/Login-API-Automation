# SeleniumBase Automation Framework

This is a robust **Selenium-based Automation Framework** designed for testing web applications. It is built using *
*Python**, **SeleniumBase**, **Pytest**, and other supporting libraries. The framework follows the **Page Object Model
** (POM) design pattern, ensuring modular and reusable code. It supports advanced features such as **Multi-Factor
Authentication (MFA)**, **HTML Reports**, and **Screenshots** for better debugging and reporting.

## Features

- **Page Object Model (POM)**: Organize tests for better readability, maintainability, and scalability.
- **Modular Design**: Reusable page classes for various web pages.
- **MFA Support**: Supports login functionality using **TOTP codes**.
- **Test Automation**: Automated tests for sign-up, login, and other functionality.
- **HTML Reporting**: Automated HTML reports are generated for each test run.
- **Screenshots**: Automatically captures screenshots on test failure for debugging.
- **Flexible Configuration**: Easily configurable through a configuration file.
- **Easy Integration**: Can be integrated with other tools or CI/CD pipelines.

---

## Prerequisites

Before you begin, ensure you have the following tools installed:

1. **Python 3.x**: Ensure that Python 3.x is installed on your system. You can download it
   from [python.org](https://www.python.org/).
2. **Pip**: Python’s package installer, which is included with Python 3.x.
3. **Selenium**: Web automation library.
4. **SeleniumBase**: Extends Selenium WebDriver to make automated testing easier.
5. **Pytest**: Framework for running the tests and managing test cases.
6. **Browser Drivers**: Ensure you have the appropriate driver for the browser (e.g., ChromeDriver for Chrome).

---

## Installation

1. **Clone the repository**:

```bash
git clone repository_url
```

2. **Open your command-line interface (e.g., Command Prompt or Terminal). Navigate to the project directory using the cd
   command**:

```bash
cd path/to/ProjectDirectory
```

3. **Create a Virtual Environment**:

```bash
python -m venv venv
```

4**Activate the Virtual Environment**:

```bash
venv\Scripts\activate
```

5**Install the required Python packages from the requirements.txt file using pip**:

```bash
pip install -r requirements.txt
```

## Running the login test

*Once you’ve installed the dependencies, you can run the automated tests with Pytest.*:

```bash
cd tests
pytest test_login.py -s -q -x --dashboard --html=report.html --maximize --screenshot --rs
```

*Run the tests in demo mode (optional):*

```bash
pytest test_login.py -s -q -x --dashboard --html=report.html --maximize --screenshot --rs --demo
```

## Framework Overview

### `data/`

- This directory stores data files, such as those containing TOTP codes or any other testing data required.

### `pages/`

- **Page Object Model (POM)** classes are stored here. Each file represents a different page on the web application
  being tested.
    - `home_page.py`: Contains the Home Page class and related functions.
    - `login_page.py`: Contains the Login Page class and related functions.
    - `sign_up_page.py`: Contains the Sign-Up Page class and related functions.

### `configurations/`

- This folder contains configuration files that help in reading URLs, credentials, and other environment settings.
    - `config_reader.py`: A Python script used to load configuration details.

### `tests/`

- This folder holds all the test scripts for the project.
    - `test_login.py`: This script contains tests specifically for the Login functionality of the application.

### `utilities/`

- This folder includes utility functions that can be reused across the project.
    - `custom_logging.py`: Custom logger configuration to manage logging during test execution.

### `requirements.txt`

- This file contains a list of all the required Python packages and dependencies needed to run the project.

# Test Flow

## Overview

The test framework follows a flow that covers user sign-up, login, and validation. Below is the breakdown of the
process:

### 1. **Sign Up**

- The first test case retrieves the secret key (TOTP code) and saves it in a file for further use.
- This step ensures that the test can generate or fetch the required authentication code for subsequent login attempts.

### 2. **Login**

- The framework supports login tests using **both dynamic and static TOTP codes**.
    - **Dynamic TOTP Codes**: These are codes that change every few seconds and are generated from the secret key.
    - **Static TOTP Codes**: These are pre-generated codes, used for testing purposes in situations where dynamic code
      generation is not required.

### 3. **Validation**

- Tests validate the **login functionality**, ensuring that the application behaves as expected.
    - **Successful Login**: Validates that correct credentials, including the correct TOTP code, allow the user to log
      in.
    - **Failed Login**: Tests scenarios where incorrect credentials or an invalid TOTP code result in a failed login
      attempt.
## GitHub Actions CI/CD

This repository includes pre-configured **GitHub Actions** workflows to automatically run the tests in a continuous integration/continuous deployment (CI/CD) pipeline.

The workflow will run the tests on every push to the repository and generate a report upon completion. Here’s what it includes:

- **Test execution on each commit**: Every push to the repository triggers the workflow to run tests.
- **Automated HTML report generation**: After each test run, an HTML report is generated, which includes detailed test results and screenshots in case of failure.
- **Notifications and logging**: The results are logged in GitHub Actions with notifications for success or failure.
- **Environment setup**: The GitHub Action automatically sets up the necessary Python environment, installs dependencies, and executes the tests.

You can find the GitHub Actions workflow file in the `.github/workflows/` directory.


# Video Demonstration

![demo_video.gif](demo_video.gif)

## Summary

This test flow covers essential functionalities for user authentication, including sign-up, login, and validation of
successful/failed login attempts.

