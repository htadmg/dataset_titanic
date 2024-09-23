from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import joblib
import pandas as pd
import numpy as np

modelo = joblib.load("model_titanic.pkl")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

formulario = html.Div([
    html.H1("Previsão de Sobrevivência do Titanic"),
    dbc.Container([
        dbc.Row([
            dbc.Col([
                dbc.CardGroup([
                    dbc.Label("Idade"),
                    dbc.Input(id="idade", type="number", placeholder="Digite a idade")
                ], className="mb-3"),

                dbc.CardGroup([
                    dbc.Label("Sexo"),
                    dcc.Dropdown(id="sexo", options=[
                        {'label': 'Masculino', 'value': '1'},
                        {'label': 'Feminino', 'value': '0'},
                    ], placeholder="Selecione o sexo")
                ], className="mb-3"),

                dbc.CardGroup([
                    dbc.Label("Tarifa"),
                    dbc.Input(id="tarifa", type="number", placeholder="Digite a tarifa")
                ], className="mb-3"),

                dbc.CardGroup([
                    dbc.Label("Irmãos/Cônjuges a Bordo"),
                    dbc.Input(id="siblings", type="number", placeholder="Digite o número de Irmãos/Cônjuges")
                ], className="mb-3"),

            ]),

            dbc.Col([
                dbc.CardGroup([
                    dbc.Label("Pais/Filhos a Bordo"),
                    dbc.Input(id="parents", type="number", placeholder="Digite o número de Pais/Filhos")
                ], className="mb-3"),

                 dbc.CardGroup([
                    dbc.Button("Prever", id="botao-prever", color="primary"),
                ], className="mb-3"),

                html.Div(id="resultado", className="mt-3")
            ])

        ])
    ])
])

app.layout = html.Div([
    html.H1("Previsão de Sobrevivência do Titanic", className="text-center mt-5"),
    formulario,
    html.Div(id="previsao")
])

@app.callback(
    Output("previsao", "children"),
    Input("botao-prever", "n_clicks"),
    [
        State("idade", "value"),
        State("sexo", "value"),
        State("classe", "value"),
        State("tarifa", "value"),
        State("siblings", "value"),
        State("parents", "value"),
    ]
)
def prever_sobrevivencia(n_clicks, idade, sexo, classe, tarifa, siblings, parents):
    if n_clicks == 0:
        return ""
    entradas_usuario = pd.DataFrame({
        "Age": [idade],
        "Fare": [tarifa],
        "Siblings/Spouses Aboard": [siblings if siblings is not None else 0], 
        "parents": [parents if parents is not None else 0], 
        "Sex_male": [1 if sexo == "Masculino" else 0],
        "Pclass_2": [1 if classe == "2 Classe" else 0],
        "Pclass_3": [1 if classe == "3 Classe" else 0],        
    })
    entradas_usuario = entradas_usuario[modelo.get_booster().feature_names]

    #fazer previsao

    try: 
        previsao = modelo.predict(entradas_usuario[0])
    except Exception as e:
        return dbc.Alert(f"Ocorreu um erro na previão: {str(e)}", color='danger')
    
    if previsao == 1:
        msg = "Você sobreviveu!"
        cor_alerta = "success"
    else:
        msg = "Você não sobreviveu!"
        cor_alerta = "danger"

    alerta = dbc.Alert(msg, color=cor_alerta, className="d-flex justify-content-center mb-5")

app.run_server(debug=True)
