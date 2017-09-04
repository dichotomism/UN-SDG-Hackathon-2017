# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import json

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

import plotly.graph_objs as go

app = dash.Dash()

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

colors = {
    'background': '#FFFFFF',    # white
    'text': '#111111'           # black
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

# import data for use
exec(open("load_data.py").read())

# create base map for country selection
exec(open("map/map.py").read())

app.layout = html.Div(
    style={'backgroundColor': colors['background']}, 
    children=[
        html.H1(
            children='Global Village',
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
        ),

        html.Div('Select your topics:', 
            style={
            'textAlign': 'center',
            'color': colors['text']
            }
        ),

        dcc.Dropdown(
            id = 'select-topic',
            options=[{'label': s, 'value': s} for s in topics],
            multi=True,
        ),

        dcc.Graph(
            id = 'world-map',
            figure=world_map_fig
        ),
        
        html.Div([
            dcc.Markdown("""
                Your country is:
                """.replace('    ', '')),
                html.H3(id = 'click-country'),
            dcc.Markdown("""
                Your topics are:
                """.replace('    ', '')),
                html.H3(id = 'topic-selection'),
            html.H5(id = "country-text")
        ]),
    ])

@app.callback(
    Output('click-country', 'children'),
    [Input('world-map', 'clickData')])
def update_country_click(clickData):
    if clickData is not None:
        return clickData['points'].pop(0)['text']

@app.callback(
    dash.dependencies.Output('country-text', 'children'),
    [dash.dependencies.Input('world-map', 'clickData')])
def update_country_text(dropdown_value):
    if dropdown_value is not None:
        value_text = dropdown_value['points'].pop(0)['text']
    else:
        value_text = ""
    country_text = (simple_wiki[
                        simple_wiki.name == value_text]
                        .clean_summary
                        .values[0])
    return " ".join(
                sent_tokenize(country_text)[:5])

@app.callback(
    Output('topic-selection', 'children'),
    [Input('select-topic', 'value')])
def update_topic(selection):
    return ', '.join(selection)

if __name__ == '__main__':
    app.run_server(debug=True)