import numpy as np
#from flask import Flask, request, jsonify, render_template, url_for
import streamlit as st
#import joblib
import pickle
#from sklearn import svm
import streamlit as st
#from tensorflow.keras.models import load_model
#model = load_model("modelo.h5")
# Path del modelo preentrenado
MODEL_PATH = 'modelodesnInfSVC.pkl'
#model = joblib.load(MODEL_PATH)
# Se recibe la imagen y el modelo, devuelve la predicción
def model_prediction(x_in, model):
    x = np.asarray(x_in).reshape(1,-1)
    preds=model.predict(x)
    return preds
def main():
    model=''

    # Se carga el modelo
    if model=='':
        MODEL_PATH = 'modelodesnInfSVC.pkl'
       # model = joblib.load(MODEL_PATH)
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
      
       

 #MODEL_PATH = 'modelodesnInfSVC.pkl'

 
    
    # Título
    html_temp = """
    <h1 style="color:#181082;text-align:center;">SISTEMA PARA DIAGNOSTICO DE DESNUTRICION INFANTIL </h1>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
  #  peso	estatura	tipo_des	Edad_dias	grupo_edad	sexo

    # Lecctura de datos
    #Datos = st.text_input("Ingrese los valores : Sexo, edad, etc:")
    P = st.text_input("Peso")
    E = st.text_input("Estatura")
    D = st.text_input("Edad en dias")
    GE = st.text_input("Grupo Edad")
    S = st.text_input("Sexo")
    # El botón predicción se usa para iniciar el procesamiento
    if st.button("Predicción :"): 

        #x_in = list(np.float_((Datos.title().split('\t'))))
        P  = 0 if P == "" else float(P)
        E  = 0 if E == "" else float(E)
        D  = 0 if D == "" else float(D)
        GE = 0 if GE == "" else float(GE)
        S  = 0 if S == "" else float(S)

        x_in = [[P, E, D, GE, S]]
        predictS = model_prediction(x_in, model)
        st.success('Su diagnostico es : {}'.format(predictS[0]).upper())

if __name__ == '__main__':
    main()
