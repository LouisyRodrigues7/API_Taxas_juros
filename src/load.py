import pandas as pd
import sqlite3
import pymysql
from sqlalchemy import create_engine

def salvarCsv(df: pd.DataFrame, caminho: str, sep=";", decimal="."):
    df.to_csv(caminho, sep=sep, decimal=decimal, index=False, encoding="utf-8")

def salvarSQLite(df: pd.DataFrame, caminho_db: str, nome_tabela: str):
    conn = sqlite3.connect(caminho_db)
    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)
    conn.close()

def salvarMySQL(df: pd.DataFrame, usuario, senha, host, banco, nome_tabela):
    engine = create_engine(f"mysql+pymysql://{usuario}:{senha}@{host}/{banco}")
    df.to_sql(nome_tabela, engine, if_exists="replace", index=False)
