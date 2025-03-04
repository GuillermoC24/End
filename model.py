import joblib

def load_model():
    try:
        # Intentar cargar el modelo entrenado
        model = joblib.load("model.pkl")
    except FileNotFoundError:
        raise FileNotFoundError("El archivo 'model.pkl' no se encontró. Asegúrate de entrenar y guardar el modelo antes de usarlo.")
    return model