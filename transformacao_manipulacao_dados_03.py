# Importa as bibliotecas numpy e pandas, que fornecem ferramentas para análise e manipulação de dados
import numpy as np
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

# Converte a coluna 'max_hospedes' para o tipo inteiro de 64 bits
dados['max_hospedes'] = dados['max_hospedes'].astype(np.int64)
# Exibe informações atualizadas sobre o DataFrame
print(dados.info())

# Lista de colunas que serão convertidas para o tipo inteiro de 64 bits
col_numericas = ['quantidade_banheiros', 'quantidade_quartos', 'quantidade_camas']
# Converte as colunas listadas para o tipo inteiro de 64 bits
dados[col_numericas] = dados[col_numericas].astype(np.int64)

# Converte a coluna 'avaliacao_geral' para o tipo float de 64 bits
dados['avaliacao_geral'] = dados['avaliacao_geral'].astype(np.float64)
# Exibe informações atualizadas sobre o DataFrame
print(dados.info())

# Remove símbolos de dólar e vírgulas da coluna 'preco' e remove espaços em branco
dados['preco'] = dados['preco'].apply(lambda x: x.replace('$', '').replace(',', '').strip())
# Converte a coluna 'preco' para o tipo float de 64 bits
dados['preco'] = dados['preco'].astype(np.float64)
# Exibe informações atualizadas sobre o DataFrame
print(dados.info())

# Remove símbolos de dólar e vírgulas das colunas 'taxa_deposito' e 'taxa_limpeza' e remove espaços em branco
dados[['taxa_deposito', 'taxa_limpeza']] = dados[['taxa_deposito', 'taxa_limpeza']].applymap(lambda x: x.replace('$', '').replace(',', '').strip())
# Converte as colunas 'taxa_deposito' e 'taxa_limpeza' para o tipo float de 64 bits
dados[['taxa_deposito', 'taxa_limpeza']] = dados[['taxa_deposito', 'taxa_limpeza']].astype(np.float64)
# Exibe informações atualizadas sobre o DataFrame
print(dados.info())

# Converte todos os caracteres da coluna 'descricao_local' para minúsculas
dados['descricao_local'] = dados['descricao_local'].str.lower()
# Exibe as primeiras 5 linhas do DataFrame
print(dados.head())

# Exibe o valor da coluna 'descricao_local' na linha 3169
print(dados['descricao_local'][3169])

# Remove todos os caracteres que não sejam letras, números, hifens ou apóstrofos
dados['descricao_local'] = dados['descricao_local'].str.replace('[^a-zA-Z0-9\-\']', ' ', regex=True)
# Substitui hifens que não estão entre palavras por espaços
dados['descricao_local'] = dados['descricao_local'].str.replace('(?<!\w)-(?!\w)', ' ', regex=True)
# Divide as palavras da coluna 'descricao_local' em listas
dados['descricao_local'] = dados['descricao_local'].str.split()
# Exibe as primeiras 5 linhas do DataFrame
print(dados.head())

# Remove chaves e aspas das strings na coluna 'comodidades'
dados['comodidades'] = dados['comodidades'].str.replace('\{|}|\"', '', regex=True)
# Divide as strings da coluna 'comodidades' em listas
dados['comodidades'] = dados['comodidades'].str.split(',')
# Exibe as primeiras 5 linhas do DataFrame
print(dados.head())

# Lê um arquivo JSON contendo dados de móveis disponíveis e armazena em um DataFrame
dt_data = pd.read_json('moveis_disponiveis.json')
# Exibe as primeiras 5 linhas do DataFrame
print(dt_data.head())

# Exibe informações sobre o DataFrame, como colunas, tipos de dados e memória utilizada
print(dt_data.info())

# Converte a coluna 'data' para o tipo datetime
dt_data['data'] = pd.to_datetime(dt_data['data'])
# Exibe informações atualizadas sobre o DataFrame
print(dt_data.info())

# Exibe as primeiras 5 linhas do DataFrame
print(dt_data.head())

# Exibe os valores da coluna 'data' formatados como ano-mês
print(dt_data['data'].dt.strftime('%Y-%m'))

# Agrupa os dados pelo ano-mês e soma a coluna 'vaga_disponivel'
subset = dt_data.groupby(dt_data['data'].dt.strftime('%Y-%m'))['vaga_disponivel'].sum()
# Exibe o resultado do agrupamento
print(subset)
