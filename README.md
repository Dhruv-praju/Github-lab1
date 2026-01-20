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
    3.  