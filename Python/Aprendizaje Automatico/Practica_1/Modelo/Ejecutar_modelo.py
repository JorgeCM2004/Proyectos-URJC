import pandas as pd
import pickle
import sklearn

def preprocesado_sin_pikcle(df: pd.DataFrame) -> pd.DataFrame:
    # Copiamos las listas creadas en el Notebook.
    atributos_categoricos = ['pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']
    atributos_no_significativos = ['rbc', 'rbcc']
    atributos_numericos = ['age', 'bp', 'sg', 'al', 'su', 'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wbcc']
    columnas_numericas = ['age', 'bp', 'sg', 'al', 'su', 'bgr', 'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wbcc', 'rbcc']

    # Sustituimos los ? por Nulos.
    df.replace('?', pd.NA, inplace=True)

    # Transformamos las columnas numericas a numeros.
    df[columnas_numericas] = df[columnas_numericas].apply(pd.to_numeric, errors='coerce')

    # Quitamos los atributos no significativos.
    df.drop(atributos_no_significativos, axis = 1, inplace = True)

    # Rellenamos los valores nulos con la media en los atributos tipo numericos.
    df[atributos_numericos] = df[atributos_numericos].fillna(df[atributos_numericos].mean())

    # Rellenamos los valores nulos con la media en los atributos tipo numericos.
    df[atributos_categoricos] = df[atributos_categoricos].fillna(df[atributos_categoricos].mode().iloc[0])

    return df

# Ruta y leemos csv.
ruta_archivo_csv = "./testX_reto1.csv"
df = pd.read_csv(ruta_archivo_csv, delimiter=';')

# Hacemos el preprocesado sin objetos con pandas.
df = preprocesado_sin_pikcle(df)

# Cargamos los objetos.
with open('./objetos.pkl', 'rb') as archivo:
    label_encoders_X = pickle.load(archivo)
    reg_logi = pickle.load(archivo)
    label_encoder_Y = pickle.load(archivo)

# Usamos los labels encoders almacenados para codificar los atributos categoricos.
atributos_categoricos = ['pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']
for i in range(len(atributos_categoricos)):
    df[atributos_categoricos[i]] = label_encoders_X[i].transform(df[atributos_categoricos[i]])
    
# Hacemos la predicción.
y_hat_test = reg_logi.predict(df)

# Decodificamos los resultados.
y_hat_decoded = label_encoder_Y.inverse_transform(y_hat_test)

# Lo cargamos en un DataFrame, concatenamos los índices y renombramos las columas para que sean idénticas a 'trainY_reto1.csv'.
y_pred = pd.DataFrame(y_hat_decoded, columns=['class'])
df_predicciones = pd.concat([df['Unnamed: 0'].reset_index(drop=True), y_pred], axis=1)
df_predicciones = df_predicciones.rename(columns={'Unnamed: 0': ''})

# Convertimos el DataFrame a un CSV separado por ';'.
df_predicciones.to_csv('retoML1_Y_test.csv', index = False, sep = ';')   