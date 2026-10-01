CREATE DATABASE IF NOT EXISTS esquema_estudiantes_cursos;

USE esquema_estudiantes_cursos;


CREATE TABLE IF NOT EXISTS cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);



CREATE TABLE IF NOT EXISTS estudiantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(45) NOT NULL,
    apellido VARCHAR(45) NOT NULL,
    edad INT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,
    curso_id INT NOT NULL,

    CONSTRAINT fk_estudiantes_curso
        FOREIGN KEY (curso_id)
        REFERENCES cursos(id)
);

-- datitos


INSERT INTO cursos
(nombre)
VALUES
("MERN"),
("Java"),
("Python"),
("Fundamentos de la Web");


INSERT INTO estudiantes
(nombre, apellido, edad, curso_id)
VALUES
("Joe", "Doe", 25, 1),
("Adrian", "Castillo", 26, 1),
("Patricio", "Estrella", 27, 1),
("Kevin", "Torres", 27, 1),
("Andrea", "Pérez", 22, 2),
("Jose", "Kujo", 24, 3);
