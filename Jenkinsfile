pipeline{
    agent {label 'slave1'}
    
    stages{
          stage("Git_Clone"){
              steps{
                  git branch: 'main', url: 'https://github.com/NextGen20/flaskproject.git'
                  
              }
          }
                stage('Build image'){
                    steps{
                         sh 'sudo docker build -t flaskproject/project1:latest .'
                    }
          }
          stage('UnieTest'){
              steps{
                  
                  
                  sh 'sudo docker run --name flaskapp1 -d -p 5000:5000 flaskproject/project1:latest'
                  sh 'sudo docker ps'
//                   sh 'curl -v --no-tcp-nodelay $(dig +short myip.opendns.com @resolver1.opendns.com):5000 > result.csv'
//                   sh 'date >> result.csv && ${BUILD_USER_FIRST_NAME} >> result.csv '
//                   sh 'sudo docker stop flaskapp1 && sudo docker rm flaskapp1'
                   
                  
                  
                  
                  
              }
          }
          stage('aws_s3_upload'){
              steps{
                  withAWS(credentials:'aws-key', region:'us-east-1'){
                    s3Upload(bucket:'jenkins-sqlabs-amitb',path: 'project1/', includePathPattern:'result*')
              }
          }
          }
          }
}
