# Neighbourhood

## Author
* Omar Hussein

## Description
Neighbourhood is an application where a user is able to join a neighbourhood group to be in the loop about everything happening in the neighbourhood.The user has to sign up in order to join a neighbourhood. Once the user joins a neighbourhood, the user can see businesses and posts in that neighbourhood that they belong to.

## User Story
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Only view details of a single neighborhood.
* Change My neighborhood when I decide to move out.

## SetUp instructions

To come up with the same project...

###### Clone the repository:
  * https://github.com/omarion3698/Neighbourhood.git
  
###### Navigate into the folder and install requirements
  * cd Neighbourhood 
  * pip install -r requirements.txt
  
###### Install and activate Virtual environment
  * virtualenv venv
  * source venv/bin/activate
  
###### Install Dependencies
  * pip install -r requirements.txt
  
##### Setup Database

###### SetUp your database User,Password, Host then make migrate
  * python manage.py makemigrations neighbour
  
###### Now Migrate
  * python manage.py migrate
  
###### Run the application
  * python manage.py runserver
  
###### Testing the application
  * python manage.py test
  
Open the application on your browser 127.0.0.1:8000.

## Technologies Used
* Python3.8
* Django
* Heroku
* Html5
* Css3
* JavaScript
* Postgresql

## Contact Information
If you have any questions or contributions, please email me at [omaribinbakarivic@gmail.com]

## License
* Licensed under the [MIT License](LICENSE)
* Copyright (c) 2020 Omar Hussein.
