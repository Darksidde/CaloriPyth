pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    bat 'docker build -t food-calculator-app .'
                }
            }
        }

        stage('Push Image to Hub') {
            steps {
                withCredentials([string(credentialsId: 'dockerhub-pwd', variable: 'dockerhubpwd')]) {
                    bat 'docker login -u darksiddee -p %dockerhubpwd%'
                    bat 'docker push darksiddee/devops-integration'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    bat 'docker run food-calculator-app'
                    // Buraya test adımlarını ekleyebilirsiniz, örneğin: unittest, pytest vb.
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    withSonarQubeEnv('SonarQubeServer') {
                        bat 'sonar-scanner'
                        // Burada SonarQube analizini başlatan adımları yapabilirsiniz
                    }
                }
            }
        }
    }
}
