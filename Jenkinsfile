pipeline {
    agent any

    stages {
        stage('Checkout from streamlit github repository') {
             steps {
                echo 'Someone pushed to this repo!'
                git branch: 'main', url: 'https://github.com/maiasmoly/streamlit_app'
                sh 'ls -l'
            }
       } 
        stage('Build') {
            steps {
                googleCloudBuild  credentialsId: 'friendly-vigil-414000', source: local('.'), request: file('cloudbuild.yaml')
            }        

        }
   }
}