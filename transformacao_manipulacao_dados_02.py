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

# Cria uma lista com os nomes das colunas do DataFrame normalizado
colunas = list(dados.columns)

# Exibe a lista de nomes das colunas
print(colunas)

# "Explode" (expande) as colunas que contêm listas em linhas individuais
dados = dados.explode(colunas[3:])

# Exibe o DataFrame após a expansão das colunas
print(dados)

# Redefine os índices do DataFrame e remove a coluna de índice antiga
dados.reset_index(inplace=True, drop=True)

# Exibe as primeiras 5 linhas do DataFrame com os índices redefinidos
print(dados.head())

# Exibe informações sobre o DataFrame, como colunas, tipos de dados e memória utilizada
print(dados.info())
