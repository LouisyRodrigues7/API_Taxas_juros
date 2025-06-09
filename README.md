# etlBCB
Projeto de ETL (Extract, Transform, Load) utilizando dados públicos do Banco Central do Brasil (BACEN) através da API na aula de DataScienc [Dados Abertos de Meios de Pagamento](https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/documentacao).

---

## 🚀 Objetivo

Extrair os dados de meios de pagamento para um trimestre específico, transformar o conteúdo conforme necessário e armazenar em um arquivo `.csv`, que pode ser utilizado em análises futuras.

---

## 📂 Estrutura do Projeto
etlBCB/ ├── main.py ├── requirements.txt ├── src/ │ ├── datasets/ │ ├── extractTransform.py │ └── load.py ├── README.md

---

## 🧠 Função Principal: `requestApiBcb(trimestre)`

📍 Localizada em: `src/extractTransform.py`

### 📥 Parâmetro

- `trimestre` (str): Trimestre no formato `YYYYT`, onde:
  - `YYYY` representa o ano
  - `T` representa o número do trimestre (1 a 4)
  - Exemplo: `'20191'` representa o primeiro trimestre de 2019.

### ⚙️ Funcionamento

A função realiza uma requisição à API do BACEN, especificamente na rota:
https://olinda.bcb.gov.br/olinda/servico/MPV_DadosAbertos/versao/v1/odata/MeiosPagamentosPorTrimestre(Tri=%27{trimestre}%27)?$format=json


Etapas:
1. Requisita os dados do trimestre informado.
2. Converte a resposta para um DataFrame com o `pandas`.
3. Retorna os dados para posterior salvamento.

---

## 💾 Salvamento dos Dados

A função `salvarCsv` (em `src/load.py`) recebe os dados extraídos e salva no caminho:
src/datasets/meiosPagamentosTri.csv


Separador utilizado: `;`  
Formatação de decimal: `.`

---

## 📊 Dicionário de Dados: `meiosPagamentosTri.csv`

| Coluna                 | Descrição                                                    | Tipo     |
|------------------------|---------------------------------------------------------------|----------|
| Ano                    | Ano de referência                                             | Inteiro  |
| Trimestre              | Trimestre de referência (1 a 4)                               | Inteiro  |
| ModalidadePagamento    | Modalidade de pagamento (ex: cartão de crédito, boleto etc.) | Texto    |
| QuantidadeTransacoes   | Quantidade total de transações                               | Inteiro  |
| ValorTransacoes        | Valor total das transações (R$)                              | Float    |
| UnidadeFederativa      | Estado da federação (sigla, ex: SP, RJ)                      | Texto    |

---
---

## 📊 Resultado Adicional 

| Nome             | Tipo     | Título                 | Descrição                                                                                                                                                                                                                                                                                                                                                                  |
|------------------|----------|------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| AnoMes           | texto    | Ano-Mês                | Mês e ano de referência dos dados (formato AAAAMM).                                                                                                                                                                                                                                                                                                                         |
| quantidadePix    | decimal  | Quantidade Pix         | Quantidade (em milhares) de transações Pix liquidadas mensalmente no SPI e fora do SPI, considerando ordens de pagamento e devoluções no período. Dados referentes às transações liquidadas fora do SPI estão sujeitas a alterações retroativas, pois dependem da prestação de informação pelos participantes.                     |
| valorPix         | decimal  | Valor Pix              | Volume financeiro (R$ milhões) de transações Pix liquidadas mensalmente no SPI e fora do SPI, considerando ordens de pagamento e devoluções no período. Dados referentes às transações liquidadas fora do SPI estão sujeitas a alterações retroativas, pois dependem da prestação de informação pelos participantes.                |
| quantidadeTED    | decimal  | Quantidade TED         | Quantidade (em milhares) de transferências por meio de TED realizadas mensalmente. Utilizada para transferir valores entre correntistas de diferentes instituições, envolvendo ou não pagamento de obrigações.                                                                                                                         |
| valorTED         | decimal  | Valor TED (R$)         | Montante financeiro (R$ milhões) transferido por meio de TED mensalmente.                                                                                                                                                                                                                                                            |
| quantidadeTEC    | decimal  | Quantidade TEC         | Quantidade (em milhares) de transferências por meio de TEC realizadas mensalmente. TEC é usada por empresas para pagamento de benefícios aos empregados.                                                                                                                                                                              |
| valorTEC         | decimal  | Valor TEC              | Montante financeiro (R$ milhões) transferido por meio de TEC mensalmente.                                                                                                                                                                                                                                                            |
| quantidadeCheque | decimal  | Quantidade de Cheques  | Quantidade (em milhares) de cheques interbancários compensados mensalmente.                                                                                                                                                                                                                                                          |
| valorCheque      | decimal  | Valor Cheques          | Montante financeiro (R$ milhões) de cheques interbancários compensados mensalmente.                                                                                                                                                                                                                                                  |
| quantidadeBoleto | decimal  | Quantidade Boletos     | Quantidade (em milhares) de boletos interbancários liquidados mensalmente.                                                                                                                                                                                                                                                           |
| valorBoleto      | decimal  | Valor Boletos          | Montante financeiro (R$ milhões) dos boletos interbancários liquidados mensalmente.                                                                                                                                                                                                                                                  |
| quantidadeDOC    | decimal  | Quantidade DOC         | Quantidade (em milhares) de transferências realizadas por meio de DOC mensalmente.                                                                                                                                                                                                                                                   |
| valorDOC         | decimal  | Valor DOC              | Montante financeiro (R$ milhões) transferido por meio de DOC mensalmente.                                                                                                                                                                                                                                                            |

---




