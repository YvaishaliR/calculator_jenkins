pipeline {
    agent any
    stages {
        stage('Run Tests') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }
    }
}
