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
                // Build your Latency Analyzer tool
                script {
                    def buildOutput = sh(script: 'your_build_command_here', returnStatus: true)
                    if (buildOutput == 0) {
                        echo 'Build succeeded'
                    } else {
                        error 'Build failed'
                    }
                }
            }
        }

        // Add more stages (e.g., test, deploy) as needed
    }

    post {
        always {
            // Perform cleanup or other final actions
        }
    }
}
