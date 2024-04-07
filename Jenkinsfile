pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from Git repository
                git branch: 'main', url: 'https://github.com/avivbs96/jenkins-selenium.git'
            }
        }
        stage('Install Dependencies') {
            steps {
            // Install Python dependencies
                sh '/Users/Aviv/Desktop/python3-env/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest
                sh '/Users/Aviv/Desktop/python3-env/bin/pytest -s -m negative tests/'
            }
        }
    }
}
