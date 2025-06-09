# src/extractTransform.py
import requests
import pandas as pd

def requestTaxaJuros():
    """
    Extrai dados da API de Taxa de Juros do BCB e retorna um DataFrame.
    """
    url = "https://olinda.bcb.gov.br/olinda/servico/taxaJuros/versao/v2/odata/ConsultaUnificada?$top=10000&$format=json"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        df = pd.DataFrame(dados["value"])
        return df
    else:
        raise Exception(f"Erro na requisição: {response.status_code}")
