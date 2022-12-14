# python-flask-MYSQL :
********************

# Build a simple python flask web-app with MYSQL as database :

# What is MYSQL
    - MySQL is most popular Open Source SQL database management system.
    - MYSQL database is a structured collection of data
    - A relational database stores data in separate tables rather than putting all the data in one big storeroom.
    - The database structures are organized into physical files optimized for speed
    - The logical model, with objects such as databases, tables, views, rows, and columns, offers a flexible programming environment. 
    - MySQL benefits-> Ease of use, Reliability, Scalability, Performance, High availability,  Data security, Flexibility
    - MYSQL is mostly used for Ecommerce, Social platforms, Content management.

-------------------------------------------------------------------------------------------------------------------    

# How to Deploy MYSQL POD in kubernetes :

# MYSQL Configuration file :
    - Apiversion -> Based on our resource type - v1
    - Kind -> Kind is nothing but our resource type like - POD
    - Metadata -> Information about our resources
    - Lable -> This is matching only thing like pod, service,deployment
    - Spec -> Then specification about out pod like image, name, port

---------------------------------------------------------------------------------------------    

# How to create MYSQL POD Deployment :

apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: mysql_deployment
  namespace: mysql
spec:
  template:
    metadata:
      labels:
        app: mysql
    spec:
      containers:
        - env:
            - name: MYSQL_DATABASE
              value: admin
            - name: MYSQL_ROOT_PASSWORD
              value: admin
          image: 'mysql:latest'
          name: mysql
          ports:
            - name: mysqlport
              containerPort: 3306
              protocol: TCP

    - To create a deployment by fallowing below command
        kubectl create -f <<dep.yml>> -n <<NS>>   

    - Below command is to get a pods
        kubectl get pods -n <<NS>>  

------------------------------------------------------------------------------------------------

# How to create MYSQL Service Deployment :  

apiVersion: v1
kind: Service
metadata:
  name: mysql_service
  namespace: mysql
spec:
  ports:
  - port: 3306
    protocol: TCP
  selector:
    app: mysql-server
  type: NodePort

    - To create service by fallowing below command
        kubectl create -f <<svc.yml>> -n <<NS>>

    - Below command is to get a SVC
        kubectl get svc -n <<NS>>    

---------------------------------------------------------------------------------------------------------     

# How to deploy python application inside the kubernetes ?

    - First we need to create docker file for python image
        vi Docker file

    - first step in containerizing the application is to create a Dockerfile.
    - In the hello-python/app directory, create a file named Dockerfile with the following contents

        FROM python:3.7

        RUN mkdir /app
        WORKDIR /app
        ADD . /app/
        RUN pip install -r requirements.txt

        EXPOSE 5000
        CMD ["python", "/app/main.py"]

    - This file is a set of instructions Docker will use to build the image
    - Get the official Python Base Image from Docker Hub.
    - In the image, create a directory named app.
    - Set the working directory to that new app directory.
    - Copy the local directory???s contents to that new folder into the image.
    - Run the pip installer to pull the requirements into the image.
    - Inform Docker the container listens on port 5000.  

    - To build the image with the following command
        docker build -f Dockerfile -t hello-python:latest

    - To verify the image was created, run the following command
        docker image ls

    - Run the following command to have Docker run the application in a container 
        docker run -p 5001:5000 hello-python

    - Then you have to use the above image (hello-python) in python deployment

----------------------------------------------------------------------------------------------------

#  How to create python POD Deployment :

apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-python
  namespace: python
spec:
  selector:
    matchLabels:
      app: hello-python
  replicas: 1
  template:
    metadata:
      labels:
        app: hello-python
    spec:
      containers:
      - name: hello-python
        image: hello-python:latest
        imagePullPolicy: Never
        ports:
        - containerPort: 5000

    - To create a deployment by fallowing below command
        kubectl create -f <<dep.yml>> -n <<NS>>   

    - Below command is to get a pods
        kubectl get pods -n <<NS>>  

---------------------------------------------------------------------------------------------------------        
# How to create python Service Deployment : 

apiVersion: v1
kind: Service
metadata:
  name: hello-python-service
  namespace: python
