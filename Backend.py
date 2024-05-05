# Import the required packages
import mysql.connector
from flask import Flask,jsonify,request
from Credentials import USER,PASSWORD

# Connect to MySQL server
db=mysql.connector.connect(host='localhost',user=USER,password=PASSWORD)

# Check if connection is established
if db.is_connected():
    print("Connection Established")

# Create cursor and use created database
cursor=db.cursor(dictionary=True)
cursor.execute("use assistantsdb")

app=Flask(__name__)

# API endpoint to retrieve an assistant by id
@app.route('/assistant/<int:assistant_id>',methods=['GET'])
def get_assistant(assistant_id):
    cursor=db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM assistants WHERE id = %s",(assistant_id,))
    assistant=cursor.fetchone()
    cursor.close()
    if assistant:
        return jsonify(assistant)
    else:
        return jsonify({'error' : 'Assistant not found'})

# API endpoint to create a new assistant
@app.route('/assistant',methods=['POST'])
def create_assistant():
    try:
        cursor=db.cursor(dictionary=True)
        data=request.json
        id=data.get('id')
        name=data.get('name')
        mobile=data.get('mobile')
        email=data.get('email')
        salary=data.get('salary')
        city=data.get('city')
        country=data.get('country')
        department=data.get('department')
        cursor.execute("INSERT INTO assistants (id, name, mobile, email, salary, city, country, department) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",(id, name, mobile, email, salary, city, country, department))
        cursor.close()
        db.commit()
        return jsonify({'message' : 'Assistant created successfully'})
    except Exception as e:
        return  jsonify({'error'})


# API endpoint to update an assistant by id
@app.route('/assistant/<int:assistant_id>',methods=['PUT'])
def update_assistant(assistant_id):
    cursor=db.cursor(dictionary=True)
    data=request.json
    name=data.get('name')
    mobile=data.get('mobile')
    email=data.get('email')
    salary=data.get('salary')
    city=data.get('city')
    country=data.get('country')
    department=data.get('department')
    cursor.execute("UPDATE assistants SET name = %s, mobile = %s, email = %s, salary = %s, city = %s, country = %s, department = %s WHERE id = %s",(name, mobile, email, salary, city, country, department, assistant_id))
    updated_rows=cursor.rowcount
    cursor.close()
    db.commit()
    if updated_rows>0:
        return jsonify({'message' : 'Assistant updated successfully'})
    else:
        return jsonify({'error' : 'Assistant not found'})

# API endpoint to delete an assistant by id
@app.route('/assistant/<int:assistant_id>', methods=['DELETE'])
def delete_assistant(assistant_id):
    cursor=db.cursor(dictionary=True)
    cursor.execute("DELETE FROM assistants WHERE id=%s",(assistant_id,))
    deleted_rows=cursor.rowcount
    cursor.close()
    db.commit()
    if deleted_rows>0:
        return jsonify({'message' : 'Assistant deleted successfully'})
    else:
        return jsonify({'error' : 'Assistant not found'})

if __name__=='__main__':
    app.run(debug=True)

print("Success")