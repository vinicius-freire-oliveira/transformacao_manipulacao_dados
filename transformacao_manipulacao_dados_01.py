# Importa a biblioteca pandas, que fornece ferramentas para análise e manipulação de dados
import pandas as pd

# Lê um arquivo JSON contendo dados de hospedagem e armazena em um DataFrame
dados = pd.read_json('dados_hospedagem.json')

# Exibe as primeiras 5 linhas do DataFrame para uma visualização rápida dos dados
print(dados.head())

# Normaliza os dados na coluna 'info_moveis', expandindo listas ou dicionários para colunas separadas
dados = pd.json_normalize(dados['info_moveis'])

# Exibe o DataFrame normalizado
print(dados)
