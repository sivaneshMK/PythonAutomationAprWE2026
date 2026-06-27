pipeline{

        agent any

        environment {
        VENV = "venv"
        }

        stages{
            stage('Checkout'){
                steps{
                    git branch: "master", url: "https://github.com/sivaneshMK/PythonAutomationAprWE2026.git"
                }

            }
            stage('Setup Python Environment'){
                steps{
                    sh'''
                    python3 -m venv ${VENV}
                    .${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install requirements.txt

                    '''
                }
            }

        stage('Run Pytest'){

            steps{
                sh'''
                .${VENV}/bin/activate
                pytest --html=report.html --self-contained-html
                '''
            }
        }


    }

    post{
        always{
            archiveArtifacts artifacts: "report.html", fingerprint:true
        }
        failure{
            echo "Tests Failed"

        }

        success{
            echo "Test is Passed"

        }
    }

}