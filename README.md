# Assistant Management API
A RESTful API for managing assistant data using Flask and MySQL, supporting CRUD operations. It includes defining database models, implementing API endpoints and testing with Postman.

## 🚀 Features  
✅ **Create** new assistant records  
✅ **Read** assistant details by ID  
✅ **Update** assistant information  
✅ **Delete** an assistant entry  
✅ **Uses Flask & MySQL** for smooth database operations  
✅ **Postman collection included** for easy API testing 

## 📌 Required Installations and Setup
Install MySQL - https://dev.mysql.com/downloads/installer

MySQL setup - https://www.javatpoint.com/how-to-install-mysql

Install Postman - https://www.postman.com/downloads

### **Install Required Python Packages**  
```bash
pip install mysql-connector-python flask
```

## 🏃‍♂️ **How to Run the Project**  

1️⃣ **Clone the Repository**  

2️⃣ **Set Up Database**  
- Open **`Credentials.py`** and replace:  
  ```python
  USER = "YOUR_USERNAME"
  PASSWORD = "YOUR_PASSWORD"
  ```  
- Run the database initialization script:  
  ```bash
  python Database.py
  ```  
  This creates the **assistantsdb** database and preloads sample data.  

3️⃣ **Start the Flask Server**  
```bash
python Backend.py
```
A **localhost URL** (e.g., `http://127.0.0.1:5000`) will be displayed. 

## How to Test in Postman
Install "HirademyAssignment.postman_collection.json" file. Open and click on import in Postman and select the json file you installed. Copy and paste the url that you got when you run the Backend.py file. Add following endpoints for the specified requests :

GET - '/assistant/1' (This will retrieve the assistant details based on id. Here, id=1, change accordingly)

POST - '/assistant' (This will create a new assistant. Json file includes a request body, make changes as per the assistant you want to add. Here, id=1, change accordingly)

PUT - '/assistant/1' (This will update the assistant details based on id. Json file includes a request body, make changes that you want to update. Here, id=1, change accordingly)

DELETE - '/assistant/1' (This will delete the assistant details based on id. Here, id=1, change accordingly)

## 🛠️ **How to Test the API in Postman**  

**1️⃣ Import the Postman Collection**  
- Open **Postman**  
- Click **Import** → Select **`Assistant-Management-API.postman_collection.json`**  

**2️⃣ Use the API Endpoints**  

### ➟ **Retrieve an Assistant (GET)**  
```http
GET /assistant/{id}
```
📌 **Example:** `/assistant/1`  

### ➟ **Create a New Assistant (POST)**  
```http
POST /assistant
```
📌 **Body (JSON Example):**  
```json
{
  "id": "6",
  "name": "Varun",
  "mobile": "54321",
  "email": "varun@gmail.com",
  "salary": "1",
  "city": "Mumbai",
  "country": "India",
  "department": "Full Stack"
}
```

### ➟ **Update an Assistant (PUT)**  
```http
PUT /assistant/{id}
```
📌 **Example:** `/assistant/2`  

📌 **Body (JSON Example):**  
```json
{
  "name": "Rahul",
  "mobile": "54321",
  "email": "rahul@gmail.com",
  "salary": "0",
  "city": "Mumbai",
  "country": "India",
  "department": "Frontend"
}
```

### ➟ **Delete an Assistant (DELETE)**  
```http
DELETE /assistant/{id}
```
📌 **Example:** `/assistant/3`  

---

## 📝 **Tech Stack**  
🔹 **Python** (Flask)  
🔹 **MySQL** (Database)  
🔹 **Postman** (API Testing)  

## 📜 License  
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
