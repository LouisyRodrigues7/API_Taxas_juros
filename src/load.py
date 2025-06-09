import sqlite3

def salvarCsv(df, nome_arquivo, separador=",", decimal="."):
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal, index=False, encoding="utf-8")

def salvarSQLite(df, caminho_banco, nome_tabela):
    conn = sqlite3.connect(caminho_banco)
    df.to_sql(nome_tabela, conn, if_exists="replace", index=False)
    conn.close()