spec:
  selector:
    app: hello-python
  ports:
  - protocol: "TCP"
    port: 6000
    targetPort: 5000
  type: NodePort

    - To create service by fallowing below command
        kubectl create -f <<svc.yml>> -n <<NS>>

    - Below command is to get a SVC
        kubectl get svc -n <<NS>>  

    - Now navigate to http://localhost:6000
    - you should see the ???Hello from Python!??? message.

------------------------------------------------------------------------------------------------------------               

# What is python flask :
    - Flask is a Python framework for creating web applications
    - python flask defines a set or rules for a web application to send and receive data.
    - It is a micro-framework, it is very easy to building web applications

------------------------------------------------------------------------------------------------------------

# How to create flask-app POD Deployment :

apiVersion: apps/v1
kind: Deployment
metadata:
  name: flaskapi-deployment
  namespace: flask
  labels:
    app: flaskapi
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flaskapi
  template:
    metadata:
      labels:
        app: flaskapi
    spec:
      containers:
        - name: flaskapi
          image: flask-api
          imagePullPolicy: Never
          ports:
            - containerPort: 5000
          env:
            - name: db_root_password
              valueFrom:
                secretKeyRef:
                  name: flaskapi-secrets
                  key: db_root_password
            - name: db_name
              value: flaskapi

    - To create a deployment by fallowing below command
        kubectl create -f <<dep.yml>> -n <<NS>>   

    - Below command is to get a pods
        kubectl get pods -n <<NS>>            

----------------------------------------------------------------------------------------------------------

# How to create flask-app Service Deployment : 

apiVersion: v1
kind: Service
metadata:
  name: flask-service
  namespace: flask
spec:
  ports:
  - port: 5000
    protocol: TCP
    targetPort: 5000
  selector:
    app: flaskapi
  type: NodePort

-----------------------------------------------------------------------------------------------------------    

# How to install python flask server :

    - Setting up Flask is pretty simple and quick. With pip package manager.
        pip install flask

    - Create a file called app.py
    - By using below python code Import the flask module and create an app using Flask 
        from flask import Flask
        app = Flask(__name__)

    - Now define the basic route / and its corresponding request handler
        @app.route("/")
        def main():
            return "Welcome!"    

    - Next, check if the executed file is the main program and run the app
        if __name__ == "__main__":
            app.run()        

    - Save the changes and execute app.py
        python app.py

    - Point your browser to http://localhost:5000/ and you should have the welcome message.

----------------------------------------------------------------------------------------------------------    

# Python MySQL Database Connection using MySQL Connector

    - Username :
    	The username that you use to work with MySQL Server.
        The default username for the MySQL database is a root.

    - Password :	
        Password is given by the user at the time of installing the MySQL server.  

    - Host name	:
        The server name or Ip address on which MySQL is running. 

    - Database name	:
        The name of the database to which you want to connect and perform the operations.          

        import datetime
        import mysql.connector

        __cnx = None

        def get_sql_connection():
        print("Opening mysql connection")
        global __cnx

        if __cnx is None:
            __cnx = mysql.connector.connect(user='root', password='root', database='grocery_store')

        return __cnx

-------------------------------------------------------------------------------------------------------------------

# Querying Data Using Connector/Python :
    - The following example shows how to query data using a cursor created using the connection's cursor() method
    - The data returned is formatted and printed on the console.

from datetime import datetime
from sql_connection import get_sql_connection

def insert_order(connection, order):
    cursor = connection.cursor()

    order_query = ("INSERT INTO orders "
             "(customer_name, total, datetime)"
             "VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['grand_total'], datetime.now())

    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    order_details_query = ("INSERT INTO order_details "
                           "(order_id, product_id, quantity, total_price)"
                           "VALUES (%s, %s, %s, %s)")

    order_details_data = []
    for order_detail_record in order['order_details']:
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])
    cursor.executemany(order_details_query, order_details_data)

    connection.commit()

    return order_id

