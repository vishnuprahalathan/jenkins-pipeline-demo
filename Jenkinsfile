pipeline {
    agent any

    environment {
        IMAGE_NAME = 'my-python-app'
    }

    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/vishnuprahalathan/jenkins-pipeline-demo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(IMAGE_NAME)
                }
            }
        }

        stage('Test') {
            steps {
                sh 'python -m unittest discover tests'
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying application..."
                sh "docker run -d -p 5000:5000 ${IMAGE_NAME}"
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution finished.'
        }
    }
}
