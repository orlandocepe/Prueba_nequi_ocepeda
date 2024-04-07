import logging
import pandas as pd
import datetime

#Por favor cambiar la ruta del log
Ruta_log='logs/app.log'

#Por favor cambiar la ruta del archivo donde estara el datasets
Ruta_datesets="Motor_Vehicle_Collisions_-_Crashes.csv"

# Configurar el logging
logging.basicConfig(filename=Ruta_log, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

try:
    Archivo=pd.read_csv(Ruta_datesets,delimiter=',',encoding='unicode_escape')
    logging.info('Proceso bien la lectura del archivo ')
    Parte1=Archivo.rename(columns={'CRASH DATE':'FECHA_ACCIDENTE',
                               'BOROUGH':'CIUDAD',
                               'ON STREET NAME':'NOMBRE_CALLE',
                               'NUMBER OF PERSONS INJURED':'NUMERO_PERSONAS_HERIDAS',
                               'NUMBER OF PEDESTRIANS KILLED':'NUMERO_PERSONAS_MUERTAS'})
    logging.info('Proceso bien la parte de renombrar las columnas')

    Valores_columnas=Parte1[['FECHA_ACCIDENTE',
                         'CIUDAD',
                         'NOMBRE_CALLE',
                         'NUMERO_PERSONAS_HERIDAS',
                         'NUMERO_PERSONAS_MUERTAS']]
    logging.info('Proceso bien la parte que filtra los datos para tener menos columnas y mejorar el rendimiento del proceso.')
    ##Borrar nulos
    Valores_columnas_sin_nulos=Valores_columnas.dropna()
    logging.info('Proceso bien la pregunta la limpieza de data nula')

    
    #1.¿Cuáles son las 13 calles donde se registró el mayor número de personas heridas, agrupadas por ciudad?
    print('#¿Cuáles son las 13 calles donde se registró el mayor número de personas heridas, agrupadas por ciudad?\n')
    accidentes_por_calle = Valores_columnas_sin_nulos.groupby(['NOMBRE_CALLE', 'CIUDAD'])['NUMERO_PERSONAS_HERIDAS'].sum()
    print(accidentes_por_calle.nlargest(13), accidentes_por_calle.max(),'\n\n')
    logging.info('Proceso bien la pregunta 1')


    #2.¿Cuales son las 3 ciudad con mas personas heridas?
    print('#¿Cuales son las 3 ciudad con mas personas heridas?\n')
    Ciudades_personas_heridas=Valores_columnas_sin_nulos.groupby('CIUDAD')['NUMERO_PERSONAS_HERIDAS'].sum()
    print(Ciudades_personas_heridas.nlargest(3), Ciudades_personas_heridas.max(),'\n\n')
    logging.info('Proceso bien la pregunta 2')

    
    #3.¿Cuales fue el año donde hubo mas  personas heridas?
    print('#¿Cuales fue el año donde hubo mas  personas heridas?\n')
    ArmarDatos=pd.DataFrame({'Anio':pd.to_datetime(Valores_columnas_sin_nulos['FECHA_ACCIDENTE']).dt.year,
                             'NUMERO_PERSONAS_HERIDAS':Valores_columnas_sin_nulos['NUMERO_PERSONAS_HERIDAS']})
    Valor_Heridos_Anio=ArmarDatos.groupby('Anio')['NUMERO_PERSONAS_HERIDAS'].sum()
    print(Valor_Heridos_Anio.idxmax(),Ciudades_personas_heridas.max(),'\n\n')
    logging.info('Proceso bien la pregunta 3')


    #4.¿Cuáles son las 10 calles donde se registró el mayor número de personas muertas, agrupadas por ciudad?
    print('#¿Cuáles son las 10 calles donde se registró el mayor número de personas muertas, agrupadas por ciudad?\n')
    Muertos = Valores_columnas_sin_nulos.groupby(['NOMBRE_CALLE', 'CIUDAD'])['NUMERO_PERSONAS_MUERTAS'].sum()
    print(Muertos.nlargest(10), Muertos.max(),'\n\n')
    logging.info('Proceso bien la pregunta 4')


    #5.¿Cuales fue el año donde hubo mas  personas muertas?
    print('#¿Cuales fue el año donde hubo mas  personas muertas?\n')
    ArmarDatos2=pd.DataFrame({'Anio':pd.to_datetime(Valores_columnas_sin_nulos['FECHA_ACCIDENTE']).dt.year,
                             'NUMERO_PERSONAS_MUERTAS':Valores_columnas_sin_nulos['NUMERO_PERSONAS_MUERTAS']})
    Valor_Muertos_Anio=ArmarDatos2.groupby('Anio')['NUMERO_PERSONAS_MUERTAS'].sum()
    print(Valor_Muertos_Anio.idxmax(),Valor_Muertos_Anio.max(),'\n\n')
    logging.info('Proceso bien la pregunta 5')

    #6.¿Cules fueron las ciudades que mas presentaron personas fallecidas agrupada por año?
    print('¿Cules fueron las ciudades que mas presentaron personas fallecidas agrupada por año?\n')
    ArmarDatos3 = pd.DataFrame({'Anio': pd.to_datetime(Valores_columnas_sin_nulos['FECHA_ACCIDENTE']).dt.year,
                                'NUMERO_PERSONAS_MUERTAS': Valores_columnas_sin_nulos['NUMERO_PERSONAS_MUERTAS'],
                                'CIUDAD': Valores_columnas_sin_nulos['CIUDAD']})
    SalidaFinal = ArmarDatos3.groupby(['Anio', 'CIUDAD'])['NUMERO_PERSONAS_MUERTAS'].sum()
    print(SalidaFinal.nlargest(10), SalidaFinal.max(),'\n\n')
    logging.info('Proceso bien la pregunta 6')

    logging.info('Proceso finalizado de manera exitosa')




except Exception as e:
    # Registrar la excepción en el archivo de logs de excepciones
    logging.exception("Ocurrió una excepción: %s", str(e))
