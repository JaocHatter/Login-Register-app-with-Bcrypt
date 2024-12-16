from src.services.auth_service import AuthService
from src.utils.database import get_db
from sqlalchemy.orm import Session
from flask import Blueprint, request, jsonify

auth = Blueprint("auth", import_name= __name__)

@auth.post("/register")
def register():
    """
    curl -X POST http://localhost:5000/auth/register \
     -H "Content-Type: application/json" \
     -d '{"username": "usuario1", "password": "1234", "email": "usuario1@example.com"}'
    """
    db:Session = next(get_db())
    auth_service = AuthService(db)
    data = request.json
    if data:
        auth_service.register_user(
            username= data["username"],
            password= data["password"],
            email = data["email"]
        )
    return jsonify({"message": "user created successfully", "status": 201}), 201

@auth.post("/login")
def login():
    """
    curl -X POST http://localhost:5000/auth/login \
     -H "Content-Type: application/json" \
     -d '{"username": "usuario1", "password": "1234"}'
    """
    db: Session = next(get_db())
    auth_service = AuthService(db)
    data = request.json
    response = auth_service.authenticate_user(
            username= data["username"],
            password= data["password"]
        )
    if response:
        return jsonify({"message": f"Welcome user {data["username"]}", "status": 200}), 200
    return jsonify({"error": "Credenciales inválidas"}), 401