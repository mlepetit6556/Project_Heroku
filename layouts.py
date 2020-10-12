#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from app import app
from dash.dependencies import Input, Output

timesData = pd.read_csv("data/timesData.csv")
df2011 = timesData[timesData.year == 2011].iloc[:50,:]
df2012 = timesData[timesData.year == 2012].iloc[:50,:]
df2013 = timesData[timesData.year == 2013].iloc[:50,:]

def layout(data, annee, varx, vary):
    dfyear=data[data.year == annee].iloc[:50, :]
    layout = html.Div([
        dcc.Graph(
            id='plotyear',
            figure={
                'data': [
                    go.Scatter(
                        x=dfyear[dfyear['country'] == i][varx],
                        y=dfyear[dfyear['country'] == i][vary],
                        text=dfyear[dfyear['country'] == i]['university_name'],
                        mode='markers',
                        opacity=0.8,
                        marker={
                            'size': 15,
                            'line': {'width': 0.5, 'color': 'white'}
                        },
                        name=i
                    ) for i in dfyear.country.unique()
                ],
                'layout': go.Layout(
                    xaxis={'title': 'GDP Per Capita'},
                    yaxis={'title': 'Life Expectancy'},
                    #title='Graphe de '+ str(annee) ,
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 1.0, 'y': 0.3},
                    hovermode='closest'
                )
            }
        ),

    html.Div(id='idyear'),
        #dcc.Link('Go to App 2011', href='/apps/2011'),
        #dcc.Link('Go to App 2012', href='/apps/2012'),
        #dcc.Link('Go to App 2013', href='/apps/2013')
    ])
    return(layout)
