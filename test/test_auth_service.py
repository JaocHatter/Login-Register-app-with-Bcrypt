import pytest
from unittest.mock import patch, MagicMock
from flask import Flask
from src.controllers.auth_controller import auth

# Configuración de la aplicación Flask para pruebas
@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(auth)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

# Pruebas para el endpoint /register
@patch("src.controllers.auth_controller.get_db")
@patch("src.controllers.auth_controller.AuthService")
def test_register_success(mock_auth_service, mock_get_db, client):
    mock_service_instance = MagicMock()
    mock_auth_service.return_value = mock_service_instance

    mock_service_instance.register_user.return_value = None

    mock_db_session = MagicMock()
    mock_get_db.return_value = iter([mock_db_session])

    data = {"username": "usuario1", "password": "1234", "email": "usuario1@example.com"}
    response = client.post("/register", json=data)

    assert response.status_code == 201
    assert response.json["message"] == "user created successfully"

    mock_service_instance.register_user.assert_called_once_with(
        username="usuario1",
        password="1234",
        email="usuario1@example.com"
    )

@patch("src.controllers.auth_controller.get_db")
@patch("src.controllers.auth_controller.AuthService")
def test_register_invalid_data(mock_auth_service, mock_get_db, client):
    # Configurar el mock del servicio
    mock_service_instance = MagicMock()
    mock_auth_service.return_value = mock_service_instance

    mock_db_session = MagicMock()
    mock_get_db.return_value = iter([mock_db_session])

    data = {"username": "usuario1"}  # Falta `password` y `email`
    response = client.post("/register", json=data)

    assert response.status_code == 500  
    mock_service_instance.register_user.assert_not_called()

# Pruebas para el endpoint /login
@patch("src.controllers.auth_controller.get_db")
@patch("src.controllers.auth_controller.AuthService")
def test_login_success(mock_auth_service, mock_get_db, client):
    mock_service_instance = MagicMock()
    mock_auth_service.return_value = mock_service_instance

    mock_service_instance.authenticate_user.return_value = {"username": "usuario1"}

    mock_db_session = MagicMock()
    mock_get_db.return_value = iter([mock_db_session])

    data = {"username": "usuario1", "password": "1234"}
    response = client.post("/login", json=data)

    assert response.status_code == 200
    assert "Welcome user usuario1" in response.json["message"]

    mock_service_instance.authenticate_user.assert_called_once_with(
        username="usuario1",
        password="1234"
    )

@patch("src.controllers.auth_controller.get_db")
@patch("src.controllers.auth_controller.AuthService")
def test_login_invalid_credentials(mock_auth_service, mock_get_db, client):
    mock_service_instance = MagicMock()
    mock_auth_service.return_value = mock_service_instance

    mock_service_instance.authenticate_user.return_value = None

    mock_db_session = MagicMock()
    mock_get_db.return_value = iter([mock_db_session])

    data = {"username": "usuario1", "password": "wrong_password"}
    response = client.post("/login", json=data)

    assert response.status_code == 401
    assert response.json["error"] == "Credenciales inválidas"

    mock_service_instance.authenticate_user.assert_called_once_with(
        username="usuario1",
        password="wrong_password"
    )
