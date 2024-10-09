from flask import Flask, request, jsonify
import sqlite3
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

# Initialize the database
def init_db():
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')

        # Validate input data
        if not name or not email:
            logging.warning("Empty fields submitted.")
            return jsonify({"error": "Please provide both name and email."}), 400

        # Insert data into the database
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        conn.close()

        logging.info(f"User added: {name}, {email}")
        return jsonify({"message": "Data submitted successfully!"}), 200
    except sqlite3.IntegrityError:
        logging.error("Email already exists in the database.")
        return jsonify({"error": "Email already exists."}), 400
    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return jsonify({"error": "An error occurred while processing the request."}), 500

if __name__ == '__main__':
    init_db()  # Initialize the database
    app.run(debug=True)
