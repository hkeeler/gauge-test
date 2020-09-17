pipeline {
    agent any

    stages {
        stage('Init') {
            steps {
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
        }

        stage('Test') {
            steps {
                // FIXME: Can't run browser tests yet since login to
                //        AWS Console is still done by hand.
                sh 'pipenv shell && gauge run --tags "\\!browser"'
            }
        }
    }
}