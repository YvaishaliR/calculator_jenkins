pipeline {
    agent any
    stages {
        stage('Run Tests') {
            steps {
                bat 'python3 -m unittest test_calculator.py'
            }
        }
    }
}
