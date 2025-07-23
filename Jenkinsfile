pipeline {
    agent any
    stages {
        // stage('Run Tests') {
        //     steps {
        //         bat 'python -m unittest test_calculator.py'
        //     }
        // }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t calculator-app .'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                bat 'docker run --rm calculator-app'
            }
        }
    }
}
