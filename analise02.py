import pandas as pd 

# Permite mostrar todas as linhas
pd.set_option('display.max_rows', None)

# Permite mostrar todas as colunas
pd.set_option('display.max_columns', None)

# Opcional: aumenta a largura da coluna para não quebrar o texto
pd.set_option('display.max_colwidth', None)

try:
    tabela = pd.read_csv("tarifas_tusd.csv", sep=";", encoding="utf-8")
except UnicodeDecodeError:
    tabela = pd.read_csv("tarifas_tusd.csv", sep=";", encoding="latin1")

#print(tabela)

agents = tabela["SigAgente"]
# 2. Ver todos os agentes únicos 
#print("\nDistribuidoras únicas:")
#print(agents.unique())

#Dados ESE
subgrupo_b4 = tabela[tabela['DscSubGrupo'] == 'B4']
ese = subgrupo_b4[subgrupo_b4['SigAgente'] == 'ESE'].copy()
print(ese)