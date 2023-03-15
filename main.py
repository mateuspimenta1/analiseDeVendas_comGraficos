import pandas as pd
import plotly.express as px
#passo 1 importar base de dados
tabela = pd.read_csv('clientes.csv', encoding="latin", sep=";")

#deletar coluna inutil
        # axis = 0 se for LINHA, = 1 se for COLUNA
tabela = tabela.drop('Unnamed: 8', axis=1)

"""

            CASO QUEIRA deletar colunas duplicadas
        # drop_duplicated()

"""

# passo 2 visualizar base de dados
# entender as opções disponiveis
# procurar erros na base de dados
print(tabela)
"""Hora de visualizar Relatório"""

#passo 3 tratamento de dados
    #acertar informações que estão sendo reconhecidas de forma errada.


tabela["Salário Anual (R$)"] = pd.to_numeric(tabela["Salário Anual (R$)"], errors='coerce')

            #  CASO QUEIRA DESCOBRIR COLUNAS VAZIAS
        #print(tabela[tabela["Profissão"].isna()])
        #corrigir informações vazias use variavel.dropna()

tabela = tabela.dropna()
print(tabela.info())  #Informação da tabela

# passo 4 análise inicial >
# entender as notas do cliente
# "MEAN" é a media das informações colhidas na tabela, chamamos de Balizador.

print(tabela.describe())

#criar o grafico
    #px.histogram(tabela, x = "Coluna 1" y = "coluna 2")
    #histogram é um grafico que agrupa semelhantes.
    #histfunc é a função que a tabela está operando, o padrão é sempre soma.
    #nbins pra demarcar grupos maiores ou menores,
    #.show() pra mostrar os graficos na tela. (no pycharm necessário instalar """Packaging""" no pip3
for colunas in tabela.columns:
    grafico = px.histogram(tabela, x=colunas, y="Nota (1-100)", histfunc="avg", text_auto=True, nbins=10)
    grafico.show()






# passo 5 analise completa
# entender como cada caracteristica do cliente impacta na nota

"""
            PERFIL IDEAL DO CLIENTE
#acima de 15 anos (não tem diferença entre as faixas etárias depois disso)
#Faixa salárial não parece fazer tanta diferença
#Area de Foco = Entretenimento e Artista, evitar (Cosntrução)
#tem entre 10 e 15 anos de experiência de trabalaho
#Familias não tão grandes, no max 7 pessoas."
"""

