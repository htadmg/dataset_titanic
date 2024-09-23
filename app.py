import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Carregando dataset
url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'
dados = pd.read_csv(url)

# Criando histograma
histograma = px.histogram(dados, x="Age", title="Histograma de Idades", nbins=30)

# Convertendo a coluna "Survived" para string
dados["Survived"] = dados["Survived"].astype(str)

boxplot = px.box(dados, x="Survived", y="Age", color="Survived", title="Boxplot de Idades")

boxplot.update_layout(
    legend_title_text='Sobrevivência',
    legend=dict(
        itemsizing='constant',
        title_font=dict(size=14)
    )
)

boxplot.add_annotation(
    text='0 - Não Sobreviveu <br> 1 - Sobreviveu',
    xref='paper', yref='paper',
    x=0.5, y=1.1,
    showarrow=False,
    font=dict(size=12),
    align='center'
)

dados["Survived"] = dados["Survived"].astype(int)
dados["Pclass"] = dados["Pclass"].astype(int)

sobrevivencia_classe = dados.groupby("Pclass")["Survived"].mean().reset_index()
grafico_classe = px.bar(sobrevivencia_classe, x="Pclass", y="Survived", title="Taxa de Sobrevivência por Classe", labels={"Survived": "Taxa de Sobrevivência"}, text="Survived")

sobrevivencia_sexo = dados.groupby("Sex")["Survived"].mean().reset_index()

grafico_sexo = px.bar(sobrevivencia_sexo, x="Sex", y="Survived", title="Taxa de Sobrevivência por Sexo", labels={"Survived": "Taxa de Sobrevivência"}, text="Survived")




# Inicializando a aplicação Dash
app = Dash(__name__)

# Definindo o layout da aplicação
app.layout = html.Div([
    html.H1("Análise do Dataset Titanic"),
    html.Div([
        html.H2("Histograma de Idades"),
        dcc.Graph(figure=histograma)
    ]),
    html.Div([
        html.H2("Boxplot de Idades"),
        dcc.Graph(figure=boxplot)
    ]),
    html.Div([
        html.H2("Taxa de Sobrevivência por Classe"),
        dcc.Graph(figure=grafico_classe)
    ]), 
    html.Div([
        html.H2("Taxa de Sobrevivência por Sexo"),
        dcc.Graph(figure=grafico_sexo)
    ]),       
])

# Rodando o servidor
if __name__ == '__main__':
    app.run_server(debug=True)
