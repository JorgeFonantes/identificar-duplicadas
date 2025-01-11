import pandas as pd

# Carregar o arquivo Excel
arquivo = 'RDP-PontosFORMATADO.xlsx'
df = pd.read_excel(arquivo)

# Verificar duplicatas na coluna 'Codigo'
duplicatas = df[df.duplicated(subset='Codigo', keep=False)]

# Exibir as informações duplicadas
if not duplicatas.empty:
    print("Informações duplicadas na coluna 'Codigo':")
    print(duplicatas)
else:
    print("Não há informações duplicadas na coluna 'Codigo'.")
