pipeline {
    agent any

    stages {
        stage('Checkout from Git') {
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

        stage('Test Latency Measurement Module') {
            steps {
                bat 'echo Testing...'
				bat 'C:\\msys64\\mingw64\\bin\\python.exe unittest_measure_latency.py'
            }
        }

        //stage('Deploy') {
        //    steps {
        //        bat 'echo Deploying...'
        //    }
        //}
    }
}
