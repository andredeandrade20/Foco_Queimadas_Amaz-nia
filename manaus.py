import pandas as pd
import numpy as np

### Função para leitura dos dados fornecidos pelo Inmet
def LoadDataInmet(file):
  chunks = []
  for chunk in pd.read_csv(file, encoding = 'latin-1', sep = ';', low_memory = True, chunksize = 1000, skiprows = 4, nrows = 1, ):
    chunks.append(chunk)
  df = pd.concat(chunks)
  return df

manaus_df = LoadDataInmet('C:/Users/Ygoor/Desktop/Facul/PI1/Inmet/INMET_N_AM_A101_MANAUS_01-01-2021_A_31-07-2021.CSV')
print(manaus_df.info())
