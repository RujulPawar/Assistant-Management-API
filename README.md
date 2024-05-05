# Hirademy Assignment
This project is developing a backend application with CRUD APIs for managing assistants using python and MySQL. It includes defining database models, implementing API endpoints and testing with Postman.

## Required Installations and Setup
Install MySQL - https://dev.mysql.com/downloads/installer

MySQL setup - https://www.javatpoint.com/how-to-install-mysql

Install Postman - https://www.postman.com/downloads

## Required Packages
pip install mysql-connector-python
pip install flask

## How to Run the Code
Import the python codes into your IDE. In the Credentials.py file, change YOUR_USERNAME and YOUR_PASSWORD to the username and the password you set during the MySQL setup. Then run the Database.py file to intialize the database. After that run the Backend.py file and keep it running. A URL will be displayed in the output terminal.

## How to Test in Postman
Install "HirademyAssignment.postman_collection.json" file. Open and click on import in Postman and select the json file you installed. Copy and paste the url that you got when you run the Backend.py file. Add following endpoints for the specified requests :

GET - '/assistant/1' (This will retrieve the assistant details based on id. Here, id=1, change accordingly)

POST - '/assistant' (This will create a new assistant. Json file includes a request body, make changes as per the assistant you want to add. Here, id=1, change accordingly)

PUT - '/assistant/1' (This will update the assistant details based on id. Json file includes a request body, make changes that you want to update. Here, id=1, change accordingly)

DELETE - '/assistant/1' (This will delete the assistant details based on id. Here, id=1, change accordingly)
