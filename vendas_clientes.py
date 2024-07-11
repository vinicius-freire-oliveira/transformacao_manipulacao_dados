# Import do pandas
import pandas as pd
# Ler o arquivo json com read_json
dados = pd.read_json('dados_vendas_clientes.json')
# Aplicar json_normalize na coluna dados_vendas
dados = pd.json_normalize(dados['dados_vendas'])
# Mostrar valores
print(dados)

# Coletar os valores das colunas e verificar
colunas = list(dados.columns)
print(colunas)

# Destrinchar as listas com explode
dados = dados.explode(colunas[1:])
# Resetar os index das linhas
dados.reset_index(drop=True,inplace=True)
# Observar o DataFrame
print(dados.head())

# Verificar os tipos de dados com info
print(dados.info())

# A coluna numérica é a 'Valor da compra'
print(dados['Valor da compra'])

# Iniciar a transformação
# Import da biblioteca numpy
import numpy as np
# Remover os textos presentes na base
# Trocar as vírgulas separadoras do decimal por ponto
dados['Valor da compra'] = dados['Valor da compra'].apply(lambda x: x.replace('R$ ', '').replace(',','.').strip())
# Alterar os tipo de dado para float
dados['Valor da compra'] = dados['Valor da compra'].astype(np.float64)
# Verificar a transformação
print(dados.info())

# Transformar os textos de Cliente para texto em minúsculo
dados['Cliente'] = dados['Cliente'].str.lower()
# Verificar o resultado
print(dados.head())

# Opção de substituição - necessário verificar o resultado da substituição
# O regex não seleciona todas as letras de a-z e espaços em branco ' '
# Tudo que satisfaz o regex é apagado
print(dados['Cliente'].str.replace('[^a-z ]', '', regex=True))

# Realizar a substituição dos dados na coluna textual
dados['Cliente'] = dados['Cliente'].str.replace('[^a-z ]', '', regex=True).str.strip()
# Visualizar o resultado final
print(dados.head())

# Transformar para o tipo datetime definindo o formato de data como DD/MM/AAAA ('%d/%m/%Y')
dados['Data de venda'] = pd.to_datetime(dados['Data de venda'], format='%d/%m/%Y')
# Visualizar o resultado
print(dados)

# Verificar o resultado da transformação
print(dados.info())

# Calcular o total arrecadado em compras por cada cliente
total_compras = dados.groupby(['Cliente'])['Valor da compra'].sum()
# Visualizar o resultado
print(total_compras)