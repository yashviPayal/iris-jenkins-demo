
pipeline {
    agent any

    environment {
        PYTHON_EXE = 'C:\\Users\\yashv\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Source code checked out from GitHub by Jenkins.'
            }
        }

        stage('Check Python and Git') {
            steps {
                bat '"%PYTHON_EXE%" --version'
                bat 'git --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '"%PYTHON_EXE%" -m venv .venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '".venv\\Scripts\\python.exe" -m pip install --upgrade pip'
                bat '".venv\\Scripts\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Iris Application') {
            steps {
                bat '".venv\\Scripts\\python.exe" app.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat '".venv\\Scripts\\python.exe" -m unittest -v'
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: GitHub Iris pipeline completed!'
        }
        failure {
            echo 'FAILED: Check the first failed stage in Console Output.'
        }
    }
}
