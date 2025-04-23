# app.py
from flask import Flask
from flask_cors import CORS
from backend.routes import contact, projects

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin requests

# Register Blueprints
app.register_blueprint(contact.contact_bp, url_prefix="/api/contact")
app.register_blueprint(projects.projects_bp, url_prefix="/api/projects")

if __name__ == "__main__":
    app.run(debug=True)