from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EntradaConsulta(BaseModel):
    chassi: str
    cnpj: str
    id_cliente: int
    versao: str

@app.post("/consulta")
def consultar_veiculo(dados: EntradaConsulta):
    return {
        "Outputs": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "Onix LT 2018"},
            {"chave": "COR_VEICULO", "valor": "Prata"}
        ]
    }
