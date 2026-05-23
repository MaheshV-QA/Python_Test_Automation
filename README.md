# Python Test Automation Project

## Overview

This repository contains Python learning examples, API testing scripts, Selenium automation examples, Appium mobile testing, and Pytest-based test cases.

## Project Structure

- `Notes/` - study notes and interview materials.
- `Python/` - Python examples and interview-practice scripts.
- `Python_API_Testing/` - sample API scripts using `requests`.
- `Python_Appium_MobileTesting/` - Appium mobile automation examples.
- `Python_Interview_Coding/` - coding interview practice problems.
- `Python_Pytest/` - Pytest automation framework, page objects, utilities, and sample tests.
- `Python_Selenium_Automation/` - Selenium automation demos.

## Setup

1. Install Python 3.10+.
2. From the repository root, install dependencies:

```bash
pip install -r requirements.txt
```

## Run Pytest

From the repository root, run:

```bash
pytest
```

To select a browser:

```bash
pytest --browser chrome
pytest --browser firefox
pytest --browser edge
```

## Notes

- `Python_Pytest/utilities/Browser_setup.py` now cleans up browser sessions with a yield fixture.
- `Python_Pytest/utilities/ReadProperties.py` loads config relative to its own location.
- `Python_Pytest/Testcases/Test_Login.py` now uses the fixture instance correctly.
- `Python_API_Testing/swagger/Get.py` now uses a reusable function and a main guard.

## Recommended next steps

- Add more Pytest test cases and page objects.
- Add a root-level `pytest.ini` or root `Python_Pytest/__init__.py` if you want package-style imports.
- Use `pytest-html` or `allure` for richer reports.
