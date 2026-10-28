pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo 'Jenkins has retrieved the GitHub project.'
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
                bat 'git --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m venv .venv'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Iris Application') {
            steps {
                bat '.venv\\Scripts\\python.exe app.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m unittest -v'
            }
        }
    }

    post {
        success {
            echo 'GitHub Iris pipeline completed successfully!'
        }

        failure {
            echo 'GitHub Iris pipeline failed. Check the console output.'
        }
    }
}