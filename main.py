from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EntradaConsulta(BaseModel):
    chassi: str
    cnpj: str
    id_cliente: int
    versao: str

banco_simulado = {
    "4NSLX4D07ZI8ZPNPV": {
        "cnpj": "18526066556151",
        "id_cliente": 100,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "Civic 2010"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    },
    "DG2VIM5F7S0YFQCS3": {
        "cnpj": "59355259592915",
        "id_cliente": 101,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Civic 2011"},
            {"chave": "COR_VEICULO", "valor": "Vermelho"}
        ]
    },
    "33X4VP62FRFNTAPQR": {
        "cnpj": "43951627133910",
        "id_cliente": 102,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "Corolla 2012"},
            {"chave": "COR_VEICULO", "valor": "Branco"}
        ]
    },
    "X8I61Q1OLH8MMCZ15": {
        "cnpj": "96585672330485",
        "id_cliente": 103,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "HB20 2013"},
            {"chave": "COR_VEICULO", "valor": "Branco"}
        ]
    },
    "ERK8GLHVDMPZV53GN": {
        "cnpj": "18397969761195",
        "id_cliente": 104,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Onix 2014"},
            {"chave": "COR_VEICULO", "valor": "Azul"}
        ]
    },
    "HNJ9NQJZ7OPDEOKBM": {
        "cnpj": "10780897071284",
        "id_cliente": 105,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "Gol 2015"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    },
    "TYKTXK3KI95JJGPSO": {
        "cnpj": "55232867103307",
        "id_cliente": 106,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "Onix 2016"},
            {"chave": "COR_VEICULO", "valor": "Branco"}
        ]
    },
    "AQPLCYBR7QCZ43JGJ": {
        "cnpj": "73254932628862",
        "id_cliente": 107,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Onix 2017"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    },
    "MC9IHFCII84F2CZHR": {
        "cnpj": "43449747209550",
        "id_cliente": 108,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "Gol 2018"},
            {"chave": "COR_VEICULO", "valor": "Prata"}
        ]
    },
    "TNYLN7IYULG5UQMMF": {
        "cnpj": "45481486294790",
        "id_cliente": 109,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "Corolla 2019"},
            {"chave": "COR_VEICULO", "valor": "Branco"}
        ]
    },
    "WG562CF3MIWEPPFW6": {
        "cnpj": "65726320940850",
        "id_cliente": 110,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Onix 2020"},
            {"chave": "COR_VEICULO", "valor": "Vermelho"}
        ]
    },
    "2N95PR6Y4G0QAGBLV": {
        "cnpj": "67526864950592",
        "id_cliente": 111,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "Corolla 2021"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    },
    "O3ZP3S77NLJZRGRIK": {
        "cnpj": "46135109883418",
        "id_cliente": 112,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "Gol 2022"},
            {"chave": "COR_VEICULO", "valor": "Branco"}
        ]
    },
    "BEOHJS51J4HEIZI23": {
        "cnpj": "52773200425333",
        "id_cliente": 113,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Civic 2023"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    },
    "LR8LNNDW8LT0FXU4A": {
        "cnpj": "05405945932046",
        "id_cliente": 114,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "Corolla 2010"},
            {"chave": "COR_VEICULO", "valor": "Prata"}
        ]
    },
    "TZVB0ORQCMGAUSUA4": {
        "cnpj": "76784420702782",
        "id_cliente": 115,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "Civic 2011"},
            {"chave": "COR_VEICULO", "valor": "Azul"}
        ]
    },
    "T7WSIK4I4JEUMZEMM": {
        "cnpj": "00996177468973",
        "id_cliente": 116,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "HB20 2012"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    },
    "DKATIKD7L8PEQJL2E": {
        "cnpj": "10124917444698",
        "id_cliente": 117,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "Gol 2013"},
            {"chave": "COR_VEICULO", "valor": "Branco"}
        ]
    },
    "QO4ZCDBQ2MZW8TWV8": {
        "cnpj": "86878635417037",
        "id_cliente": 118,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "HB20 2014"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    },
    "NZSQD3Y5HIN72B13C": {
        "cnpj": "88682836786521",
        "id_cliente": 119,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Civic 2015"},
            {"chave": "COR_VEICULO", "valor": "Prata"}
        ]
    },
    "T3KJZDFZ9US1M2FEP": {
        "cnpj": "42817623512585",
        "id_cliente": 120,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "Corolla 2016"},
            {"chave": "COR_VEICULO", "valor": "Azul"}
        ]
    },
    "RC7FS3T23WTRE8OVM": {
        "cnpj": "67846595494309",
        "id_cliente": 121,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "Civic 2017"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    },
    "1NDKGO5RX6FAFAVH8": {
        "cnpj": "93249706713146",
        "id_cliente": 122,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Gol 2018"},
            {"chave": "COR_VEICULO", "valor": "Vermelho"}
        ]
    },
    "82T3G1H8G5WQ3BDW9": {
        "cnpj": "16406770875240",
        "id_cliente": 123,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "HB20 2019"},
            {"chave": "COR_VEICULO", "valor": "Branco"}
        ]
    },
    "GHFCXG2STVC1LD39I": {
        "cnpj": "26221721590407",
        "id_cliente": 124,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "Corolla 2020"},
            {"chave": "COR_VEICULO", "valor": "Azul"}
        ]
    },
    "2K2NPRYX1O0P4HF9D": {
        "cnpj": "00821698604739",
        "id_cliente": 125,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Civic 2021"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    },
    "IJ9JTX8D88FTNZBNS": {
        "cnpj": "08331288934416",
        "id_cliente": 126,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "Onix 2022"},
            {"chave": "COR_VEICULO", "valor": "Branco"}
        ]
    },
    "MHT5SGA3BDQIHRE8L": {
        "cnpj": "95775736189504",
        "id_cliente": 127,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "Gol 2023"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    },
    "KQ3C0M6L42HVKNZ41": {
        "cnpj": "32509836751023",
        "id_cliente": 128,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Corolla 2010"},
            {"chave": "COR_VEICULO", "valor": "Cinza"}
        ]
    },
    "KY5PZ4BOEQQTB7XJN": {
        "cnpj": "73555140820687",
        "id_cliente": 129,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "Civic 2011"},
            {"chave": "COR_VEICULO", "valor": "Prata"}
        ]
    },
    "1AXUS3K0RJWSW1EVD": {
        "cnpj": "31275575974982",
        "id_cliente": 130,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "HB20 2012"},
            {"chave": "COR_VEICULO", "valor": "Branco"}
        ]
    },
    "ZHLCFXCXE0AGHTVK5": {
        "cnpj": "65967823328646",
        "id_cliente": 131,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Corolla 2013"},
            {"chave": "COR_VEICULO", "valor": "Vermelho"}
        ]
    },
    "OJQWZWEG5C0TTTGWD": {
        "cnpj": "20763233282265",
        "id_cliente": 132,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "Gol 2014"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    },
    "AMYZF8CBQXNZBO2YQ": {
        "cnpj": "20940768314866",
        "id_cliente": 133,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "Civic 2015"},
            {"chave": "COR_VEICULO", "valor": "Cinza"}
        ]
    },
    "WZ2X0U0XYT0UQ8VWS": {
        "cnpj": "75490489702110",
        "id_cliente": 134,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Onix 2016"},
            {"chave": "COR_VEICULO", "valor": "Azul"}
        ]
    },
    "FGKAWDLZPJP04OQPH": {
        "cnpj": "26387511405743",
        "id_cliente": 135,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "HB20 2017"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    },
    "Z0F8CD5GMLN1G3LV8": {
        "cnpj": "73469237009052",
        "id_cliente": 136,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "Gol 2018"},
            {"chave": "COR_VEICULO", "valor": "Branco"}
        ]
    },
    "GX42AHPKYQF9W5PJK": {
        "cnpj": "76864374923413",
        "id_cliente": 137,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Civic 2019"},
            {"chave": "COR_VEICULO", "valor": "Cinza"}
        ]
    },
    "5RIWKKD7EOTR4ZP6Z": {
        "cnpj": "28279210894716",
        "id_cliente": 138,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "Corolla 2020"},
            {"chave": "COR_VEICULO", "valor": "Vermelho"}
        ]
    },
    "NLMOGTMI2RZ4PV22W": {
        "cnpj": "88020577512202",
        "id_cliente": 139,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "Onix 2021"},
            {"chave": "COR_VEICULO", "valor": "Branco"}
        ]
    },
    "HTYOV59U4T7R8J5YX": {
        "cnpj": "53823826702731",
        "id_cliente": 140,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "HB20 2022"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    },
    "V5U7R4J6Z4ULANWA9": {
        "cnpj": "91627792438571",
        "id_cliente": 141,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "Gol 2023"},
            {"chave": "COR_VEICULO", "valor": "Azul"}
        ]
    },
    "NQ6N1Y8F0XEZAXZXD": {
        "cnpj": "78912704705961",
        "id_cliente": 142,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "Civic 2010"},
            {"chave": "COR_VEICULO", "valor": "Vermelho"}
        ]
    },
    "S8HJE5KPGXLROWWY9": {
        "cnpj": "51820787935439",
        "id_cliente": 143,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Onix 2011"},
            {"chave": "COR_VEICULO", "valor": "Prata"}
        ]
    },
    "PAJ4L5W7D79C7GGTP": {
        "cnpj": "61330227305790",
        "id_cliente": 144,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "Corolla 2012"},
            {"chave": "COR_VEICULO", "valor": "Cinza"}
        ]
    },
    "JK0H82QFP5QEO8LVY": {
        "cnpj": "15849231662472",
        "id_cliente": 145,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "HB20 2013"},
            {"chave": "COR_VEICULO", "valor": "Azul"}
        ]
    },
    "ZAHDSU8AWK7R35SCG": {
        "cnpj": "97506174673918",
        "id_cliente": 146,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Civic 2014"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    },
    "2SPZJ7MNGX4CO9KZ2": {
        "cnpj": "82301893712707",
        "id_cliente": 147,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "300"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_ERROR"},
            {"chave": "MODELO_VEICULO", "valor": "Corolla 2015"},
            {"chave": "COR_VEICULO", "valor": "Branco"}
        ]
    },
    "UJ6QRC8JZTZMJH9S4": {
        "cnpj": "91322016127967",
        "id_cliente": 148,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "100"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_OK"},
            {"chave": "MODELO_VEICULO", "valor": "Onix 2016"},
            {"chave": "COR_VEICULO", "valor": "Vermelho"}
        ]
    },
    "KTTZP0S8HHR0U9FKP": {
        "cnpj": "00638649528024",
        "id_cliente": 149,
        "versao": "1.0",
        "retorno": [
            {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "200"},
            {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_WARN"},
            {"chave": "MODELO_VEICULO", "valor": "Gol 2017"},
            {"chave": "COR_VEICULO", "valor": "Preto"}
        ]
    }
}

@app.post("/consulta")
def consultar_veiculo(dados: EntradaConsulta):
    if dados.chassi in banco_simulado:
        return {
            "Inputs": {
                "chassi": dados.chassi,
                "cnpj": dados.cnpj,
                "id_cliente": dados.id_cliente,
                "versao": dados.versao
            },
            "Outputs": banco_simulado[dados.chassi]["retorno"]
        }
    else:
        return {
            "Outputs": [
                {"chave": "CALC_SIMULADO_COD_RETORNO", "valor": "404"},
                {"chave": "CALC_SIMULADO_ID_RETORNO", "valor": "RET_NOT_FOUND"},
                {"chave": "MENSAGEM", "valor": "Veículo não encontrado para o chassi informado"}
            ]
        }
