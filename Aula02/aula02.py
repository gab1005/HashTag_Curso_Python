from IPython.display import display
#import IPython.display as display
import pandas as pd
clientes_df = pd.read_csv('C:/PROGAMACAO/CURSOS/Hashtag_Python/Aula02/aula02_Baixados_Google_drive/ClientesBanco.csv', encoding='latin1')

# .drop() elemina uma coluna ou linha da tabela; o axis= serve para saber se é uma linha (0)
# ou coluna (1)
clientes_df = clientes_df.drop('CLIENTNUM', axis=1)

# para retirar linhas vazias usamos o .dropna()
clientes_df = clientes_df.dropna()
# display(clientes_df.info())
# display(clientes_df.describe())

# display(clientes_df["Categoria"].value_counts())
# display(clientes_df["Categoria"].value_counts(normalize="True"))

# montar grafico para melhor analisar os dados
# documentação: https://plotly.com/python ou https://plotly.com/python/histograms/
import plotly.express as px
def grafico_coluna_categoria(coluna, tabela):
	fig = px.histogram(tabela, x=coluna, color='Categoria')
	fig.show()
for coluna in clientes_df:
	grafico_coluna_categoria(coluna, clientes_df)