import pandas as pd
from model import load_model

def predict(input_data):
    # Cargar el modelo
    model = load_model()
    
    # Hacer la predicción
    predictions = model.predict(input_data)
    return predictions