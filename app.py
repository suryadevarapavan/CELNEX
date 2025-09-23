
from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # Replace with a secure key in production!

# MongoDB connection with authentication source set to 'dex'
client = MongoClient("mongodb://p1ttadu:pwd@localhost:27017/dex?authSource=dex")
db = client["dex"]
users_collection = db["users"]  # collection for login users

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        user = users_collection.find_one({"username": username, "password": password})
        if user:
            session["username"] = username
            return redirect("/work")
        else:
            return render_template("login.html", error="Invalid username or password")

    return render_template("login.html")

@app.route("/work", methods=["GET", "POST"])
def work():
    if "username" not in session:
        return redirect("/")

    message = ""

    if request.method == "POST":
        collection_name = request.form.get("collection", "").strip()
        name = request.form.get("name", "").strip()
        hp = request.form.get("hp", "").strip()

        if collection_name and name and hp:
            target_collection = db[collection_name]
            target_collection.insert_one({"name": name, "hp": hp})
            message = f"Inserted document into collection '{collection_name}'"
        else:
            message = "Please fill in all fields."

    # List all collections except 'users'
    collections = [col for col in db.list_collection_names() if col != "users"]
    data = {col: list(db[col].find()) for col in collections}

    return render_template("work.html", data=data, message=message)

@app.route("/delete/<collection>/<doc_id>")
def delete(collection, doc_id):
    if "username" not in session:
        return redirect("/")

    try:
        db[collection].delete_one({"_id": ObjectId(doc_id)})
    except Exception as e:
        print(f"Delete error: {e}")

    return redirect("/work")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
