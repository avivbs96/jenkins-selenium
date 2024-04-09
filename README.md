
---

# Jenkins Selenium Pytest Project

This project contains automated tests using Selenium and Pytest, integrated with Jenkins for continuous integration.

## Jenkins Pipeline

The Jenkins pipeline consists of the following stages:

1. **Checkout**: Clones the code from the Git repository.
2. **Install Dependencies**: Installs Python dependencies from the `requirements.txt` file.
3. **Run Tests**: Executes Pytest for negative tests.
4. **Run Login Tests and Generate HTML Report**: Runs login tests and generates an HTML report.

```groovy
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/avivbs96/jenkins-selenium.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '/Users/Aviv/Desktop/python3-env/bin/pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh '/Users/Aviv/Desktop/python3-env/bin/pytest -s -m negative tests/'
            }
        }
        stage('Run Login Tests and Generate HTML Report') {
            steps {
                sh '/Users/Aviv/Desktop/python3-env/bin/pytest -m login tests/ --html=reports/report.html'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'reports/report.html', allowEmptyArchive: true
                }
            }
        }
    }
}
```

## Test Scenarios

### Positive Scenarios

The `TestPositiveScenarios` class contains a positive login test scenario:

- It navigates to a webpage, fills in the login form with valid credentials, submits the form, and verifies successful login.

### Negative Scenarios

The `TestNegativeScenarios` class contains negative login test scenarios:

- It tests invalid username and password combinations to verify appropriate error messages.

