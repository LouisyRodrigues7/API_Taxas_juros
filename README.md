# etlTaxasJurosBCB

Projeto de ETL (Extract, Transform, Load) utilizando dados públicos do Banco Central do Brasil (BACEN) através da [API de Taxas de Juros](https://olinda.bcb.gov.br/olinda/servico/taxaJuros/versao/v2/odata/ConsultaUnificada).

---

## 🚀 Objetivo

Extrair dados de taxas médias de juros por instituição financeira, transformar o conteúdo conforme necessário e armazenar os resultados em `.csv` e/ou banco de dados SQLite, para facilitar análises exploratórias e comparativas.

---

## 📂 Estrutura do Projeto

```
etlTaxasJurosBCB/
├── main.py
├── requirements.txt
├── src/
│   ├── datasets/
│   ├── extractTransform.py
│   └── load.py
├── README.md
```

---

## 🧠 Função Principal: `requestTaxasJuros(filtro: str, ordenacao: str, limite: int)`

📍 Localizada em: `src/extractTransform.py`

### 📥 Parâmetros

- `filtro` (str): Expressão de filtro OData.  
  Ex: `"Segmento eq 'Pessoa Física'"`

- `ordenacao` (str): Coluna e direção para ordenação.  
  Ex: `"TaxaJurosAoAno desc"`

- `limite` (int): Número máximo de registros retornados.  
  Ex: `10`

### ⚙️ Funcionamento

A função realiza requisição para a seguinte rota da API do BACEN:

```
https://olinda.bcb.gov.br/olinda/servico/taxaJuros/versao/v2/odata/ConsultaUnificada
```

Etapas:
1. Constrói a URL com os parâmetros fornecidos.
2. Requisita os dados com `requests`.
3. Converte a resposta para um `DataFrame`.
4. Retorna os dados prontos para uso.

---

## 💾 Salvamento dos Dados

A função `salvarCsv` (em `src/load.py`) recebe o DataFrame e salva o conteúdo no caminho:

```
src/datasets/taxasJuros.csv
```

Separador utilizado: `;`  
Formatação de decimal: `.`

---

## 📊 Dicionário de Dados: `taxasJuros.csv`

| Coluna                 | Descrição                                                                 |
|------------------------|--------------------------------------------------------------------------|
| InicioPeriodo          | Data de início do período analisado                                     |
| FimPeriodo             | Data de fim do período analisado                                        |
| Segmento               | Segmento de cliente (Pessoa Física ou Jurídica)                         |
| Modalidade             | Modalidade de crédito (ex: Cheque especial, Crédito pessoal)            |
| Posicao                | Posição da instituição no ranking para a modalidade                     |
| InstituicaoFinanceira  | Nome da instituição financeira                                          |
| TaxaJurosAoMes         | Taxa média de juros ao mês (%)                                          |
| TaxaJurosAoAno         | Taxa média de juros ao ano (%)                                          |
| cnpj8                  | CNPJ simplificado da instituição (8 primeiros dígitos)                  |

---

## 📊 Exemplos de Análises

### 1. Instituições que mais cobram juros (Pessoa Física)

| Instituição Financeira | Taxa Média Mensal (%) | Taxa Média Anual (%) |
|------------------------|------------------------|-----------------------|
| Banco A                | 4,50                   | 60,00                 |
| Banco B                | 4,20                   | 58,00                 |
| Banco C                | 3,95                   | 55,00                 |

### 2. Instituições com maior volume de operações

| Instituição Financeira | Quantidade de Operações (milhares) |
|------------------------|--------------------------------------|
| Banco X                | 1500                                 |
| Banco Y                | 1200                                 |
| Banco Z                | 1000                                 |

### 3. Modalidades com maiores taxas médias

| Modalidade                   | Taxa Média ao Mês (%) | Taxa Média ao Ano (%) |
|-----------------------------|------------------------|------------------------|
| Cartão de crédito parcelado | 5,00                   | 65,00                  |
| Cheque especial             | 4,80                   | 62,00                  |
| Crédito pessoal consignado  | 3,80                   | 50,00                  |

---

## 📌 Exemplos de Uso dos Parâmetros na API

### Buscar as 10 maiores taxas ao ano para Pessoa Física:

```http
$filter=Segmento eq 'Pessoa Física'&$orderby=TaxaJurosAoAno desc&$top=10
```

### Selecionar dados de uma instituição específica:

```http
$filter=InstituicaoFinanceira eq 'Banco A'&$select=InstituicaoFinanceira,TaxaJurosAoMes,TaxaJurosAoAno
```

---

## ✅ Conclusão

Este projeto fornece uma base sólida para consultar, salvar e analisar as taxas de juros cobradas por instituições financeiras no Brasil. Através dele, é possível identificar padrões de mercado, comparar modalidades de crédito e embasar decisões com dados oficiais do Banco Central.

---