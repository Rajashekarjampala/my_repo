# KIBANA :
**********

SECTION 1:
---------
    # What's kibana and why we use it ?
        - Kibana is an open source browser based visualization tool.
        - Searching, viewing, and visualizing data indexed in Elasticsearch and analyzing the data
        - By using data Creation of bar charts, pie charts, tables, histograms, and maps
        - Kibana works in sync with Elasticsearch and Logstash which together forms the so called ELK.
        - A dashboard view combines these visual elements to then be shared via browser.
        - Kibana used for Infrastructure metrics and container monitoring
        - Application performance monitoring (APM)
        - Geospatial data analysis and visualization
        - Monitoring, managing, and securing an Elastic Stack instance via web interface.

SECTION 2:
---------
    # Deploying kibana using Dockers :
        - Docker images for Kibana are available from the Elastic Docker registry
        - Before pull Docker Image (Kibana image) We have to create the Docker network

        - Docker network creation
            docker network create <Network_Name>

        1. Docker Image name
            docker pull docker.elastic.co/kibana/kibana:8.5.0
            
        2. Running Docker Container
            docker run --name <kibana> --net <Network_Name> -p 5601:5601 docker.elastic.co/kibana/kibana:8.5.0

        - Kibana default port number is 5601
        - We can access the kibana UI Access using localhost:5601 or VM_IP:5601        
        
SECTION 3:
---------
    # Deploying kibana using Kubernetes :
        - First we have to create name space for kibana

        - Name Space create by using below command
            kubectl create namespace <namespace_name>
        
        - Check name space created or not by Using below command
            kubectl get namespace        

        1. Deployment Spec
            - We can create Deployment yml file for kibana
                vi deployment.yml

            - To deploy the kibana by using below command specified namespace
                kubectl create -f service.yml -n <Namespace>

            - Check the deployment by using below command
                kubectl get deployments -n <namespece>  

            - Check the pods by using below command   
                kubectl get pods -n <namespece> 

        2. Service Spec
            - We can create Service yml file for kibana
                vi service.yml

            - To deploy the kibana by using below command specified namespace
                kubectl create -f service.yml -n <Name_space>

            - Check the service by using below command
                kubectl get svc -n <namespece>      

            - Kibana UI Access using localhost:port or VM_IP:5601

        3. kubectl commands for debug
            - Describe the pod by using below command
                kubectl describe  pod <pod-name> -n <namespace-name>

            - Edit pod by using below command
                kubectl edit  pod <pod-name> -n <namespace-name>

            - Describe the service by using below command
                kubectl describe  svc <svc-name> -n <namespace-name>  

            - Edit Service by using below command
                kubectl edit  svc <svc-name> -n <namespace-name>   

SECTION 4:
---------
    # Deploying kibana using HELM
        1. HELM Charts
        2. HELM commands for bring-up
        3. HELM commands for debug

SECTION 5:
---------
    # Verification post installation
        1. Access kibana in UI

        2. CREATE/DELETE/UPDATE Indexes
            - In Elasticsearch, data is stored as documents. A document is a JSON object format. 
            - Each document has a unique ID.
            - In a JSON object, you have a list of fields or key value pairs.
             
            CREATE--> Create an index        
                - PUT <Name-of-the-Index>

                - To create an index, we use verb PUT followed by the name of the index
                - When index is used as a verb, it means that we are storing documents.

            POST:
                - You use POST it will autogenerate an id for your document. 

                    POST emp_data/_doc
                    {
                    "first_name": "Rajashekar",
                    "last_name": "Jampala"
                    "emp_id": "143"
                    "Emp_age": "25"
                    }     
 
                - You use the verb PUT when you want to assign a specific id to your document
                - If only use put was an easier way to index and find these documents.

                    PUT emp_data/_doc/1       # 1 is the index unique ID
                    {
                    "first_name": "Rajashekar",
                    "last_name": "Jampala"
                    }

            READ--> Read a document
                - We use the following syntax to read the previously created document.
                    GET emp_data/_doc/id

                - This request directs kibana to GET from emp_data index a document(_doc) with an id of 1

            UPDATE--> Update a document
                - There will be times when you will want to update an existing document

                - You will use the following syntax to update a field of a document.

                    POST emp_data/_update/1_update
                    {
                        "doc": {
                            "age": "26"     # Update the employee age
                        }
                    } 

            DELETE--> Delete a document
                - The following syntax is used to delete a document.
                    DELETE emp_data/_doc/1_delete

                - Then it will deleted the emp_data Index  
      
