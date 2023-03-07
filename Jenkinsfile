pipeline{
    agent {label 'slave1'}
    
    stages{
       stage("build user") {
        steps{
              wrap([$class: 'BuildUser']) {
                sh 'echo ${BUILD_USER} >> result.json'
                sh 'date >> result.json '
                
  }
        }
  
  
}
          stage("Git_Clone"){
              steps{
                  git branch: 'main', url: 'https://github.com/NextGen20/flaskproject.git'
                  
              }
          }
                stage('Build and Run image'){
                    steps{
                         sh 'sudo docker build -t flaskproject/project1:latest .'
                         sh 'sudo docker run --name flaskapp1 -d -p 5000:5000 flaskproject/project1:latest'
                    }
          }
          stage("UniTest") {
    steps {
        script {
            def USER
            STATUS = sh(script: "curl -v \$(dig +short myip.opendns.com @resolver1.opendns.com):5000 | grep \" 200 OK\" | tr -d \"\\r\\n\"", returnStdout: true).trim()
            sh 'curl -I $(dig +short myip.opendns.com @resolver1.opendns.com):5000 | grep "HTTP/1.1 200 OK" >> result.json'
            
            withAWS(credentials: 'aws-key', region: 'us-east-1') {
            sh "aws dynamodb put-item --table-name result --item '{\"User\": {\"S\": \"${BUILD_USER}\"}, \"Date\": {\"S\": \"date\"}, \"TEST_RESULT\": {\"S\": \"${STATUS}\"}}'"
            }
        }
    }
      }
          stage('Aws_S3_Upload'){
              steps{
                  withAWS(credentials:'aws-key', region:'us-east-1'){
                    s3Upload(bucket:'jenkins-sqlabs-amitb',path: 'project1/', includePathPattern:'result*')
                    sh 'rm -r result.json'
              }
          }
          }
          }
}

