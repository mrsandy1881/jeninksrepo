pipeline {
    agent any

    stages {
        stage('downloadcode/ checkout code') {
            steps {
                checkout scm
            }
        }
        stage('downloadcode/ checkout codeshow python version') {
            steps {
                "python3 --version"
            }
        }

        stage('run python program') {
            steps {
                sh "python3 read.py"
            }
        }
    }
}