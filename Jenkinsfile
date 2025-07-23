pipeline {
    agent any
    stages {
        stage('Run Tests') {
            steps {
                bat 'python -m unittest test_calculator.py'
            }
        }
    }
}
