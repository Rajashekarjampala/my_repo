

# AIM :
    CI/CD Automation ~ Using Docker and Kubernetes build agents for Jenkins

# PRE-REQUISITES:    
    - Kubernetes cluster
    - Docker
    - Jenkins server
    - SCM Tool- Bitbucket
    - Java-11
    - Docker plugin
    - Kubernetes plugin
    - Bitbucke plugin


# DEFINATION OF DONE : 
    - K8S agents need persistent storage to use as cache (e.g. cloned git repository to speed up next job). 
    - HostPath storage driver could be used.
   
# SECTIONS:    
    # SECTION 1 :
        # How to install Jenkins using docker? 

        STEP 1:
            - Pull the Jenkins image using from the docker hub.
                docker pull jenkins/jenkins:lts

            - To check jenkins image is downloaded or not   
                docker images

        STEP 2:
            - Run the docker container by using jenkins image, jenkins default port is 8080
                docker run --rm -d --name vudejenkins -p 8080:8080 -p 50000:50000 jenkins/jenkins
            
            - List of docker containers by fallowing below command
                docker ps -a    

            - Access the Docker container by running the following command
                docker exec -it <container_id> /bin/bash

            - To find jenkins administrator password by running the below commands
                cat /var/jenkins_home/secrets/initialAdminPassword

            - Below command also we can find the jenkins administrator password  
                docker logs <container-id>

    # SECTION 2 :
        # How to Install Jenkins on Kubernetes?

        STEP 1 :
            - Create a name space :
            - First, we need to create the namespace  
                kubectl create namespace <namespace-name>  

            - Name space is created or not we use the below command 
                kubectl get ns

        STEP 2:
            - Next, create the YAML file that will deploy Jenkins:

            - Create and open a new file called jenkins.yaml using vi editor
            - Now add the code to define the Jenkins image, its port, and several more configurations
            - For the code we can find the Example section
            - This YAML file creates a deployment using the Jenkins image and also opens port 8080
            - You use these ports to access to the Jenkins and accept connections.

            - Now create this deployment in the respective namespace
                kubectl create -f <jenkins.yaml> -n <namespace>

            - Use below command to verify the pod’s state
                kubectl get pods -n <namespace>
        
        STEP 3 :
            - Create servive for the jenkins :

            - you need to expose it using a Service. You will use the NodePort Service type
            - Create and open a new file called jenkins-service.yaml
                vi <jenkins-service.yml>

            - Add the following code to define the NodePort Service,find the code in example section
            - You define your NodePort Service and then expose port of the Jenkins pod to port

            - Now create the Service in the same namespace
                kubectl create -f <jenkins-service.yaml> -n <namespace>

            - Check that the Service is running or not
                kubectl get services -n <namespace>

        STEP 4 :
            - Bring up deployment and services by using shell functions :

            function deployment() {
                echo "Bring up Deployment => START"
                kubectl apply -f <</opt/vude/assignments/ci-cd-jenkins/build-agents/specs/deployments/start.yml>>
                echo "Deployment ACTIVE => DONE"
            }       

            function svcs() {
                echo "Bring up Service => START"
                kubectl apply -f <</opt/vude/assignments/ci-cd-jenkins/build-agents/specs/services/start.yml>>
                echo "Service ACTIVE  => DONE"    
            }

            function main() {
                deployment
                svcs
            }        

        STEP 5 :
            - Accessing the Jenkins UI :
            - In this step, you will access and explore the Jenkins UI
            - Our NodePort service is accessible on port across the cluster nodes 
            - To take the VM exernal IP and nodeport IP
            - Now open a web browser and navigate to <VM exernal IP>:<port>
            - A page will appear asking for an administrator password

        STEP 6 :
        - Then we need to login pod :

            - Login the pod pod by using below command
                kubectl exec -it <podname> -n <namespace> -- bash  
        
            - Find the below command for jenkins administrator password
                cat /var/jenkins_home/secrets/initialAdminPassword        

    # SECTION 3 :
        # How to integrate jenkins with bitbucket?

        STEP 1:
            - Now we have to create the bitbucket server for SCM tool
            - Create Repo using Bitbucket:

            - First, you need a BitBucket account. Register and login to BitBucket
            - Create repository in the bitbucket server
            - Create a project and add the project name. Give a name for your repository. 
            - I am choosing this as a private repository

        STEP 2:
            - Install the Bitbucket plugin in Jenkins:

            - Log in to the Jenkins server and go to Manage Jenkins->Manage plugins
            - Then search for the BitBucket plugin and Install without restart the plugin.
    
        STEP 3:
            -  Create New Job in Jenkins and connect BitBucket Repo:
        
            - New Item to create a new Jenkins job
            - Then give a name for the Jenkins job. And then select FreeStyle Project
            - Then go to the Source Code Management section.and select the repository type bitbucket repository.
            - Then give the Bitbucket repo in the Repository URL.
            - Add->Jenkins to pass the username and password of the Bitbucket.
            - In the Build Trigger section, To select Build when a change is pushed to BitBucket and save it

    # SECTION 4 :
        # How to run a sample build by committing code in bit-bucket and triggering Jenkins?

        STEP 1:
            - Go to the Repository Setting page of your repo in the Bitbucket.
            - Then Go to the Webhooks section.Then give a name for this hook. 
            - Add your Jenkins URL in the URL inputs
        
        STEP 2:
            - Test the BitBucket and Jenkins Integration:

            - To test the integration, click the Build Now button in the Jenkins Job.
            - See the output using the console.
            - Everything works fine. So no error. If an error occurs, then build will show red color.
            - Whenever a new code is committed in the BitBucket,
            - Jenkins job will automatically create a new build each time.

    # SECTION 5 :
        # How to integrate Jenkins with docker?

        STEPS 
           - Go to your Jenkins dashboard and click Manage Jenkins.
           - Go to Manage Plugins. Search for Docker plugins and Install without restart button.
           - Once the installation is done, go to your job in the Jenkins dashboard.
           - In the job, when you go to the Build step, you can now see the option to start and stop containers.

    # SECTION 6 :
        # How to integrate Jenkins with K8s?

        STEP 1 : Go to your Jenkins dashboard and click Manage Jenkins.
        STEP 2 : Go to Manage Plugins. Search for kubernetes plugins and Install without restart button.
        STEP 3 : Within the Jenkins dashboard, select a Job and then select Configure.Then add build step.
        STEP 4 : To Select Deploy to Kubernetes, select the kubeconfig stored in Jenkins
        STEP 5 : Go to Kubernetes cloud configuration (kubeconfig)).Enter the kubeconfig content directly
        STEP 6 : Fill in the "Config Files" with the configuration file paths. 
        STEP 7 : By checking "Enable Variable Substitution in Config
        STEP 8 : Then provide the jenkins credentials like domin, kind, secret and Id
        STEP 9 : Configure the Jenkins URL Details like jenkins url and pod lebels

    # SECTION 7 :
        # How to write Declarative Pipeline?

        - First we need to install pipeline plugin as pipeline plugin

        STEP 1: 
            Pipeline:
            - All valid Declarative Pipelines must be enclosed within a pipeline block
                For example:

                pipeline {
        
                }
            - The top-level of the Pipeline must be a block, specifically: pipeline { }.
            
        STEP 2 : 
            Agent:
            - where you want buil the job is called agent
            - The agent section specifies where the entire Pipeline, or a specific stage
            - The section must be defined at the top-level inside the pipeline block
            - Execute the Pipeline, or stage, on any available agent. For example: agent any

              agent any {

              }

        STEP 3 : 
            Stages:    
            - Stages Containing a sequence of one or more stage directives
            - The stages section is where the bulk of the "work" described by a Pipeline will be located.  
            - At a minimum, it is recommended that stages contain at least one stage directive
            - For each discrete part of the continuous delivery process, such as Build, Test, and Deploy.

              stages { 
                stage('Example') {

                    }
                }  

        STEP 4 : 
            Steps:
            - The steps section defines a series of one or more steps to be executed in a given stage        
              directive.
            - The steps section must contain one or more steps.

            steps {
                echo 'Hello World'
            }    
                  
    # SECTION 8 :
        # How to write a scripted jenkins pipeline?

        - A Pipeline’s code defines your entire build process
        - which typically includes stages for building an application
        - jenkins scripted pipeline genarally we are using groovy language

        STEP 1 :
            Node :
            - The first block to be defined is the “node”:
            - A node is a machine which is part of the Jenkins environment and is capable of executing a Pipeline.
            node {

            }    

        STEP 2 :
            - The next required section is the “stage”
            - Each stage block specifies the tasks to be performed.
            - example- Build, Scm,Test and Deploy stages
            stage ('1'){            

            }

        STEP 3 :
            - A single task. Fundamentally, a step tells Jenkins what to do at a particular point/step in process
            - to execute the shell command make use the sh step
            - echo'hello world'

    # SECTION 9 :
        # How run jenkins job inside of docker containers?

        STEP 1 : 
            - Once installed, head over to Jenkins Dashboard –> Manage Jenkins –>Configure system

        STEP 2 : 
            - Under Configure System, there will be a section named cloud 
            - Manage Jenkins –> Manage Nodes and Clouds, Under docker you need to fill out the details
            - Replace “Docker URI” with your docker host IP. 
            - Test connection” to test if Jenkins is able to connect to the Docker host.

        STEP 3 : 
            - Now, from Docker Agent Template, Add Docker template.
            - fill in the details based on the the image    
            - Labels – Identification for the docker host. It will be used in the Job configuration
            - Name- Name of the docker template. Here we use the same name as label
            - The image that you created for the slave. Then give Home folder for the user you have created.
            - Credentials – add and enter the username and password that you have created for the docker image.
            - There are additional configurations like registry authentication and container settings.
            - You can also use JNLP-based slave agents. For this, the configurations need a little change
            - Primarily the docker image name and the connect method
            - if you want the workspace to be persistent, add a host volume path under container settings.

        STEP 4 :
            - Test Jenkins Build Inside a Docker container   
            - configurations ready, we will test the docker agent plugin using a freestyle job.
            - Create a freestyle job, select Restrict where this project can be run, select docker host
            - Add a shell build step which echoes a simple “Hello World“
            - If you have done all the configurations, builds the project.
            - With help of console output we can find buils job details.

    # SECTION 10 :
        # How run jenkins job inside of K8s PODS?

        STEP 1 : Go to Manage Jenkins –> Manage Plugins, search for Kubernetes Plugin and install it.
        STEP 2 : Once installed, go to Manage Jenkins –> Manage Node & Clouds, “Add a new Cloud” select Kubernetes.
        STEP 3 : Jenkins server running inside the same Kubernetes cluster
            - we have inside the Kubernetes cluster with a service account to deploy the agent pods, 
            - we don’t have to mention the Kubernetes URL or certificate key.

        STEP 4 :
            - we have to need to create one namespace and service account
              kubectl create namespace <NS-NAME>
              kubectl create serviceaccount <SA-NAME> -n <NS-NAME>

        STEP 5 :
            - Add button under credentials and create a credential type “Secret text“. 
            - Enter the service account token in the secret box and add other details as description
            - The kubernetes cloud configuration like kubernetes url, server certificates and namespace credentials

        STEP 6 : 
            - Create POD and Container Template    
            - Next, you need to add the POD template with the details, as Name, namespace, labels, container details

        STEP 7 : 
            - Go to Jenkins home –> New Item and create a freestyle project.
            - select Restrict where this project can be run and  label we assigned to the pod template. 
            - This way, it knows which pod template to use for the agent container.
            - Add a shell build step with an echo command to validate the job as "echo hello world"
            - Now, save the job configuration and click Build Now

    # SECTION 11 :
        # How to use kubernetes agents in Jenkins pipeline? 
        
        STEP 1 :
            # Kubernetes plugin and kubernetes cloud configuration :

            - Go to Manage Jenkins -> Manage Plugins, search for Kubernetes Plugin and install it.
            - Once install the kubernetes plugins then Fill in the Kubernetes plugin configuration.
            - Manage Jenkins -> Manage Nodes and Clouds -> Configure Clouds -> Add a new cloud -> Kubernetes
            - And enter the Kubernetes URL and Jenkins URL, 
            - You can use the kubernetes proxy like kubernetes server certificates key
            - You need create name kubernetes name space we can enter name space and credentials
            - Below commands to create name space and to get the name space 

                kubectl create name space <<name-space>>
                kubectl get namespace 
                
            - Then after you can run the test connection if it is fine you can go to kubernetes pod template.

        STEP 2 :     
            # Kubernetes Pod Template configuration :  

            - We need to configure the image that will be used to spin up the agent pod. 
            - Then we need to configure the pod template details, Under the kubernetes pod template section 
            - we can fill the like pod name, name space, label, etc...
            - Then we have fill the container template details like container name, docker image, working directory.

        STEP 3 :
            # Declarative Pipeline agent as kubernetes :

            - Basic syntax of declarative pipeline for run agent as kubernetes

            pipeline {
                agent {
                kubernetes {
                    ymlfile 'k8spod.yml'
                }
                }
                stages {
                steps{
                }
                }
            }

        STEP 4 :
            # Explanation of yml file for kubernetes agent :

            - Below Explanation showing to the example 1
            - In this scenario pipeline agent as kubernetes 
            - In the yml file defination for to cretate the a pod 
            - Run steps within a container by default.Steps will be container(name) {...} block instead of being 
              executed the maven container.
            - In this case we want to create container name of maven image using maven:alpine
            - In our job stage to run the maven job, Node is having container like maven 
            - This maven is map to the k8spod.yml file container name will be same 
            - In the steps we have to create the maven version, Steps are depends on our requirements  
            - If you have more steps, we have to add the steps under stages 
            - The next stage is we have to run the our job thats means build our job   

    # SECTION 12 : 
      # How to use docker agents in Jenkins pipeline? :

        STEP 1 :
            # Docker plugin and Docker cloud configuration :

            - Go to Manage Jenkins -> Manage Plugins, search for Docker and Docker pipeline Plugin and install it.
            - Manage Jenkins -> Manage Nodes and Clouds -> Configure Clouds -> Add a new cloud -> Docker
            - In the cloud configuration name as docker and Docker URL fill the your docker host IP  
            - Then we have to add docker server credentials and run test connection if test connecton is succsess
               we have to go with Docker Agent Template

        STEP 2 :
            # Docker Agent Template configuration :

            - Add Docker template and fill in the details based on the the image.
            - Labels - Identification for the docker host. It will be used in the Job configuration.
            - Name - Name of the docker template. Here we use the same name as label
            - Docker Image - The image that you created for the slave
            - Remote Filing System Root - Home folder for the user you have created like /home/jenkins.
            - Credentials - Add and enter the SSH username and password that you have created for the docker image.

        STEP 3 :
            # Declarative Pipeline agent as Docker : 

            - Basic syntax of declarative pipeline for run agent as Docker

            pipeline {
            agent {
                docker { image 'image' }
            }
            stages {
                stage ('test') {
                steps {
                    sh 'node --version'
                }
                }
            }
            }

        STEP 4 :
            # Explanation of Declarative pipeline for Docker agent :

            - In this case pipeline top level agent docker
            - Agent top level means all stages docker agent. Aspecially a container based on the node16:alpine image
            - We can use the image as node:16-alpine. We can take image is its depends on our requirement.
            - Here there is a stage part of pipeline node version (image version).
            - Here pipeline in the step we can find out image version
            - Under the stage we can write the steps and then we can create steps based on require.

            - Comming to the example number 5
            - The global level agent setup none. Here we have no agent to find at a global level
            - That means each stage we have define different containers definations
            - In the this case we can take the graddle image, Because of i have single static agent with docker on it. 
            - To run the container on the node specified at the top-level of the Pipeline, in the same workspace.
            - When we run this job we will expect the image pull from the dockerhub.
            - If you need more stages we can add the extra stages then we have to add the steps like clonerepo, build
            - In this example we have to find the graddle version it can mentined at the steps.

    # SECTION 13 :
        # New Trenton CI Implementation :
        # https://npsg-jira.elements.local/browse/CICD-257

        # What jobs Implementation do we have here :

            - Trenton ci instead manual we can use jenkins file like pipeline job
            - we know the create to create a what kind of job like job as HUD    
            - In the bitbucket we will create a repository under the repositoty to create branch
              like feature, master branches.
            - The devoloper commit the code like master branch/feature branch
            - Then we have to integrate jenkins with bitbucket
            - Create a pipeline job agents as docker
            - In the job we can give build tabs,emails,and pull request it will avaoid the confusion of developer
              and also give build parameter
            - The job implementation that means jenkins file stored in bitbucket
            - To setup the build trigger as every 4hours, If any changes in remote repository automatically 
              the code will be build trigger in every 4hours
            - The build trigger and unit test run parallel
            - If the build is successfull to merge the pull request    

        # Implementation Steps :
        # Jenkinsfiles location: https://npsg-bit.elements.local/projects/FSEDEV/repos/trenton/browse/hud/ci 

        STEP 1 :
            Entrypoint:
            - We can create Job by using parameters like Branch name, Build, Test, Promote, ent_ssd_test revision, 
              Pull request checks
            - If in case user selected Build, Test, Promote and there is no pull request to here.
            - Then we have to trigger the Main job by following above parameters

            Entrypoint-jenkinsfile :
            - Genarally A build parameter allows us to pass data into our Jenkins jobs
            - In the jenkins pipeline, first we need to pass the parameters like Build, Test, Promote, ent_ssd_test
              revision, Branch name, E-mail notifications
            - The Agent as built-in nothing but built-in node was renamed from "master node" to "built-in node" in  
              Jenkins
            - The main stages block contains a series of steps in a pipeline  
            - Then Triggers Main job with the above parameters
            - Then next step will be to clean up the work space
            - There is a way to clean up a workspace in Jenkins, clean up the workspace before or after build 
            - Then we have to build job with our required parameters

        STEP 2 :  
            Main job :
            - Here we have to trigger the like build and test job by required parameters and then we have to 
              do merge changes
            - Rquired parameters like WORKFLOW_TYPE, COMMIT_HASH, PULL_REQUEST_ID, EMAIL_LIST, BRANCH_NAME,
              UPSTREAM_BRANCH, SEND_EMAIL_NOTIFICATION, SEND_PULL_REQUEST_NOTIFICATION,SEND_BUILD_TAB_NOTIFICATION.
            - We can run the Triggers build, unit test jobs in parallel.
            - If the Merge pull request if it was successful or faile we have to set up the notification alert.

            Main job-jenkinsfile :
            - In the pipeline we can pass the parameters like WORKFLOW_TYPE,COMMIT_HASH,ENT_SSD_TEST_REVISION, 
              PULL_REQUEST_ID, etc...
            1.First stage will be pull request 
            - You can setup the environment step
            - We can use a agent as docker then add the image with arg

            2.second stage is code commit check and pull request    
            - Under the stage we can create steps one by one
            - Like cleanWorkspace, cloneRepository url, etc....

            3.Third stage will be Build and basic tests are run parallel
            - To build the code by using build steps like build stage   
            - Next stage will be code quality check under stage we can mention steps

            4.last stage will consider as merge stage    
            - In the Merge stage, Any changes from develop locally automatically build
            - Then next step is clean up the work place.
            - We can set up email alert post build like success or unsuccess and we can find via console output

        STEP 3 :
            Build, unit tests, code quality checks :
            - Clone the repository then if any merge changes locally the build is parallel like build,unit test, 
              code quality check
            - Then we have to push artifacts in to artifast storage
            - once done build we can set up the build notification
            - It is notified the the result of if is build success or fail then send to emils

            Build-Jenkins file :
            - In the build jenkins file first we need to pass the parameters
            - parameters like TRENTON_COMMIT_HASH, UPSTREAM_BUILD_NUMBER, ENT_SSD_TEST_REVISION etc...

            1.first will be Build firmware targets with agent is none
            - I describe the details I like to store in each build, how I capture these details,
            - And how I make them available to the firmware,and Configure the target
            - We can take agent as docker and under the steps we can use docker image and arg  

            2.second stage is run then we have to add build stage  
            - under the build stage we have to add the build steps,like target, node name, clean up workspace
              cloneRepository url, Build firmware

            3.Third stage will be to Publish artifacts  
            - The final stage is to publish the artifacts that means to copy the artifacts.
            - Then next step will be to run the build steps and then clean work space  

        STEP 4 :
            Code QualityChecks-jenkins file :
            - Here also we can pass the parameters in the pipeline like TRENTON_COMMIT_HASH,ENT_SSD_TEST_REVISION,
              UPSTREAM_BUILD_NUMBER, UPSTREAM_BRANCH
            - We can take agent as none and we can run the test casess parallale

            1.first stage will be run the test casess
            - This is the stage where you configure your CI/CD to execute the tests that are in your codebase.
            - Under the stage we can use agent as docker and we run steps for the image and arg
            - We can run the steps like to print The node name, cloneRepository and clean Workspace

            2.second stage Doxygen check
            - Then we can take docker as agent use docker image with arg
            - We can run the steps like to print The node name, cloneRepository and clean Workspace

            3.Third stage is stage Klocwork
            - Under the docker agent steps to clean the work space and use image and args   
            - We can run the steps like to print The node name, cloneRepository and clean up work space

        STEP 5 :
            - Maintenance jobs:  

            - NFS cleanup :

            - we can use storage type like NFS storage
            - Check how much space is used on NFS/other storage
            - If storage is more than 70% space used we can set the email alert
            - And then to clean the oldest artifacts from the artifacts repository

        STEP 6 :
            - nodes clean-up :

            - we need to remove jenkins work place from old files
            - we have to find old files and remove them and also clean nodes from old docker images
            - Find old workspaces and delete them
            - Delete old directories starting with git

        STEP 7 :     
            - Refresh reference clones : 

            - We need a job that will refresh local clones from time to time on all nodes.
            - Refresh reference clone and create new ones if do not exist
            - List of repositories should be easy to change              

    # SECTION 14 :     

        # Kubernetes agents can access local persistent storage :
        
        STEP 1 :
            - Kubernetes supports many types of storage class and volumes
            - In this scenario we can use the NFS storage class

            # create storageclass
                kubectl apply -f storage.yml -n <<namespace>>

            # get sc
                kubectl get sc

            # describe sc
                kubectl describe sc

            # delete sc
                kubectl delete sc <<scname>> -n <<namespace>>

        STEP 2 :
            - Create a hostPath PersistentVolume
            - In this section, we'll create a hostPath PersistentVolume
            - Kubernetes supports hostPath for development and testing on a single-node cluster
            - A hostPath PersistentVolume uses a file or directory on the Node to attached storage
            - Here is the configuration file for the hostPath PersistentVolume pv.yml

            # create pv
                kubectl apply -f pv.yml -n <<namespace>>

            # get pv
                kubectl get pv

            # describe pv
                kubectl describe pv vude-pv

            # delete pv 
                kubectl delete pv vude-pv -n <<namespace>>

        STEP 3 :
            - Create a PersistentVolumeClaim
            - Pods use PersistentVolumeClaims to request physical storage
            - In this section, we create a PersistentVolumeClaim that requests a volume of at least
              three gibibytes that can provide read-write access for at least one Node.
            - Here is the configuration file for the hostPath PersistentVolumeClaim pvc.yml  

            # create pvc
                kubectl apply -f pvc.yml -n <<namespace>>

            # get pvc
                kubectl get pvc -n <<namespace>>

            # describe pvc
                kubectl describe pvc vude-pvc -n <<namespace>>

            # delete pvc
                kubectl delete pvc vude-pvc -n <<namespace>>

            - After we created the PersistentVolumeClaim, If the control plane finds a suitable PersistentVolume
              with the same StorageClass, it binds the claim to the volume.  

        STEP 4 :   
            - Create a Pod uses PersistentVolumeClaim as a volume
            - Now it's time to create a Pod that uses our PersistentVolumeClaim as a volume.
            - To configuration file for the Pod looks like this pv-pod.yml

            # create pod
            kubectl apply -f pod.yml -n <<namespace>>

            # get pods
            kubectl get pods pod.yml -n <<namespace>>

            # describe pod
            kubectl describe pod pod.yml -n <<namespace>>

            # delete pod
            kubectl delete pod pod.yml -n <<namespace>>

            # edit pod
            kubectl edit pod pod.yml -n <<namespace>>

