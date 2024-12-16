from flask import Flask, request, jsonify
from src.utils.database import Base, engine
from src.models.user import User
from src.controllers.auth_controller import auth

app = Flask(__name__)
app.register_blueprint(blueprint= auth, url_prefix="/auth")

@app.get("/")
def main_page():
    return jsonify({
        "status": "active",
        "message": "welcome to my landpage"
    }), 200

if __name__ == "__main___":
    app.run(
        host = "0.0.0.0",
        port = 5000
    )

