# backend/routes/contact.py
from flask import Blueprint, request, jsonify

contact_bp = Blueprint('contact', __name__)

@contact_bp.route("/", methods=["POST"])
def submit_contact():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    message = data.get("message")

    # Add logic to save to DB or send email (placeholder here)
    print(f"Received contact from {name}, {email}: {message}")

    return jsonify({"status": "success", "message": "Message received."}), 200
