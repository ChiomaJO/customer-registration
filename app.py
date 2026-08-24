import sqlite3
from pathlib import Path

from flask import Flask, render_template, request, jsonify, g


# --------------------------------------------------
# APPLICATION SETUP
# --------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "customers.db"

app = Flask(__name__)
app.config["DATABASE"] = DB_PATH


# --------------------------------------------------
# DATABASE CONNECTION
# --------------------------------------------------

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row

    return g.db


@app.teardown_appcontext
def close_db(error):
    db = g.pop("db", None)

    if db is not None:
        db.close()


# --------------------------------------------------
# CREATE DATABASE TABLE
# --------------------------------------------------

def init_db():
    db = get_db()

    db.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL,
            date_of_birth TEXT NOT NULL,
            gender TEXT NOT NULL,
            address TEXT NOT NULL
        )
    """)

    db.commit()


with app.app_context():
    init_db()


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


# --------------------------------------------------
# REGISTER CUSTOMER
# --------------------------------------------------

@app.route("/register", methods=["POST"])
def register():

    full_name = request.form.get("fullName", "").strip()
    email = request.form.get("email", "").strip()
    phone = request.form.get("phone", "").strip()
    date_of_birth = request.form.get("dateOfBirth", "").strip()
    gender = request.form.get("gender", "").strip()
    address = request.form.get("address", "").strip()

    # ------------------------------
    # SERVER-SIDE VALIDATION
    # ------------------------------

    if not full_name:
        return jsonify({
            "message": "Please enter your full name."
        }), 400

    if not email:
        return jsonify({
            "message": "Please enter your email address."
        }), 400

    if "@" not in email or "." not in email:
        return jsonify({
            "message": "Please enter a valid email address."
        }), 400

    if not phone:
        return jsonify({
            "message": "Please enter your phone number."
        }), 400

    if not phone.isdigit() or not 10 <= len(phone) <= 15:
        return jsonify({
            "message": "Please enter a valid phone number using 10 to 15 digits."
        }), 400

    if not date_of_birth:
        return jsonify({
            "message": "Please enter your date of birth."
        }), 400

    if not gender:
        return jsonify({
            "message": "Please select your gender."
        }), 400

    if not address:
        return jsonify({
            "message": "Please enter your address."
        }), 400


    # ------------------------------
    # SAVE CUSTOMER TO DATABASE
    # ------------------------------

    db = get_db()

    try:

        db.execute("""
            INSERT INTO customers
            (
                full_name,
                email,
                phone,
                date_of_birth,
                gender,
                address
            )
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            full_name,
            email,
            phone,
            date_of_birth,
            gender,
            address
        ))

        db.commit()

    except sqlite3.IntegrityError:

        return jsonify({
            "message": "This email address is already registered."
        }), 400


    return jsonify({
        "message": "Registration successful!"
    }), 200


# --------------------------------------------------
# VIEW CUSTOMERS
# --------------------------------------------------

@app.route("/customers")
def customers():

    db = get_db()

    rows = db.execute("""
        SELECT
            id,
            full_name,
            email,
            phone,
            date_of_birth,
            gender,
            address
        FROM customers
        ORDER BY id DESC
    """).fetchall()

    return render_template(
        "customers.html",
        customers=rows
    )


# --------------------------------------------------
# RUN APPLICATION
# --------------------------------------------------

if __name__ == "__main__":
    app.run(debug=True)