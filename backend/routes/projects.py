# backend/routes/projects.py
from flask import Blueprint, jsonify

projects_bp = Blueprint('projects', __name__)

@projects_bp.route("/", methods=["GET"])
def get_projects():
    # Placeholder: normally fetch from DB or JSON file
    projects = [
        {"title": "Data Forecasting", "tech": ["Python", "Prophet"], "link": "https://github.com/your/project1"},
        {"title": "Recommendation Engine", "tech": ["Flask", "Pandas"], "link": "https://github.com/your/project2"},
    ]
    return jsonify(projects)