def get_order_details(connection, order_id):
    cursor = connection.cursor()

    query = "SELECT * from order_details where order_id = %s"

    query = "SELECT order_details.order_id, order_details.quantity, order_details.total_price, "\
            "products.name, products.price_per_unit FROM order_details LEFT JOIN products on " \
            "order_details.product_id = products.product_id where order_details.order_id = %s"

    data = (order_id, )

    cursor.execute(query, data)

    records = []
    for (order_id, quantity, total_price, product_name, price_per_unit) in cursor:
        records.append({
            'order_id': order_id,
            'quantity': quantity,
            'total_price': total_price,
            'product_name': product_name,
            'price_per_unit': price_per_unit
        })

    cursor.close()

    return records

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)
    response = []
    for (order_id, customer_name, total, dt) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'datetime': dt,
        })

    cursor.close()

    # append order details in each order
    for record in response:
        record['order_details'] = get_order_details(connection, record['order_id'])

    return response

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))
    # print(get_order_details(connection,4))
    # print(insert_order(connection, {
    #     'customer_name': 'dhaval',
    #     'total': '500',
    #     'datetime': datetime.now(),
    #     'order_details': [
    #         {
    #             'product_id': 1,
    #             'quantity': 2,
    #             'total_price': 50
    #         },
    #         {
    #             'product_id': 3,
    #             'quantity': 1,
    #             'total_price': 30
    #         }
    #     ]
    # }))

--------------------------------------------------------------------------------------------------------------------

# Python Flask APIs for GET, POST,PUT,DELETE Oparations :

# Deploy API :

from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import mysql.connector
import json

import products_dao
import orders_dao
import uom_dao

app = Flask(__name__)

connection = get_sql_connection()

---------------------------------------------------------------------------------------------------------------------

# GET- Method by using python flask code for MySQL :

@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

-----------------------------------------------------------------------------------------------------------------

# POST- Method by using python flask code for MySQL DB :

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

---------------------------------------------------------------------------------------------------------

# UPDATE- Method by using python flask code for MySQL DB :

@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

---------------------------------------------------------------------------------------------------------------

# DELETE - Method by using python flask code for MySQL DB :    

@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5000)

Price of products			
			
-----------------------------------------------------------------------------------------------------------

# MYSQL DB & Tables :

1. Product 
    1. Aim: Product Information
    2. Fields :
        1. product_name
        2. product_id
        3. quantity
        4. Price
        5. Stock
        6. Mfg_datetime
        7. Exp_date

2. Order
    1. Aim: Order Information
    2. Fields:
        1. Product
        2. Quantity
        3. Price
        4. Total
        5. Product_id

3. Customer    
    1. Aim: Customer Information
    2. fields
        1. Customer_name
        2. Order_number
        3. Product_name
        4. Order_date
        5. Total_order
        6. customer_address
        7. customer_mobile_number
        8. customer_ gender

4. Inventory
    1. Aim: Inventory Information
    2. fields
        1. Procuct
        2. Unit_price
        3. Qty_in_hand
        4. Qty_sold
        5. Inventory_value
        6. Sales_stock
        7. Available_stock

5. Discout
    1. Aim: Product Discount Information
    2. fields
        1. Product
        2. Quantity
        3. Price
        4. Total
        5. Discount
        6. Total_amount

6. Bill
    1. Aim: Product bill Information
    2. fields
        1. Product_id   
        2. Invoice_id
        3. Invoice_date
        4. Supplier_name
        5. Payment_mode
        6. Amount
        7. Status

7. Feedback
    1. Aim: Customer feedback Information
    2. fields
        1. product
        2. Customer_name
        3. rating
        4. feedback
        5. suggestion

8. Product section     
    1. Aim: Product available section
    2. fields
        1. product_name
        2. product_id
        3. Available_floor
        4. Available_section
        5. Section_keeper
        6. Stock

9. Customer timing 
    1. Aim: Customer spend in storeroom
    2. fields
        1. customer_name
        2. customer_id
        3. date
        4. entry_time
        5. exit_time
        6. duration_time    

10.Product Exchange
    1. Aim: Product Exchange Information      
    2. fields
        1. product
        2. customer_name
        3. exchange_item
        4. reason
        5. invoice/bill
        6. product_id











