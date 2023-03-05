pipeline{
    agent {label 'slave1'}
    
    stages{
       stage("build user") {
        steps{
              wrap([$class: 'BuildUser']) {
                sh 'echo ${BUILD_USER} >> result.csv'
                sh 'date >> result.csv '
                
  }
        }
  
  
}
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
                  sh '(time curl -v -k $(dig +short myip.opendns.com @resolver1.opendns.com):5000 2>&1 | grep OK)>> result.csv'
                //   sh 'echo $(curl -v --silent $(dig +short myip.opendns.com @resolver1.opendns.com):5000 2>&1 | grep OK ) >> result.csv'
                  sh 'curl -v $(dig +short myip.opendns.com @resolver1.opendns.com):5000 >> result.csv'
                //   sh 'sudo docker stop flaskapp1 && sudo docker rm flaskapp1'
                  

                 
                   
                  
                  
                  
 
              }
          }
          stage('aws_s3_upload'){
              steps{
                  withAWS(credentials:'aws-key', region:'us-east-1'){
                    s3Upload(bucket:'jenkins-sqlabs-amitb',path: 'project1/', includePathPattern:'result*')
                    sh 'rm -r result.csv'
              }
          }
          }
          }
}

