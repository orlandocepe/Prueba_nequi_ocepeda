# Prueba_nequi_ocepeda
- Repositorio creado para pruebas

# Paso 1: Alcance del proyecto y captura de datos

Dado que el alcance la prueba dependerá en gran medida de los datos, En este paso, debes:
- Identificar y recopilar los datos que usaras para tu proyecto.

Para esta prueba se utilizo el dataset llamado  ** Motor Vehicle Collisions - Crashes ** que esta en la pagina  ** data.gov ** este dataset tiene mas de 2 millones de registros.

**Nota:** en la siguiente **URL** puede descargar el archivo que contriene los datos de la prueba en formato .**csv**

`https://catalog.data.gov/dataset/motor-vehicle-collisions-crashes`


La tabla de accidentes de colisiones de vehículos motorizados contiene detalles sobre el evento del accidente. Cada fila representa un evento de accidente. Las tablas de datos de colisiones de vehículos motorizados contienen información de todas las colisiones de vehículos motorizados reportadas por la policía en la ciudad de Nueva York.



-  Explicar para qué casos de uso final deseas preparar los datos, por ejemplo: tabla de análisis,

En el repositorio esta un archivo Excel llamado tabla de datos donde se encuentra resaltado en amarillo los campos que se utilizaran en el analisis.

En la siguiente **URL** se encuentra la descripcion de los datos tambien.

`https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data`

| Español                       | Column Name                     | Description                                       | Type       |
|-------------------------------|---------------------------------|---------------------------------------------------|------------|
| FECHA DEL ACCIDENTE           | CRASH DATE                      | Occurrence date of collision                      | Date & Time|
| CIUDAD                        | BOROUGH                         | Borough where collision occurred                   | Plain Text ||
| EN EL NOMBRE DE LA CALLE      | ON STREET NAME                  | Street on which the collision occurred            | Plain Text |
| NOMBRE DEL CRUCE DE CALLES    | CROSS STREET NAME               | Nearest cross street to the collision              | Plain Text |
| NOMBRE FUERA DE LA CALLE      | OFF STREET NAME                 | Street address if known                           | Plain Text |
| NÚMERO DE PERSONAS HERIDAS    | NUMBER OF PERSONS INJURED      | Number of persons injured                         | Number     |
| NÚMERO DE PERSONAS MUERTAS    | NUMBER OF PERSONS KILLED       | Number of persons killed                          | Number     |
| NÚMERO DE PEATONES HERIDOS    | NUMBER OF PEDESTRIANS INJURED  | Number of pedestrians injured                     | Number     |
| NÚMERO DE PEATONES MUERTOS    | NUMBER OF PEDESTRIANS KILLED   | Number of pedestrians killed                      | Number     ||

Para proceder a correo el proyecto se debe instalar la libreria ** pandas** y  **logging.**

`pip install pandas`
`pip install logging`

El archivo llamado **Prueba_nequi.py ** tiene todas pas preguntas de analisis que se hizo al datasets con sus respectivas respuestas y logs.

El archivo ** Script.sql ** tiene las creacion de las tablas donde se va almacenar la información.
