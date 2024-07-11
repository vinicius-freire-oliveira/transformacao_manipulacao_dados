# Import do pandas
import pandas as pd
# Ler o arquivo json com read_json
dados = pd.read_json('dados_locacao_imoveis.json')
# Aplicar json_normalize na coluna dados_locacao
dados = pd.json_normalize(dados['dados_locacao'])
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

# A coluna numérica é a 'valor_aluguel'
print(dados['valor_aluguel'])

# Iniciar a transformação
# Import da biblioteca numpy
import numpy as np
# Remover os textos presentes na base
# Trocar as vírgulas separadoras do decimal por ponto
dados['valor_aluguel'] = dados['valor_aluguel'].apply(lambda x: x.replace('$ ', '').replace(' reais', '').replace(',','.').strip())
# Alterar os tipo de dado para float
dados['valor_aluguel'] = dados['valor_aluguel'].astype(np.float64)
# Verificar a transformação
print(dados.info())

# Opção de substituição - necessário verificar o resultado da substituição
# Foi necessário adicionar a barra '\' para ser considerados os parênteses como caracteres literais
print(dados['apartamento'].str.replace(' \(blocoAP\)', ''))

# Realizar a substituição dos dados na coluna textual
dados['apartamento'] = dados['apartamento'].str.replace(' \(blocoAP\)', '')
# Visualizar o resultado final
print(dados)

# Transformar para o tipo datetime definindo o formato de data como DD/MM/AAAA ('%d/%m/%Y')
dados['datas_combinadas_pagamento'] = pd.to_datetime(dados['datas_combinadas_pagamento'], format='%d/%m/%Y')
dados['datas_de_pagamento'] = pd.to_datetime(dados['datas_de_pagamento'], format='%d/%m/%Y')
# Visualizar o resultado
print(dados)

# Para contribuir na solução do contexto é possível calcula a diferença de dias
# entre a data combinada e a data de pagamento com dt.days
dados['atraso'] = (dados['datas_de_pagamento'] - dados['datas_combinadas_pagamento']).dt.days
# Observar o novo DataFrame
print(dados.head())

# Calcular a média de tempo de atraso por apartamentos
media_atraso = dados.groupby(['apartamento'])['atraso'].mean()
# Visualizar o resultado
print(media_atraso)

