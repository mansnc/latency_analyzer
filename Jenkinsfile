pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your Git repository
                checkout scm
            }
        }

        stage('Run Script') {
            steps {
                // Execute the main.py script
                bat 'start python main.py'
            }
        }
    }
}
