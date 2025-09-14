
from flask import Flask, request, redirect, render_template, url_for
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/')
db = client['celnex']
cred_collection = db['cred']
deck_collection = db['deck']

@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

@app.route("/", methods=["POST"])
def login():
    user_id_raw = request.form.get("user_id")

    if not user_id_raw or not user_id_raw.isdigit():
        return redirect(url_for('login_page', error=1))

    user_id = int(user_id_raw)
    user = cred_collection.find_one({"pid": user_id})

    if user:
        # fetch MARIA and A.V
        characters = list(deck_collection.find(
            {"char": {"$in": ["A.V", "MARIA"]}},
            {"_id": 0}
        ))

        return render_template(
            "welcome.html",
            user_id=user_id,
            characters=characters
        )
    else:
        return redirect(url_for('login_page', error=1))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/choose_character", methods=["POST"])
def choose_character():
    user_id = request.form.get("user_id")
    char_name = request.form.get("char_name")

    if not user_id or not char_name:
        return "<h2>Invalid request</h2>", 400

    user_id = int(user_id)
    character = deck_collection.find_one({"char": char_name}, {"_id": 0})

    if not character:
        return "<h2>Character not found</h2>", 404

    # create per-user collection
    user_collection = db[f"user_{user_id}"]
    user_collection.insert_one(character)

    return render_template("character.html", character=character, user_id=user_id)

if __name__ == "__main__":
    app.run(debug=True)
