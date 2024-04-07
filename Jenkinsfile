// pipeline {
//     agent any

//     stages {
//         stage('Checkout') {
//             steps {
//                 // Checkout your code from Git repository
//                 git branch: 'main', url: 'https://github.com/avivbs96/jenkins-selenium.git'
//             }
//         }
//         stage('Install Dependencies') {
//             steps {
//             // Install Python dependencies
//                 sh '/Users/Aviv/Desktop/python3-env/bin/pip install -r requirements.txt'
//             }
//         }

//         stage('Run Tests') {
//             steps {
//                 // Run pytest
//                 sh '/Users/Aviv/Desktop/python3-env/bin/pytest -s -m negative tests/'
//             }
//         }
//     }
// }

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
        stage('Generate HTML Report') {
            steps {
                // Generate HTML test report
                sh '/Users/Aviv/Desktop/python3-env/bin/pytest --html=reports/report.html'
            }
        }
        stage('Run Login Tests and Generate HTML Report') {
            steps {
                // Run login tests and generate HTML report
                sh '/Users/Aviv/Desktop/python3-env/bin/pytest -m login --html=reports/report.html'
            }
        }
    }
}
