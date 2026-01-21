Step 1: Create Virtual Environment

Step 2: Create calculator.py in src Folder

Step 3: Create tests using Pytest and Unittests

Write test cases in test_*.py file

Run Pytest tests:
```
pytest test_pytest.py
```

Run Unittest tests:
```
python test_unittest.py
```

Step 4: Implement Github Actions


Github can perform actions based on events like pushing code to main branch, merge pull request or create new issue. This actions are nothing but a series of steps defined in the workflow file

**pytest_action.yml**

-   Workflow Name: "Testing with Pytest"
-   Event Trigger: It specifies the event which triggers this workflow. It triggers when code is pushed to the main branch/ triggers when new issue is opened or an existing issue is labeled/ runs workflow whenever new label is created in the repo
-   Jobs: The workflow has single job which runs on Ubuntu Linux machine
-   Steps:
    1.  Checkout code: copy code from repo to github runner machine using actions/checkout@v4.
    2.  SetupPython: It sets up the Python environment using actions/setup-python@v4 and specifies Python version 3.8.
    3.  Install Dependencies: This step installs the project dependencies by running pip install -r requirements.txt.
    4.  Run Tests and Generate XML Report: The core testing step runs Pytest with the --junitxml flag to generate an XML report named pytest-report.xml. The continue-on-error: false setting ensures that the workflow will be marked as failed if any test fails.
    5.  Upload Test Results: In this step, the generated XML report is uploaded as an artifact using actions/upload-artifact@v2. The name of the artifact is "test-results," and the path to the report is specified as pytest-report.xml.
    6.  Notify on Success and Failure: These two steps use conditional logic to notify based on the outcome of the tests.
    7.  if: success() checks if the tests passed successfully and runs the "Tests passed successfully" message.
    8.  if: failure() checks if the tests failed and runs the "Tests failed" message.


**unittest_action.yml**

-   Workflow Name: "Testing with Unittest"
-   Event: Trigger workflow when new code is pushed to main branch
-   Jobs: Workflow will run on Ubuntu-Linux Machine
-   Steps:
    1.  Checkout code
    2.  Install Python version
    3.  Install dependencies
    4.  Run unit tests
    5.  Notify on success
    6.  Notify on failure