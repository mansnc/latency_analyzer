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

        //stage('Docker Build') {
            //steps {
                //script {
                    //docker.build("latency-analyzer:1.0", "-f Dockerfile .")
                //}
            //}
        //}

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
