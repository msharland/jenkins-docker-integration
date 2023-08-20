pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh "cd app/"
                sh "docker image build -t cyware-test:latest -f Dockerfile ."
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}