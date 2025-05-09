import requests
import pandas as pd

def requestApiTaxaJuros():
    base_url = "https://olinda.bcb.gov.br/olinda/servico/taxaJuros/versao/v2/odata/ConsultaUnificada"
    params = {
        "$format": "json",
        "$select": "InicioPeriodo,FimPeriodo,Segmento,Modalidade,Posicao,InstituicaoFinanceira,TaxaJurosAoMes,TaxaJurosAoAno",
        "$top": 100,
        "$skip": 0
    }

    dados = []

    while True:
        resp = requests.get(base_url, params=params)
        resp.raise_for_status()
        json_data = resp.json()

        if not json_data["value"]:
            break

        dados.extend(json_data["value"])
        params["$skip"] += 100

    df = pd.DataFrame(dados)
    return df