# EXAMPLES :

# Example 1: 
# Example yml file for pod by using jenkins image 

apiVersion: apps/v1
kind: Deployment
metadata:
  namespace: rjamapax
  name: vude-pod
spec:
  replicas: 1
  selector:
    matchLabels:
      app: jenkins
  template:
    metadata:
      labels:
        app: jenkins
    spec:
      containers:
      - name: jenkins
        image: jenkins/jenkins:lts
        ports:
         - name: http-port
           containerPort: 8080
# Example 2 :
# Example yml file for Create a service(NodePort) for jenkins 

apiVersion: v1
kind: Service
metadata:
  namespace: rjamapax
  name: vude-svc
  labels:
   app: jenkins
spec:
  type: NodePort
  ports:
 -  port: 8080   
    protocol: TCP
  selector:
    app: jenkins

# Example 3 :
# Below pipeline showing the kubernetes agents in Jenkins pipeline :

pipeline {
  agent {
    kubernetes {
      yaml '''
        apiVersion: v1
        kind: Pod
        spec:
          containers:
          - name: maven
            image: maven:alpine
            command:
            - cat
            tty: true
        '''
    }
  }
  stages {
    stage('Run maven') {
      steps {
        container('maven') {
          sh 'mvn -version'
        }
      }
    }
  }
}

