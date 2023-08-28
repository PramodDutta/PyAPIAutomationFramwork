# Python API Automation Framework

###  Integration Test cases for the Restful Booker
URL - https://restful-booker.herokuapp.com/apidoc/index.html

1. Verify GET, POST, PACTH, DELETE, PUT
2. Response Body, Headers, Status Code.
2. Auth - Basic Auth, Cookie Based Auth.
3. JSON Schema Validation.

<img width="948" alt="Screenshot 2023-08-28 at 5 34 39 PM" src="https://github.com/PramodDutta/PyAPIAutomationFramwork/assets/1409610/98e85a62-00fc-4c97-bb42-3f2ab998dcfa">


###  Tech Stack (Python Packages used)
1. Python, Request Module
2. PyTest, PyTest-html
3. Allure Report
4. Faker, CSV, JSON, YAML.
5. Run via Commandline - Jenkins

#### P.S - DB Connection(in future)

## Install pip packkes
- ` pip install requests pytest pytest-html faker allure-pytest jsonschema`
- `pip install requirements.txt`

## How to run Locally and see the Report?
`` pytest tests/* -s -v --alluredir=./reports --html=report.html
``

## How to Run via Jenkins? 

<img width="861" alt="Screenshot 2023-08-28 at 5 34 52 PM" src="https://github.com/PramodDutta/PyAPIAutomationFramwork/assets/1409610/e6cf19cd-68bd-4e7b-ab78-28472232efc3">
