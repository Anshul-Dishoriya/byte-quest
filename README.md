## Byte Quest Assignemnt

### Introduction

Created an CRUD API using Django on whcih user can CRUD oprtains on on Products and Django Default Session Authentication has beed used,
which adds the security to the Application.


### Swagger-UI

Added Documentation with the help of Swagger-UI to all API Endpoints.

### Features

`Get all Products` from `API`

`Update` Product details on `API`

`Create` Product on `API`

`Delete` Product to `API`

`Read the Documentation` of all `API` end points.


### Requirements
Before getting started, ensure you have the following prerequisites installed:

  `Python`

### Installation

Clone this repo to your machine

    $ git clone https://github.com/Anshul-Dishoriya/byte-quest.git
    
If you wish to buid  your own Virtual Enviourment , run these Following Commands :

     $ pip install virtualenv
     $ virtualenv venv

### Dependencies

Activate the virtual env by running the following command:
    
    $ ./venv/scripts/activate
Install the dependencies needed to run the app:

    $ pip install -r requirements.txt 

### Run It on Local Machine
   
   Fire up the server using this one simple command:
     
       $ python manage.py runserver
   You can now access the file API service on your browser by using
   
       http://localhost:8000/

### Access it Wihtout Installing

   Link : https://dishoriyaanshul.pythonanywhere.com/

   API end points :
   1. Use `GET` method to List all Products = `https://dishoriyaanshul.pythonanywhere.com/api/shop/`
   2. Use `POST` method to Add Product = `https://dishoriyaanshul.pythonanywhere.com/api/shop/`
   3. Use `PUT` method to Update a Product with `ID` = `https://dishoriyaanshul.pythonanywhere.com/api/shop/{id}`
   4. Use `Delete` method to Delete Product with `ID` = `https://dishoriyaanshul.pythonanywhere.com/api/shop/{id}`
   5. Use `GET` method to Access Documentation for all `API end points` = `https://dishoriyaanshul.pythonanywhere.com/api/schema/swagger-ui/`
 

