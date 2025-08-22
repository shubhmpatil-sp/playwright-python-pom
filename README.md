# Playwright Python POM Framework

This repository contains a **Page Object Model (POM)** based test automation framework using **Playwright** and **Pytest** in Python.  
It is designed for scalability, readability, and easy maintenance of UI test scripts.
---
## Features
- Built with **Python + Pytest + Playwright**
- **Page Object Model (POM)** design for clean separation of locators & test logic
- Reusable utilities and fixtures
- Supports **cross-browser testing** (Chromium, Firefox, WebKit)
- Test reports with **pytest-html / Allure Reports**
- Easily extensible for CI/CD (GitHub Actions, Jenkins, etc.)

---

## Installation & Setup

### 1. Clone the repository
```
git clone git@github.com:shubhmpatil-sp/playwright-python-pom.git
cd playwright-python-pom
```
### 2. Create virtual environment & install dependencies
```
python -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Install Playwright browsers
```
playwright install
```
## Running Tests
#### Run all tests
```
pytest
```
#### Run tests with headed browser
```
pytest --headed
```
#### Run tests in specific browser
```
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```
## Reports
#### Generate a simple HTML report:
```
pytest --html=report.html
```
Or use Allure:
```
pytest --alluredir=allure-results
allure serve allure-results
```
