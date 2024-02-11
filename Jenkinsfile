pipeline {
    agent any

    stages {
        stage('Checkout from streamlit github repository') {
             steps {
                echo 'Someone pushed to this repo!'
                git branch: 'main', url: 'https://github.com/maiasmoly/streamlit_app'
                sh 'ls -l'
            } 
        stage('Build docker image from github dockerfile') {
             steps {
               sh 'docker build Dockerfile -t "streamlit-docker-img"'
               echo 'Successfully built docker image'
        }
    }
}

