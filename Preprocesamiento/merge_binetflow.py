import os
import pandas as pd

# Directorio donde están los archivos CSV
DIRECTORIO = "./CTU13"

# Lista para almacenar los DataFrames
dataframes = []

# Iterar sobre los archivos en el directorio
for archivo in os.listdir(DIRECTORIO):
    if archivo.endswith(".binetflow"):  # Filtrar solo archivos CSV
        ruta_completa = os.path.join(DIRECTORIO, archivo)
        print(f"Leyendo: {ruta_completa}")
        
        # Leer el CSV y añadirlo a la lista
        df = pd.read_csv(ruta_completa)
        print(df.shape)
        dataframes.append(df)

# Concatenar los DataFrames en uno solo
if dataframes:
    df_final = pd.concat(dataframes, ignore_index=True)
    print("Archivos concatenados correctamente.")
    
    # Guardar en un nuevo archivo CSV
    df_final.to_csv(os.path.join(DIRECTORIO, "concatenado.csv"), index=False)
    print("Archivo guardado como 'concatenado.csv'")
else:
    print("No se encontraron archivos CSV en el directorio.")
