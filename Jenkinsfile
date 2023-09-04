pipeline {
    agent any

    stages {
        stage('Checkout from Git') {
            steps {
                checkout scm
            }
        }
		

		stage('Setup Packages') {
			steps {
				// Install Required Packages
				bat 'check_packages_windows.bat'
		}


        stage('Build Ping-Latency-Measure') {
            steps {
                bat 'echo Building main_run_ping.py'
                bat 'C:\\msys64\\mingw64\\bin\\python.exe main_run_ping.py'
            }
        }

        stage('Build Scapy-Latency-Measure') {
            steps {
                bat 'echo Building main_run_scapy.py'
                bat 'C:\\msys64\\mingw64\\bin\\python.exe main_run_scapy.py'
            }
        }

        stage('Build Main()') {
            steps {
                bat 'echo Building main.py'
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

        stage('Test Ping Latency Module') {
            steps {
                bat 'echo Testing Ping Latency Module'
				bat 'C:\\msys64\\mingw64\\bin\\python.exe unittest_measure_latency_ping.py'
            }
        }

        stage('Test Scapy Latency Module') {
            steps {
                bat 'echo Testing Scapy Latency Module'
				bat 'C:\\msys64\\mingw64\\bin\\python.exe unittest_measure_latency_scapy.py'
            }
        }

        //stage('Deploy') {
        //    steps {
        //        bat 'echo Deploying...'
        //    }
        //}
    }
}
