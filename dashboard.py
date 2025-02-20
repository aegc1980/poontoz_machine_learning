# dashboard.py
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Poontoz brand color palette
colors = {
    'verde_poontoz': '#004c78',
    'azul_oscuro': '#7fafcc',
    'azul_medio': '#f8fbfc',
    'azul_claro': '#f1523c',
    'rojo': '#e0407c',
    'rosado_socios': '#e7b00f',
    'amarillo_ocre': '#5acdc8',
    'celeste': '#FCEE21'
}

# Sample data
data = [
    {"id": "1", "name": "Club One", "loyalty_details": "Basic loyalty program", "engagement_score": 9},
    {"id": "2", "name": "Club Two", "loyalty_details": "Advanced loyalty program", "engagement_score": 8},
    {"id": "3", "name": "Unknown Club", "loyalty_details": "Missing club name", "engagement_score": 11}
]
df = pd.DataFrame(data)

# Create charts using Plotly Express
fig_bar = px.bar(df, x="name", y="engagement_score", 
                 title="Engagement Score by Club",
                 labels={"name": "Club Name", "engagement_score": "Engagement Score"},
                 color_discrete_sequence=[colors['azul_oscuro']])
fig_hist = px.histogram(df, x="engagement_score", nbins=5, 
                        title="Distribution of Engagement Scores",
                        labels={"engagement_score": "Engagement Score"},
                        color_discrete_sequence=[colors['celeste']])

external_stylesheets = ['https://fonts.googleapis.com/css?family=Nunito+Sans&display=swap']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(style={'backgroundColor': colors['azul_medio'], 'color': colors['verde_poontoz'], 'padding': '20px'}, children=[
    html.H1("Poontoz Analytics Dashboard", style={'textAlign': 'center', 'color': colors['verde_poontoz']}),
    html.Div("An interactive dashboard displaying key metrics for Poontoz.", style={'textAlign': 'center'}),
    dcc.Graph(id='bar-chart', figure=fig_bar),
    dcc.Graph(id='hist-chart', figure=fig_hist)
])

if __name__ == '__main__':
    app.run_server(debug=True, port=8050)
