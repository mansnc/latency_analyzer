pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                bat 'echo Building...'
				bat 'C:\\msys64\\mingw64\\bin\\python.exe main.py'
            }
        }

        stage('Test') {
            steps {
                bat 'echo Testing...'
            }
        }

        stage('Deploy') {
            steps {
                bat 'echo Deploying...'
            }
        }
    }
}