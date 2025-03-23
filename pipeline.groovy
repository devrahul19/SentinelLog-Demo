pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t sentinel-log .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker run -d sentinel-log'
            }
        }
    }
}
