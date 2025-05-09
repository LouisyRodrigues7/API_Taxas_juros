import pandas as pd
from src.extractTransform import requestApiTaxaJuros
from src.load import salvarCsv, salvarSQLite, salvarMySQL

dados = requestApiTaxaJuros()

salvarCsv(dados, "src/datasets/taxaJuros.csv", ";", ".")
salvarSQLite(dados, "src/datasets/etltaxajuros.db", "taxa_juros")