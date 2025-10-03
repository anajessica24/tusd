import csv

# Abrir e ler arquivo 
try:
    with open("tarifas_tusd.csv", "r", encoding="utf-8") as arquivo:
        #tratando o arquivo com a importação csv
        arquivo_csv = csv.reader(arquivo, delimiter=";")
        #ler linhas 
        for i, linha in enumerate(arquivo_csv):
            if i >= 5:
                break
            print(linha)
except UnicodeDecodeError:
    with open("tarifas_tusd.csv", "r", encoding="latin1") as arquivo:
        #tratando o arquivo com a importação csv
        arquivo_csv = csv.reader(arquivo, delimiter=";")
        #ler linhas 
        for i, linha in enumerate(arquivo_csv):
            if i >= 5:
                break
            print(linha)
