pipeline{
    agent {label 'slave1'}
    environment {
    TIME = sh(script: 'date "+%Y-%m-%d %H:%M:%S"', returnStdout: true).trim()
     
      }
    
    stages{

          stage("Git_Clone"){
              steps{
                  git branch: 'main', url: 'https://github.com/NextGen20/flaskproject.git'
                  
              }
          }
                stage('Build & Run image'){
                    steps{
                         sh 'sudo docker build -t flaskproject/project1:latest .'
                         sh 'sudo docker run --name flaskapp1 -d -p 5000:5000 flaskproject/project1:latest'
                    }
          }
         stage("Unitest & DynamoDB") {
    steps {
        script {
           STATUS = sh(script: "curl -I \$(dig +short myip.opendns.com @resolver1.opendns.com):5000 | grep \"HTTP/1.1 200 OK\" | tr -d \"\\r\\n\"", returnStdout: true).trim()
             sh 'echo "$STATUS" >> result.json'
             sh 'echo "$TIME" >> result.json'
            withAWS(credentials: 'aws-key', region: 'us-east-1') {
            sh "aws dynamodb put-item --table-name result --item '{\"User\": {\"S\": \"${BUILD_USER_ID}\"}, \"Date\": {\"S\": \"${TIME}\"}, \"TEST_RESULT\": {\"S\": \"${STATUS}\"}}'"
            }
            
        }
    }
      }
          stage('Aws_S3_Upload'){
              steps{
                  withAWS(credentials:'aws-key', region:'us-east-1'){
                    s3Upload(bucket:'jenkins-sqlabs-amitb',path: 'project1/', includePathPattern:'result*')
                    
              }
          }
          }
          stage('Stop&Clean&Logfile'){
            steps{
            sh 'sudo docker stop flaskapp1 && sudo docker rm flaskapp1'
            sh 'result.json >> Logfile.txt'
            sh 'rm -r result.json'
            }
           
            
          }
          
}

}