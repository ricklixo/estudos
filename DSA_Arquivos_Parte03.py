# IMPORTANDO UM DATASET COM PANDAS.

import pandas as pd

file_name = 'arquivos/binary.csv'

df = pd.read_csv(file_name)

print(df.head()) # apenas imprime as primeiras linhas


# IMPORTANDO OUTRO ARQUIVO

file2 = 'arquivos/salarios.csv'

df = pd.read_csv(file2)

print(df.head())
