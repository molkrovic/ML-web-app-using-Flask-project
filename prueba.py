import pickle
import pandas as pd 
import numpy as np 

age = 80
sex = 'Female'
bmi = 48.7
children = 8
smoker = 'No'
region = 'Southeast'

if sex.lower() == 'male':
    sex = 1
elif sex.lower() == 'female':
    sex = 0

if smoker.lower() == 'yes':
    smoker = 1
elif smoker.lower() == 'no':
    smoker = 0

region_northeast = 0
region_northwest = 0
region_southeast = 0
region_southwest = 0

if region.lower() == 'northeast':
    region_northeast = 1
elif region.lower() == 'northwest':
    region_northwest = 1
elif region.lower() == 'southeast':
    region_southeast = 1
elif region.lower() == 'southwest':
    region_southwest = 1
else:
    region_northeast = 'Valor incorrecto'


data = [age, sex, bmi, children, smoker, region_northeast, region_northwest, region_southeast, region_southwest]

posted = np.asarray(data).reshape(1,9)

modelo_no_fumador = pickle.load(open('modelo_no_fumador.pkl', 'rb'))
modelo_fumador_bmi_alto = pickle.load(open('modelo_fumador_bmi_alto.pkl', 'rb'))
modelo_fumador_bmi_bajo = pickle.load(open('modelo_fumador_bmi_bajo.pkl', 'rb'))

if smoker == 0:
    modelo = modelo_no_fumador
else:
    if bmi<30:
        modelo = modelo_fumador_bmi_bajo
    else:
        modelo = modelo_fumador_bmi_alto

try:
    result = modelo.predict(posted)
    text_result = result.tolist()[0]
except:
    text_result = 'Invalid values'

print(text_result)