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
```bash
git clone https://github.com/RujulPawar/Assistant-Management-API.git
cd Assistant-Management-API
```

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

## 🛠️ **How to Test the API in Postman**  

**1️⃣ Import the Postman Collection**  
- Open **Postman**  
- Click **Import** → Select **`Assistant-Management-API.postman_collection.json`**  

**2️⃣ Use the API Endpoints**  

### ➟ **Retrieve an Assistant (GET)**  
```http
GET /assistant/{id}
```
📌 **Example:** `/assistant/2`
![GET Assistant](Postman%20Screenshots/Get.png)

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
![POST Assistant](Postman%20Screenshots/Post.png)

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
![PUT Assistant](Postman%20Screenshots/Put.png)

### ➟ **Delete an Assistant (DELETE)**  
```http
DELETE /assistant/{id}
```
📌 **Example:** `/assistant/4`  
![DELETE Assistant](Postman%20Screenshots/Delete.png)

## 📊 **Database State After CRUD Operations**
The following screenshot shows the state of the MySQL database after each CRUD operation:
![Database](Postman%20Screenshots/MySQL-Database.png)

---
## 📝 **Tech Stack**  
🔹 **Python** (Flask)  
🔹 **MySQL** (Database)  
🔹 **Postman** (API Testing)  

## 📜 License  
This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.
