from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # Connect to the MySQL database
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='696969',
            database='db1'
        )

        cursor = connection.cursor(dictionary=True)

        # Execute a query to fetch data from the 'world' table
        cursor.execute("SELECT * FROM student")

        # Fetch all the data
        data = cursor.fetchall()

        # Close the cursor and the database connection
        cursor.close()
        connection.close()
        # Convert the data to JSON and return it
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
