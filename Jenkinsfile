pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                cd app/
                docker image build -t cyware-test:latest -f Dockerfile .
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