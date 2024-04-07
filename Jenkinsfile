pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout your code from Git repository
                git url: 'https://github.com/avivbs96/jenkins-selenium.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Run pytest
                sh 'pytest -s -m negative tests/'
            }
        }
    }

    post {
        always {
            // Clean up or post-processing steps
        }
    }
}
