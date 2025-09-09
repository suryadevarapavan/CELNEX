from flask import Flask, request, redirect, render_template, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['celnex']
users_collection = db['cred']

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            user_id = int(request.form.get("user_id"))
        except ValueError:
            return redirect(url_for('login', error=1))

        user = users_collection.find_one({"pid": user_id})

        if user:
            return f"<h2>Welcome, {user_id}!</h2><p>You have successfully logged in.</p>"
        else:
            return redirect(url_for('login', error=1))
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

