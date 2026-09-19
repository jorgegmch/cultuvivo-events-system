import os
import json
from datetime import datetime

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause():
    input("Presione ENTER para continuar...")

def validador_capacidadmaxima(capacidad):
    try:
        return int(capacidad) > 0
    except ValueError:
        return False

def validador_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validador_hora(hora):
    try:
        datetime.strptime(hora, "%H:%M")
        return True
    except ValueError:
        return False

def asignar_boleto():
    pass

def validador_imput():
    pass

def escribir_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def leer_json(filename):
    with open(filename, 'r') as f:
        return json.load(f)