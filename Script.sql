Tabla para la pregunta 1: "Calles con mayor número de personas heridas"
sql
Copy code
CREATE TABLE CallesMasHeridas (
    ID INT PRIMARY KEY IDENTITY(1,1),
    NombreCalle NVARCHAR(255),
    Ciudad NVARCHAR(255),
    NumeroPersonasHeridas INT
);

CREATE TABLE CiudadesMasHeridas (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Ciudad NVARCHAR(255),
    NumeroPersonasHeridas INT
);

CREATE TABLE AnioMasHeridas (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Anio INT,
    NumeroPersonasHeridas INT
);

CREATE TABLE CallesMasMuertes (
    ID INT PRIMARY KEY IDENTITY(1,1),
    NombreCalle NVARCHAR(255),
    Ciudad NVARCHAR(255),
    NumeroPersonasMuertas INT
);

CREATE TABLE AnioMasMuertes (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Anio INT,
    NumeroPersonasMuertas INT
);

CREATE TABLE CiudadesMasMuertesPorAnio (
    ID INT PRIMARY KEY IDENTITY(1,1),
    Anio INT,
    Ciudad NVARCHAR(255),
    NumeroPersonasMuertas INT
);