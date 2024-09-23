from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from pages import graficos, formulario
from app import app


navegacao = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Gráficos", href="/graficos")),
        dbc.NavItem(dbc.NavLink("Formulário", href="/formulario")),
    ],
    brand="Dash Titanic",
    brand_href="#",
    color="primary",
    dark=True,
)

app.layout = html.Div([
    dcc.Location(id="url", refresh=False), 
    navegacao,
    html.Div(id="page-content")
])

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname"),
)
def abre_pagina(pathname):
    if pathname == "/formulario":
        return formulario.layout
    elif pathname == "/graficos":
        return graficos.layout
    else: 
        return graficos.layout
    
if __name__ == "__main__":
    app.run_server(debug=True)