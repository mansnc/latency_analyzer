pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your Git repository
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Build your Latency Analyzer tool (if applicable)
            }
        }

        stage('Run Script') {
            steps {
                // Execute the latency_measurement.py script
                sh 'python3 main.py'
            }
        }
    }
}
