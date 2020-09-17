pipeline {
    agent any

    stages {
        stage('Init') {
            sh """
            env | sh
            sh 'gauge --version
            # FIXME: Figure out why `gauge install ...` in Dockefile doesn't stick
            gauge install python
            gauge install html-report
            gauge install json-report
            gauge install xml-report

            pipenv install
            """
        }

        stage('Test') {
            sh 'pipenv shell && gauge run'
        }
    }
}