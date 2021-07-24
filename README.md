# SCA-Cloud-School-Application

My Jenkins server can be accessed here ```http://52.188.157.63:8080/``` 
> **Username**: ```CloudTask``` **Password**: ```Password_01```


##  Jenkins pipeline syntax used for defining JenkinsFile

An alternative to creating and configuring a job using the jenkins user interface is defining or scripting the pipeline in a code. A **Jenkinsfile** is simply a scripted pipeline.

The Jenkinsfile can be written as a scripted or declarative pipeline. The declarative syntax which I'll be explaining is easier to get started with and has a predefined structure. 

Since we will are using a declarative pipeline, we do not need to include our source in the Jenkinsfile. This is because on the Jenkins interface, we can choose Git as our SCM and input our repository URL and script path.

You will create a Jenkinsfile in your repository with your code. 

### Stages 

```groovy
pipeline {
    
    agent any

    stages {
         
          stage("build") {

               steps {
                   ** code goes here **
               }
          }
          stage("test") {

               steps {
                   ** code goes here **
               }
          }
          stage("deploy") {
               
               steps {
                   ** code goes here **
               }
          }
     }
}
```

#### Explanation
Each step contains scripts that execute on the jenkins server or jenkins agent.

On line 1 ```pipeline``` just shows that you're declaring a pipeline

On line 2 ```agent any``` means that this build can run on any jenkins agent

On line 3 ```stages``` is where the whole work happens. You can define as many stages as you want. Here, I defined three stages:

The **build** stage contains your build scripts. For example if you're building a javascript application, things like your ```npm install``` and ```npm build``` script will  go in here. 
The **test** stage contains your test scripts. And the **deploy** stage contains your deployment scripts.

