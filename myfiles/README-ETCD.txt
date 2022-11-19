1. Deploy ETCD Deployment POD and a Service for that POD
2. Run a Python Script to connect to that ETCD and CRUD(Create, Update & Delete Records)

# AIM : 
  Deploy ETCD Deployment POD and a Service for that POD

# PRE-REQUISITES:
  1. Docker
  2. Kubernetes cluster
  3. python-etcd 

# SECTION 1 :

  - What is ETCD ? :

    - Etcd stores the configuration data of the Kubernetes cluster
    - Uses etcd to store all its data - its configuration data
    - Etcd is a distributed database - because Kubernetes is a distributed system.
    - It also stores the actual state of the system and the desired state of the system in etcd.
    - Anything you might read from a kubectl get xyz
    - Any change you make via kubectl create xyz

# SECTION 2 :
  - ETCD Deployment POD :

  # STEP 1 :
    - Configuration file for the etcd server Explanation :

      - Apiversion -> Based on our resource type - v1
      - Kind -> Kind is nothing but our resource type like - POD
      - Metadata -> Information about our resources
      - Lable -> This is matching only thing like pod, service,deployment
      - Spec -> Then specification about out pod like image, name, port
      - Under the Container specification we have to configure the clustering

  # STEP 2 :  
    - Clustering configuration for ETCD :  

      - Human readable name for this member
      - Name -> default

      - Initial-advertise-peer-urls -> This peer URLs to advertise to the rest of the cluster.
      - These addresses are used for communicating etcd data around the cluster
      - These URLs can contain domain names like http://example.com

      - Initial-cluster -> Initial cluster configuration for bootstrapping
      - Default -> default=http://localhost:2380

      - Initial-cluster-state -> Initial cluster state means new or existing
      - If Set to new state for all members present during initial static
      - If option is set to existing, etcd will attempt to join the existing cluster

      - Advertise-client-urls -> Client URLs to advertise to the rest of the cluster
      - Client URLs can contain domain names like example.com
      - The advertise addresses must be reachable from the remote machines
      - Do not advertise addresses like localhost

      - To create a deployment by fallowing below command
          kubectl create -f <<dep.yml>> -n <<NS>>   

      - Below command is to get a pods
          kubectl get pods -n <<NS>>    

# SECTION 3 :    
  - Service for ETCD-POD Deployment :

  # STEP 1 :
  -  kubernetes service file Explanation :
      - Expose an application running on a set of Pods as a network service.
      - We can access the service from outside the cluster.
      - The sevicess way of grouping pods that are running on the cluster.

      - Apiversion -> Based on our resource type - v1
      - Kind -> Kind is nothing but our resource type like - Service
      - Metadata -> Information about our resources
      - Expose the service on a static port on each node
      - When the node receives a request on the static port
      - Select pods with the label 'app' set to etcd.
      - Three types of ports for a service
      - NodePort - a static port assigned on each the node
      - Port - port exposed internally in the cluster
      - TargetPort - the container port to send requests 

      - To create service by fallowing below command
          kubectl create -f <<svc.yml>> -n <<NS>>

      - Below command is to get a SVC
          kubectl get svc -n <<NS>>     

  # STEP 2 :
  - Interacting with etcd :
      - To know the ETCD Version fallowing below command
          kubectl exec -it <<etcd-0>> -- etcdctl --version

      - Login to the ETCD Pod by fallowin below command
          kubectl exec -it <<etcd-0>> -- /bin/sh    

      - Checking cluster and nodes heath by fallowing below command
          kubectl exec -it <<etcd-0>> -- etcdctl cluster-health    

      - To check the member list by fallowing below command
          kubectl exec -it <<etcd-0>> -- etcdctl member list

# EXAMPLES :

@ EXAMPLE 1 :

apiVersion: v1
kind: Pod
metadata:
  labels:
    app: etcd
    etcd_node: etcd0
  name: etcd0
spec:
  containers:
  - command:
    - /usr/local/bin/etcd
    - --name
    - etcd0
    - --initial-advertise-peer-urls
    - http://etcd0:2380
    - --listen-peer-urls
    - http://0.0.0.0:2380
    - --listen-client-urls
    - http://0.0.0.0:2379
    - --advertise-client-urls
    - http://etcd0:2379
    - --initial-cluster
    - etcd0=http://etcd0:2380,etcd1=http://etcd1:2380,etcd2=http://etcd2:2380
    - --initial-cluster-state
    - new
    image: quay.io/coreos/etcd:latest
    name: etcd0
    ports:
    - containerPort: 2379
      name: client
      protocol: TCP
    - containerPort: 2380
      name: server
      protocol: TCP
  restartPolicy: Always    

@ EXAMPLE 2 :

apiVersion: v1
kind: Service
metadata:
  name: etcd-client
spec:
  ports:
  - name: etcd-client-port
    port: 2379
    protocol: TCP
    targetPort: 2379
  selector:
    app: etcd

# VERIFICATIONS :
  - Create ETCD Deployment - Not Done
  - Create Service for Deployment - Not Done
  - Run a Python Script to connect to that ETCD - Not Done

# REFERENCE : 
  - https://etcd.io/docs/v3.4/op-guide/configuration/
  - https://python-etcd.readthedocs.io/en/latest/
  - https://github.com/rustudorcalin/deploying-etcd-cluster
  - https://kubernetes.io/docs/concepts/services-networking/service/

-----------------------------------------------------------------