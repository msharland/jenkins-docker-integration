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
                echo 'Testing..'
                //script {
                //}
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                //script {
                //}
            }
        }
    }
}