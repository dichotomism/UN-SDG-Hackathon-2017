# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json

import plotly.graph_objs as go

app = dash.Dash()

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

colors = {
    'background': '#FFFFFF',
    'text': '#111111'
}

styles = {
    'column': {
        'display': 'inline-block',
        'width': '33%',
        'padding': 10,
        'boxSizing': 'border-box',
        'minHeight': '200px'
    },
    'pre': {'border': 'thin lightgrey solid'}
}

# create base map for country selection
exec(open("map/map.py").read())

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='Dash: A web application framework for Python.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id = 'world-map',
        figure=fig
    ),
    
    html.Div([
        dcc.Markdown("""
            You just selected:
        """.replace('    ', '')),
        html.H3(id='click-data'),
    ]),

])

@app.callback(
    Output('click-data', 'children'),
    [Input('world-map', 'clickData')])
def display_click_data(clickData):
    return clickData['points'].pop(0)['text']

# @app.callback(
#     Output('click-data', 'children'),
#     [Input('world-map', 'clickData')])
# def display_click_data(clickData):
#     return json.dumps(clickData, indent=2)


if __name__ == '__main__':
    app.run_server(debug=True)