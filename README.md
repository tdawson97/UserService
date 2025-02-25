# User-Service
This user service microservice accepts a username and password input to sign up a new user or log in an existing user and returns the user ID associated with the account to the calling program. The service also allows for a stored password to be changed and a message returned indicating a successfully updated password. 

## How To REQUEST Data
Simply use one of the route endpoints to request data with the specified function. The three routes are aptly named '/signup', '/login', and '/change_password' and can be called on using the requests module in Python in the following manner.  
  
import requests  
userSignUp = "http://127.0.0.1:5000/signup"  
data = {'username': username,  
            'password': password }  
**response = requests.post(userSignUp, json=data)**  

The service is written as is to run locally on port 5000.

## How to RECEIVE Data
Each function will receive and return data in the form of JSON data. This data can be accessed using the requests module and json method in python in the following manner.  

import requests  
userSignUp = "http://127.0.0.1:5000/signup" 
data = {'username': username,  
            'password': password }  
response = requests.post(userSignUp, json=data)  
**receivedData = response.json()['id']**

## UML Sequence Diagram
![screenshot](/UMLDiagram.png)# UserService