# Example 4 :
# Below pipeline showing the Docker agents in Jenkins pipeline :

pipeline {
    agent {
        docker { image 'node:16.13.1-alpine' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'node --version'
            }
        }
    }
}

# Example 5 :
# Below pipeline showing the agents any in Jenkins pipeline :

pipeline {
    agent any
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'gradle:6.7-jdk11'
                }
            }
            steps {
                sh 'gradle --version'
            }
        }
    }
}    

# VERIFICATIONS:
    - Install Jenkins using docker - Done 
    - Install Jenkins using kubernetes POD - Done
    - Write a sample Jenkinsfile - Done
    - Integrate jenkins with bitbucket - Not Done
    - Integrate Jenkins with docker - Not Done
    - Integrate Jenkins with K8s - Not Done
    - Run jenkins job inside of docker containers - Not Done
    - Run jenkins job inside of K8s PODS - Not Done    

# REFERENCE :  
    - https://plugins.jenkins.io/kubernetes/
    - https://www.jenkins.io/blog/2021/12/08/containers-as-build-agents/
    - https://devopscube.com/jenkins-build-agents-kubernetes/
    - https://www.bogotobogo.com/DevOps/Docker/Docker_Kubernetes_PersistentVolumes_PersistentVolumeClaims.php
    - https://medium.com/@vishal.sharma./running-jenkins-in-kubernetes-cluster-with-persistent-volume-da6584edc126
    - https://www.digitalocean.com/community/tutorials/how-to-install-jenkins-on-kubernetes
