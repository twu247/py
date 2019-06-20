pipeline{
	agent any
	stages{
		stage('Build'){
			steps{
				echo "Build";
				git 'https://github.com/twu247/py.git'
				sh "python hw.py"
			}
		}
		stage('Test'){
			steps{
				echo "Test";
				sh 'python -m unittest hw_test'
			}
		}
		stage('Deploy'){
			steps{
				echo "Deploy";
			}
		}

	}
	post{
		always{
			echo "Always";
		}
		success{
			echo "Success";
		}
		failure{
			echo "Failure";
		}
	}
}
