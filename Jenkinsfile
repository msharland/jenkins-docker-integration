pipeline {
    agent any
    environment {
        AWS_ACCOUNT_ID="12345"
        AWS_DEFAULT_REGION="us-east-2" 
        IMAGE_REPO_NAME="my-ecr"
        IMAGE_TAG="latest"
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
 }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                script {
                  //sh "cd app/"
                  sh "docker image build -t my-app:latest -f Dockerfile ."
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Pushing..'
                script {
                sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                script {
                sh "docker --version"
                }
            }
        }
    }
}