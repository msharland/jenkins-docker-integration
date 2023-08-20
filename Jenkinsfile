pipeline {
    agent any
    // Environment Variables set in Jenkins Global Environment Variables
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                script {
                  //sh "cd app/"
                  sh "docker image build -t my-app -f Dockerfile ."
                  //sh "docker tag "
                }
            }
        }
        stage('Test') {
            steps {
                echo 'Pushing..'
                script {
                sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
                sh "docker push my-app"
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