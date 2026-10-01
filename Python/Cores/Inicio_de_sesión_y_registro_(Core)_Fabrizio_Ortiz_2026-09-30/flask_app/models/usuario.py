from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from datetime import datetime, date
import os
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$')
PASSWORD_REGEX = re.compile(r'^(?=.*[A-Z])(?=.*\d).+$')

class Usuario:
    DB = os.getenv('DB_NAME', 'esquema_login_registro')

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.password = data['password']
        self.fecha_nacimiento = data.get('fecha_nacimiento')
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def guardar(cls, data):
        query = """
            INSERT INTO usuarios (nombre, apellido, email, password, fecha_nacimiento)
            VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, %(fecha_nacimiento)s);
        """
        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def obtener_por_email(cls, email):
        query = "SELECT * FROM usuarios WHERE email = %(email)s;"
        results = connectToMySQL(cls.DB).query_db(query, {'email': email})
        if not results or len(results) < 1:
            return False
        return cls(results[0])

    @classmethod
    def obtener_por_id(cls, usuario_id):
        query = "SELECT * FROM usuarios WHERE id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, {'id': usuario_id})
        if not results or len(results) < 1:
            return False
        return cls(results[0])

    @staticmethod
    def validar_registro(form_data):
        is_valid = True

        if len(form_data['nombre'].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "register")
            is_valid = False
        elif not NAME_REGEX.match(form_data['nombre']):
            flash("El nombre solo debe contener letras.", "register")
            is_valid = False

        if len(form_data['apellido'].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "register")
            is_valid = False
        elif not NAME_REGEX.match(form_data['apellido']):
            flash("El apellido solo debe contener letras.", "register")
            is_valid = False

        if not EMAIL_REGEX.match(form_data['email']):
            flash("Formato de correo electrónico inválido.", "register")
            is_valid = False
        elif Usuario.obtener_por_email(form_data['email']):
            flash("El correo electrónico ya está registrado.", "register")
            is_valid = False

        if len(form_data['password']) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "register")
            is_valid = False
        elif not PASSWORD_REGEX.match(form_data['password']):
            flash("La contraseña debe incluir al menos un número y una mayúscula.", "register")
            is_valid = False

        if form_data['password'] != form_data['confirm_password']:
            flash("Las contraseñas no coinciden.", "register")
            is_valid = False

        if form_data.get('fecha_nacimiento'):
            try:
                dob = datetime.strptime(form_data['fecha_nacimiento'], '%Y-%m-%d').date()
                today = date.today()
                age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
                if age < 18:
                    flash("Debes tener al menos 18 años para registrarte.", "register")
                    is_valid = False
            except ValueError:
                flash("Fecha de nacimiento no válida.", "register")
                is_valid = False

        return is_valid