SECTION 6:
---------
    # kibana UI Access
        - http://10.208.41.125:5601

SECTION 7:
---------
    # REST API Commands for all CRUD
        - Create an Index on kibana by using below command
            curl -XPUT "http://10.208.41.125:5601/emp_data" 

        - To verify Index created or not by using below command
            curl -XGET "http://10.208.41.125:5601/emp_data" 

        - Insert our date into our index by using below command
            curl -XPOST "http://10.208.41.125:5601/emp_data/_doc/1" -H 'Content-Type: application/json' -d' 
            {
            "Emp_name": "Rajashekar",
            "Emp_id": "143",
            "Age": 25,
            "Gender": "male",
            "Address": "Hyderabad"
            }'  

        - Update data in to our index by using below command
            curl -XPOST "http://10.208.41.125:5601/emp_data/_doc/1" -H 'Content-Type: application/json' -d'
            {
            "Emp_name": "Rajashekar",
            "Emp_id": "12345",     # Update emp_id
            "Age": 25,
            "Gender": "male",
            "Address": "Hyderabad"
            }' 

        - Delete in our index by using below command
            curl -XDELETE "http://10.208.41.125:5601/emp_data"  

    # Bulk API for Multiple Document Indexing and Modification

        Create bulk indexes:
            curl -XPOST "http://10.208.41.125:5601/_bulk" -H 'Content-Type: application/json' -d' 
            {"create" : {"_index":"emp_data", "_id":"1"}}
            {"name":"Rajashekar", "emp_id":"143", "dob":"1997","desc":"Devops", "address":"hyderabad", "age":"25"}
            {"create" : {"_index":"emp_data", "_id":"2"}}
            {"name":"Sai maneesh", "emp_id":"123", "dob":"1998","desc":"tester", "address":"nellur", "age":"24"}
            {"create" : {"_index":"emp_data", "_id":"3"}}
            {"name":"Venkat", "emp_id":"456", "dob":"1995","desc":"developer", "address":"guntur", "age":"26"}
            {"create" : {"_index":"emp_data", "_id":"4"}}
            {"name":"Rakesh", "emp_id":"789", "dob":"1990","desc":"tech_spec", "address":"chennai", "age":"32"}
            {"create" : {"_index":"emp_data", "_id":"5"}}
            {"name":"Gowtham", "emp_id":"112", "dob":"1980","desc":"Team_lead", "address":"bangulur", "age":"40"}
            {"create" : {"_index":"emp_data", "_id":"6"}}
            {"name":"sunil", "emp_id":"321", "dob":"1992","desc":"jr_developer", "address":"mumbai", "age":"30"}
            {"create" : {"_index":"emp_data", "_id":"7"}}
            {"name":"kumar", "emp_id":"555", "dob":"1970","desc":"manager", "address":"pune", "age":"52"}
            {"create" : {"_index":"emp_data", "_id":"8"}}
            {"name":"karthik", "emp_id":"900", "dob":"1972","desc":"gen_manager", "address":"kadapa", "age":"50"}
            {"create" : {"_index":"emp_data", "_id":"9"}}
            {"name":"prashanth", "emp_id":"210", "dob":"1993","desc":"asso_engg", "address":"ranchi", "age":"23"}
            {"create" : {"_index":"emp_data", "_id":"10"}}
            {"name":"sravika", "emp_id":"560", "dob":"1984","desc":"repo_manager", "address":"tirupati", "age":"35"}
            {"create" : {"_index":"emp_data", "_id":"11"}}
            {"name":"sony", "emp_id":"987", "dob":"1999","desc":"jr_trainee", "address":"mncl", "age":"23"}
            {"create" : {"_index":"emp_data", "_id":"12"}}
            {"name":"sanjana", "emp_id":"300", "dob":"1998","desc":"jr_engg", "address":"lb_nagar", "age":"22"}
            {"create" : {"_index":"emp_data", "_id":"13"}}
            {"name":"sravani", "emp_id":"380", "dob":"1994","desc":"typist", "address":"kachiguda", "age":"26"}
            {"create" : {"_index":"emp_data", "_id":"14"}}
            {"name":"pooja", "emp_id":"777", "dob":"1988","desc":"security", "address":"koti", "age":"32"}
            {"create" : {"_index":"emp_data", "_id":"15"}}
            {"name":"aruna", "emp_id":"760", "dob":"1990","desc":"trainer", "address":"kukatpally", "age":"30"}

        Update bulk indexes:
            curl -XPOST "http://10.208.41.125:5601/_bulk" -H 'Content-Type: application/json' -d' 
            {"update" : {"_index":"emp_data", "_id":"3"}}
            {"doc": {"desc":"senior manager"}}
            {"update" : {"_index":"emp_data", "_id":"5"}}
            {"doc": {"address":"ananthapur"}}
            {"update" : {"_index":"emp_data", "_id":"6"}}
            {"doc": {"desc":"sr_develpoer"}}
            {"update" : {"_index":"emp_data", "_id":"10"}}
            {"doc": {"age":"25"}}
            {"update" : {"_index":"emp_data", "_id":"2"}}
            {"doc": {"dob":"27"}}

        Delete bulk indexes:   
            curl -XPOST "http://10.208.41.125:5601/_bulk" -H 'Content-Type: application/json' -d'
            {"delete" : {"_index":"emp_data", "_id":"1"}}
            {"delete" : {"_index":"emp_data", "_id":"12"}}
            {"delete" : {"_index":"emp_data", "_id":"4"}}
            {"delete" : {"_index":"emp_data", "_id":"13"}}
            {"delete" : {"_index":"emp_data", "_id":"15"}}
            {"delete" : {"_index":"emp_data", "_id":"7"}}

        Search bulk indexes:
            curl -XGET "http://10.208.41.125:5601/_bulk" -H 'Content-Type: application/json' -d'
            {
                "query": {
                    "match_all": {}
                }
            }

        Performs multiple Indexing, Updating, Deleting operations in a single API call:
            curl -XPOST "http://10.208.41.125:5601/_bulk" -H 'Content-Type: application/json' -d'
            {"create":{"_index":"emp_data", "_id":"16"}}
            {"name":"mahesh","desc":"pro_manager"}
            {"delete":{"_index":"employee", "_id":"5"}}
            {"update":{"_index":"emp_data","_id":"4"}}
            {"name":"ramesh,"desc":"sr_devops"}            
       
SECTION 8:
----------
Kibana deployment yml file

    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: kibana
      namespace: kibana
      labels:
        app: kibana
        kubernetes.io/cluster-service: "true"
        addonmanager.kubernetes.io/mode: Reconcile
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: kibana
      template:
        metadata:
          labels:
            app: kibana
          annotations:
            seccomp.security.alpha.kubernetes.io/pod: 'docker/default'
            spec:
              containers:
              - name: kibana
              image: docker.elastic.co/kibana/kibana-oss:6.5.4
              resources:
             # need more cpu upon initialization, therefore burstable class
                limits:
                  cpu: 1000m
                requests:
                  cpu: 100m
              env:
                - name: ELASTICSEARCH_URL
                value: http://10.208.41.125:5601/
              ports:
                - containerPort: 5601
                name: ui
                protocol: TCP

Kibana Service yml file

    apiVersion: v1
    kind: Service
    metadata:
      name: kibana
      namespace: kibana
      labels:
        app: kibana
        kubernetes.io/cluster-service: "true"
        addonmanager.kubernetes.io/mode: Reconcile
        kubernetes.io/name: "Kibana"
    spec:
      type: NodePort
      ports:
      - port: 5601
        protocol: TCP
        targetPort: ui
        nodePort: 31336
      selector:
        app: kibana         

SECTION 9:
---------
    # References
        - https://www.youtube.com/watch?v=pL_0qKxIWZE
        - https://www.elastic.co/guide/en/kibana/current/docker.html
        - https://dev.to/elastic/performing-crud-operations-with-elasticsearch-kibana-50ka
        - https://www.elastic.co/guide/en/elasticsearch/reference/7.17/docs-bulk.html

#   m y _ r e p o  
 