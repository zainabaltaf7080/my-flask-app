pipeline {
    agent any
    environment {
        IMAGE_NAME = "flask-app"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                sh '''
                #!/bin/bash
                python3 -m venv venv
                source venv/bin/activate
                pip install --upgrade pip
                pip install flake8 selenium flask
                '''
            }
        }
        stage('Lint') {
            steps {
                sh '''
                #!/bin/bash
                source venv/bin/activate
                flake8 app.py
                '''
            }
        }
        stage('Build Docker') {
            steps {
                sh '''
                docker build -t $IMAGE_NAME .
                '''
            }
        }
        stage('Deploy Container') {
            steps {
                sh '''
                docker rm -f $IMAGE_NAME || true
                docker run -d --name $IMAGE_NAME -p 5000:5000 $IMAGE_NAME
                '''
            }
        }
        stage('Selenium Test') {
            steps {
                sh '''
                #!/bin/bash
                source venv/bin/activate
                python tests/test_home.py
                python tests/test_route.py
                '''
            }
        }
    }
    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}


