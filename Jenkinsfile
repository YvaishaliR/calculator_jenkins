pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        S3_BUCKET = 'calculator-jenkins' 
        AWS_DEFAULT_REGION = 'eu-north-1'
    }

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt || true'
            }
        }

        stage('Run Unit Tests') {
            steps {
                sh 'python -m unittest test_calculator.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t calculator-app .'
            }
        }

        stage('Run Tests in Docker') {
            steps {
                sh 'docker run --rm calculator-app'
            }
        }

        stage('Deploy with AWS SAM') {
            steps {
                withCredentials([[
                    $class: 'AmazonWebServicesCredentialsBinding',
                    credentialsId: 'aws-creds'  
                ]]) {
                    sh '''
                        pip install aws-sam-cli
                        sam build
                        sam package \
                          --s3-bucket $S3_BUCKET \
                          --output-template-file packaged.yaml
                        sam deploy \
                          --template-file packaged.yaml \
                          --stack-name calculator-stack \
                          --capabilities CAPABILITY_IAM
                    '''
                }
            }
        }
    }
}
