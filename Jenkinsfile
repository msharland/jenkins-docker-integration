pipeline {
    agent any

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
                sh "docker --version"
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