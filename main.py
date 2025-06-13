# main.py
import pandas as pd
from src.extractTransform import requestTaxaJuros
from src.load import salvarCsv, salvarSQLite

# Etapa 1: Baixa os dados
df = requestTaxaJuros("2022-01-01", "2025-05-25")

# Etapa 2: Mostra primeiras linhas e tipos
print(df.head())
print(df.dtypes)

# Etapa 3: Converte colunas problemáticas, se houver
# Exemplo: datas, números em string, colunas muito grandes
df_clean = df.copy()

# Converte datas (exemplo)
for col in df_clean.columns:
    if "Data" in col or "data" in col:
        df_clean[col] = pd.to_datetime(df_clean[col], errors="coerce")

# Etapa 4: Salva os dados já tratados
salvarCsv(df_clean, "src/datasets/taxaJuros.csv", ";", ".")
salvarSQLite(df_clean, "src/datasets/taxa_juros.db", "taxa_juros")
