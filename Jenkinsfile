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
        stage('Lint') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 app.py'
            }
        }
        stage('Build Docker') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }
        stage('Deploy Container') {
            steps {
                sh 'docker rm -f $IMAGE_NAME || true'
                sh 'docker run -d --name $IMAGE_NAME -p 5000:5000 $IMAGE_NAME'
            }
        }
        stage('Selenium Test') {
            steps {
                sh 'pip install selenium'
                sh 'python tests/test_home.py'
                sh 'python tests/test_route.py'
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

