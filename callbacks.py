#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from dash.dependencies import Input, Output

from app import app
import pandas as pd
import plotly.graph_objs as go
from layouts import layout


timesData = pd.read_csv("data/timesData.csv")


@app.callback(
    Output('id2011', 'children'),
    [Input('plot2011', 'value')])

def display_value(value):
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output('id2012', 'children'),
    [Input('plot2012', 'value')])

def display_value(value):
    return 'You have display"{}"'.format(value)


@app.callback(
    Output('plotyear', 'figure'),
    [Input('Radiox', 'value'),
    Input('Radioy', 'value'),
    Input('Annee', 'value'),
     ])
def update_graph(axis_x, axis_y, annee):
    dataFrame = timesData[timesData.year == annee].iloc[:50, :]
    fig = {
        'data':[
            go.Scatter(
                x=dataFrame[dataFrame['country'] == i][axis_x],
                y=dataFrame[dataFrame['country'] == i][axis_y],
                text=dataFrame[dataFrame['country'] == i]['university_name'],
                mode='markers',
                opacity=0.8,
                marker={
                    'size': 15,
                    'line': {'width': 0.5, 'color': 'white'}
                },
                name=i
            ) for i in dataFrame.country.unique()],
           'layout': go.Layout(
               xaxis={'title': axis_x},
               yaxis={'title': axis_y},
               margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
               legend={'x': 1.0, 'y': 0.3},
               hovermode='closest'
           )
        }

    return fig

@app.callback(Output('url', 'pathname'),
              [Input('Annee', 'value'),
               ])
def display_page(annee):
    if annee == 2011:
        return '/apps/2011'
    elif annee == 2012:
        return '/apps/2012'
    elif annee == 2013:
        return '/apps/2013'
