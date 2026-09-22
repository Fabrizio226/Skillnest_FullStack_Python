# ==========================================================
# MODELO USUARIO
# ==========================================================

from mysqlconnection import connectToMySQL


# ==========================================================
# CLASE USUARIO
# ==========================================================

class Usuario:
    """
    Representa un registro de la tabla usuarios.
    """

    def __init__(self, data):
        """
        Recibe un diccionario proveniente de MySQL
        y lo transforma en un objeto Usuario.
        """
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    # ======================================================
    # READ - OBTENER TODOS LOS USUARIOS
    # ======================================================

    @classmethod
    def get_all(cls):
        """
        Recupera todos los usuarios de la base de datos.
        Retorna una lista de objetos Usuario.
        """
        query = """
            SELECT
                id,
                nombre,
                apellido,
                email,
                created_at,
                updated_at
            FROM usuarios
            ORDER BY id;
        """

        resultados = connectToMySQL("esquema_usuarios").query_db(query)

        # Si ocurre un error o la BD retorna False/None, se devuelve lista vacía
        if not resultados:
            return []

        usuarios = []
        for usuario in resultados:
            usuarios.append(cls(usuario))

        return usuarios

    # ======================================================
    # READ - OBTENER UN SOLO USUARIO POR ID
    # ======================================================

    @classmethod
    def get_one(cls, data):
        """
        Recupera un solo usuario según su ID.
        Recibe un diccionario como: {'id': 1}
        """
        query = """
            SELECT
                id,
                nombre,
                apellido,
                email,
                created_at,
                updated_at
            FROM usuarios
            WHERE id = %(id)s;
        """

        resultados = connectToMySQL("esquema_usuarios").query_db(query, data)

        if not resultados:
            return None

        # Al ser un SELECT por ID, tomamos el primer diccionario obtenido
        return cls(resultados[0])

    # ======================================================
    # CREATE - CREAR NUEVO USUARIO
    # ======================================================

    @classmethod
    def save(cls, data):
        """
        Inserta un nuevo usuario en la base de datos.
        Recibe un diccionario con: nombre, apellido, email.
        Retorna el ID del registro creado.
        """
        query = """
            INSERT INTO usuarios
            (
                nombre,
                apellido,
                email,
                created_at,
                updated_at
            )
            VALUES
            (
                %(nombre)s,
                %(apellido)s,
                %(email)s,
                NOW(),
                NOW()
            );
        """

        return connectToMySQL("esquema_usuarios").query_db(query, data)

    # ======================================================
    # UPDATE - ACTUALIZAR USUARIO
    # ======================================================

    @classmethod
    def update(cls, data):
        """
        Actualiza los datos de un usuario existente.
        Recibe un diccionario con: id, nombre, apellido, email.
        """
        query = """
            UPDATE usuarios
            SET
                nombre = %(nombre)s,
                apellido = %(apellido)s,
                email = %(email)s,
                updated_at = NOW()
            WHERE id = %(id)s;
        """

        return connectToMySQL("esquema_usuarios").query_db(query, data)

    # ======================================================
    # DELETE - ELIMINAR USUARIO
    # ======================================================

    @classmethod
    def delete(cls, data):
        """
        Elimina un usuario de la base de datos por su ID.
        Recibe un diccionario como: {'id': 1}
        """
        query = """
            DELETE FROM usuarios
            WHERE id = %(id)s;
        """

        return connectToMySQL("esquema_usuarios").query_db(query, data)