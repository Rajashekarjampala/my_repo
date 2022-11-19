# Grafana :
*********

# What is Grafana and its Applications :
    - Grafana is a popular open source, general purpose dashboards
    - Grafana is a visualization tool that offers beautiful visualizations.
    - And interactive graphs and easy-to-set-up dashboards.
    - Grafana, which runs as a web application, is used by small to large enterprises to monitor visualizations.
    - And manage reports on metrics, logs and alerts.
    - Grafana Integrates with set of data sources, like Prometheus,MySQL, Elasticsearch and Splunk.

# AIM :
    To monitoring the kubernetes deployments and infra by using Grafana

# DEFINATION OF DONE :
    Monitioring kuberntes deployements, configuration, cup utilization, memory utilization and disk utilization
    By using grafana and it will display the perfomence of application in nice dashboards.

# PRE-REQUISITES :  
    1. kubernetes-cluster
    2. Docker
    
# STAGES :
    STAGE 1 :

        STEP 1 :
            Create A Namespace :
                - First, we will create a Kubernetes namespace for all our monitoring components

                - Execute the following command to create a new namespace 
                    kubectl create namespace << namespace-name >>

                - following below command to check namespace create or not
                    kubectl get ns

    STAGE 2 : 
        Installation using Kubernetes :

        STEP 1 :
            Create A Grafana Deployment :
                - Create a file for prometheus deployment

        STEP 2 :
            Configuration file for the Grafana server Explanation :

                - Apiversion -> Based on our resource type - v1
                - Kind -> Kind is nothing but our resource type like - Deployment
                - Metadata -> Information about our resources
                - Lable -> This is matching only thing like pod, service,deployment
                - Spec -> Then specification about out pod like image, name, port   

        STEP 3 :
            Create a deployment on monitoring namespace using the above file :
                - kubectl create -f << Dep.yml>> -n << namespace >>

            You can check the created deployment using the following command : 
                - kubectl get deployments -n << namespace >>

        STEP 4 : 
            Create a Grafana Service :
                - Create a file for prometheus deployment

        STEP 5 :
            Create a service on monitoring namespace using the above file :
                - kubectl create -f << svc.yml>> -n << namespace >>

            You can check the created service using the following command : 
                - kubectl get svc -n << namespace >>  

        STEP 6 :
            Once created nodeport service, you can access the Grafana dashboard using any Kubernetes node IP.
                << VM-IP >> : << NodePort >>
                - Navigate to http://localhost:<< PORT-NUMBER >> to access the Grafana UI:

# Create Specifications file for grafana :

- Deployment yml file for grafana :

apiVersion: apps/v1
kind: Deployment
metadata:
  name: grafana
  namespace: monitoring
spec:
  replicas: 1
  selector:
    matchLabels:
      app: grafana
  template:
    metadata:
      name: grafana
      labels:
        app: grafana
    spec:
      containers:
      - name: grafana
        image: grafana/grafana:latest
        ports:
        - name: grafana
          containerPort: 3000

- Service yml file for grafana :

apiVersion: v1
kind: Service
metadata:
  name: grafana
  namespace: monitoring
  annotations:
      prometheus.io/scrape: 'true'
      prometheus.io/port:   '3000'
spec:
  selector: 
    app: grafana
  type: NodePort  
  ports:
    - port: 3000
      targetPort: 3000
      nodePort: 32000

# Automation for Grafana Deployment and Service :

function deployment() {
   echo "Bring up Deployment => START"
   kubectl apply -f /opt/vude/assignments/grafana/specs/deployments/start.yml
   echo "Deployment ACTIVE => DONE"  
}

function svcs() {
   echo "Bring up Service => START"
   kubectl apply -f /opt/vude/assignments/grafana/specs/svc/start.yml
   echo "Service ACTIVE  => DONE"
}


function main() {
#  namespace $1
  deployment
  svcs
}

# Arguments :: $1 = namespace
main $1

# VERIFICATIONS :
    1. Create Grafana Deployment - Done
    2. Create Grafana Service - Done
    3. Access the Grafana UI - Done

# REFERENCE :
    - https://devopscube.com/setup-grafana-kubernetes/
    - https://github.com/DeekshithSN/kubernetes/blob/master/monitoring/kubernetes-grafana/service.yaml
--------------------------------------------------------------------------------------------------------
https://avleonov.com/2020/06/10/how-to-list-create-update-and-delete-grafana-dashboards-via-api/
https://www.itpanther.com/grafana-rest-apis/

