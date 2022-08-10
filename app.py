import pickle
import numpy as np
from flask import Flask, render_template, request 

app = Flask(__name__, template_folder='')

modelo_no_fumador = pickle.load(open('modelo_no_fumador.pkl', 'rb'))
modelo_fumador_bmi_alto = pickle.load(open('modelo_fumador_bmi_alto.pkl', 'rb'))
modelo_fumador_bmi_bajo = pickle.load(open('modelo_fumador_bmi_bajo.pkl', 'rb'))

@app.route('/') 
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [x for x in request.form.values()]

    if features[1].lower() == 'male':
        features[1] = 1
    elif features[1].lower() == 'female':
        features[1] = 0

    if features[4].lower() == 'yes':
        features[4] = 1
    elif features[4].lower() == 'no':
        features[4] = 0

    for i in range(4):
        features.append(0)
    
    if features[5].lower() == 'northeast':
        features[6] = 1
    elif features[5].lower() == 'northwest':
        features[7] = 1
    elif features[5].lower() == 'southeast':
        features[8] = 1
    elif features[5].lower() == 'southwest':
        features[9] = 1
    else:
        features[9] = 'Valor incorrecto'

    del(features[5])

    for i in [0, 2, 3]:
        features[i] = float(features[i])
    
    final_features = np.asarray(features).reshape(1,9)

    if features[4] == 0:
        modelo = modelo_no_fumador
    else:
        if features[2]<30:
            modelo = modelo_fumador_bmi_bajo
        else:
            modelo = modelo_fumador_bmi_alto
    
    try:
        prediction = modelo.predict(final_features)
        output = prediction.tolist()[0]
    except:
        output = 'Invalid values'

    return render_template('index.html', prediction_text='Estimated charges: {}'.format(output))

if __name__=="__main__":
    app.run(port=5000, debug=True)