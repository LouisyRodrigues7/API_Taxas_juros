# src/extractTransform.py
import requests
import pandas as pd

def requestTaxaJuros(inicio: str, fim: str):
    """
    Extrai dados da API de Taxa de Juros do BCB e retorna um DataFrame.
    """

    filtro = f"InicioPeriodo ge '{inicio}' and FimPeriodo le '{fim}'"
    filtro_encoded = requests.utils.quote(filtro)
    url = f"https://olinda.bcb.gov.br/olinda/servico/taxaJuros/versao/v2/odata/ConsultaUnificada?$top=1000000&$format=json&$filter={filtro_encoded}"
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        df = pd.DataFrame(dados["value"])
        return df
    else:
        raise Exception(f"Erro na requisição: {response.status_code}")
