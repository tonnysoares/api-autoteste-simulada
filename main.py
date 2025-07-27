from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

banco_simulado = {
    "iphone-16": {
        "modelo": "iPhone 16",
        "referencia": "A3160",
        "ram_gb": 6,
        "armazenamento_gb": 128,
        "processador": "A18 Bionic",
        "tela_polegadas": 6.1,
        "resolucao_display": "2532x1170",
        "ppi": 460,
        "bateria_mah": 3300,
        "camera_traseira_mp": ["48MP", "12MP"],
        "camera_frontal_mp": "12MP",
        "conectividade": ["5G", "WiFi 6E", "Bluetooth 5.3", "NFC"],
        "peso_g": 173,
        "dimensoes_mm": "146.7x71.5x7.7",
        "certificacao_ip": "IP68"
    },
    "iphone-16-pro": {
        "modelo": "iPhone 16 Pro",
        "referencia": "A3161",
        "ram_gb": 8,
        "armazenamento_gb": 256,
        "processador": "A18 Pro",
        "tela_polegadas": 6.1,
        "resolucao_display": "2556x1179",
        "ppi": 460,
        "bateria_mah": 3350,
        "camera_traseira_mp": ["48MP", "12MP", "12MP"],
        "camera_frontal_mp": "12MP",
        "conectividade": ["5G", "WiFi 6E", "Bluetooth 5.3", "NFC"],
        "peso_g": 187,
        "dimensoes_mm": "146.6x70.6x7.8",
        "certificacao_ip": "IP68"
    },
    "iphone-16-pro-max": {
        "modelo": "iPhone 16 Pro Max",
        "referencia": "A3162",
        "ram_gb": 8,
        "armazenamento_gb": 512,
        "processador": "A18 Pro",
        "tela_polegadas": 6.7,
        "resolucao_display": "2796x1290",
        "ppi": 460,
        "bateria_mah": 4350,
        "camera_traseira_mp": ["48MP", "12MP", "12MP", "TOF 3D"],
        "camera_frontal_mp": "12MP",
        "conectividade": ["5G", "WiFi 6E", "Bluetooth 5.3", "NFC"],
        "peso_g": 221,
        "dimensoes_mm": "160.7x77.6x7.9",
        "certificacao_ip": "IP68"
    },
    "galaxy-s24-ultra": {
        "modelo": "Galaxy S24 Ultra",
        "referencia": "SM-S928B",
        "ram_gb": 12,
        "armazenamento_gb": 512,
        "processador": "Snapdragon 8 Gen 3",
        "tela_polegadas": 6.8,
        "resolucao_display": "3120x1440",
        "ppi": 505,
        "bateria_mah": 5000,
        "camera_traseira_mp": ["200MP", "12MP", "10MP", "50MP"],
        "camera_frontal_mp": "12MP",
        "conectividade": ["5G", "WiFi 7", "Bluetooth 5.3", "NFC"],
        "peso_g": 232,
        "dimensoes_mm": "162.3x79x8.6",
        "certificacao_ip": "IP68"
    },
    "galaxy-s25-ultra": {
        "modelo": "Galaxy S25 Ultra",
        "referencia": "SM-S938B",
        "ram_gb": 16,
        "armazenamento_gb": 1024,
        "processador": "Snapdragon 8 Gen 4",
        "tela_polegadas": 6.9,
        "resolucao_display": "3200x1440",
        "ppi": 515,
        "bateria_mah": 5100,
        "camera_traseira_mp": ["250MP", "12MP", "50MP", "50MP"],
        "camera_frontal_mp": "12MP",
        "conectividade": ["5G", "WiFi 7", "Bluetooth 5.4", "NFC"],
        "peso_g": 235,
        "dimensoes_mm": "163.4x80.3x8.8",
        "certificacao_ip": "IP68"
    }
}

class ModeloConsulta(BaseModel):
    modelo: str

@app.get("/consulta/{modelo}")
def consultar_aparelho(modelo: str):
    modelo_key = modelo.lower().replace(" ", "-")
    if modelo_key not in banco_simulado:
        raise HTTPException(status_code=404, detail="Modelo não encontrado")
    return banco_simulado[modelo_key]
