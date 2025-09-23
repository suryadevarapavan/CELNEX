import os
from flask import Flask, jsonify
from pymongo import MongoClient, errors

app = Flask(__name__)

# Get MongoDB URI from environment variable
MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise Exception("MONGODB_URI environment variable is not set!")

try:
    # Connect to MongoDB with 5-second timeout
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    db = client.get_default_database()

    # Force connection on startup to verify everything works
    client.server_info()
except errors.ServerSelectionTimeoutError as e:
    print("Could not connect to MongoDB:", e)
    raise

@app.route('/')
def home():
    return jsonify({"message": "Connected to MongoDB successfully!"})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
