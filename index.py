#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd

from app import app
from app import server
from layouts import *
import callbacks

timesData = pd.read_csv("data/timesData.csv")

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),

    html.H6("Change the variable for year"),
    dcc.RadioItems(
        options=[
            {'label': '2011', 'value': 2011},
            {'label': '2012', 'value': 2012},
            {'label': '2013', 'value': 2013},
        ],
        value=2011,
        labelStyle={'display': 'inline-block'},
        id='Annee'
    ),
    html.H6("Change the variable for x"),
    dcc.RadioItems(
        options=[
            {'label': 'teaching', 'value': 'teaching'},
            {'label': 'citations', 'value': 'citations'},
            {'label':'international', 'value': 'international'}
            ],
            value='teaching',
            labelStyle = {'display': 'inline-block'},
            id='Radiox'
    ),

    html.H6("Change the variable for y"),
    dcc.RadioItems(
        options=[
            {'label': 'teaching', 'value': 'teaching'},
            {'label': 'citations', 'value': 'citations'},
            {'label':'international', 'value': 'international'}
            ],
            value='international',
            labelStyle={'display': 'inline-block'},
            id='Radioy'
    ),
    html.Div(id='page-content')

])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/2011':
        return layout(timesData, 2011, 'teaching', 'international')
    elif pathname == '/apps/2012':
         return layout(timesData, 2012, 'teaching', 'international')
    elif pathname == '/apps/2013':
        return layout(timesData, 2013, 'teaching', 'international')
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)

