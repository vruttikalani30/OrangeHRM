# Selenium with Python Automation Framework

This is an automation framework created using Selenium with Python and pytest. This framework can be used to automate web applications and run tests efficiently.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Reporting](#reporting)

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python:** Install Python 3.6+ from [here](https://www.python.org/downloads/).
- **pip:** Install pip, the Python package installer, from [here](https://pip.pypa.io/en/stable/installation/).
- **Git:** Install Git from [here](https://git-scm.com/downloads).
- **IDE:** Use an Integrated Development Environment (IDE) such as PyCharm, VS Code, or any other preferred IDE.

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/selenium-pytest-framework.git
    cd selenium-pytest-framework
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

The project follows a standard structure:

- `tests`: Contains test case files.
- `pages`: Contains Page Object Model (POM) classes.
- `utils`: Contains utility files, such as configuration and browser setup.
- `conftest.py`: Contains pytest fixtures.
- `requirements.txt`: Lists project dependencies.
- `pytest.ini`: Configuration file for pytest.

## Usage

### Configurations

- **Config File:**
    - Create a `config.py` file in the `utils` directory.
    - Add necessary configurations like URLs, credentials, browser settings, etc.

### Writing Tests

1. **Page Object Model (POM):**
    - Create a Python class for each web page under the `pages` directory.
    - Define web elements and methods to interact with them.

2. **Test Cases:**
    - Create a test class under the `tests` directory.
    - Write test methods using pytest.

Example Test Class:

```python
import pytest
from pages.login_page import LoginPage

def test_valid_login(browser):
    login_page = LoginPage(browser)
    login_page.login("username", "password")
    assert login_page.is_logged_in()


## Running Tests

pytest
pytest tests/test_login.py
pytest tests/test_login.py::test_valid_login

## Reporting

pytest Reports:

By default, pytest generates output in the terminal.
Additional Reporting:

Integrate additional reporting tools like pytest-html or Allure for advanced reporting.
To install pytest-html:

bash
Copy code
pip install pytest-html
To generate an HTML report:

bash
Copy code
pytest --html=report.html


Happy Testing! 🚀
