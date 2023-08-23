pipeline {
    agent any

    // Environment Variables set in Jenkins Global Environment Variables
    environment {
        AWS_DEFAULT_REGION = "us-east-2"
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${REPO_NAME}"
    }
    
    stages {
        stage('Docker Build and Docker Tag') {
            steps {
                echo 'Building and Tag ...'
                script {
                  //sh "cd app/"
                  sh '''
                    docker image build -t my-app:latest -f Dockerfile .
                    docker tag my-app:latest ${REPOSITORY_URI}:latest
                  '''
                }
            }
        }
        stage('Docker Push') {
            steps {
                echo 'Pushing ...'
                script {
                sh '''
                  aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com
                  docker push ${REPOSITORY_URI}:latest
                '''
                }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying ...'
                script {
                sh '''
                    aws ecs create-service \
                        --cluster ECS \
                        --service-name cyware \
                        --task-definition cyware \
                        --desired-count 1"
                '''
                }
            }
        }
    }
}