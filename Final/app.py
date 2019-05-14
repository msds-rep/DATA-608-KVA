#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  5 09:23:51 2019

@author: eleanorrsecoquian
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
#import plotly.plotly as py
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

region = ['Europe', 'Africa', 'America', 'Asia', 'Arab']

df = pd.read_csv('https://raw.githubusercontent.com/msds-rep/DATA-608-KVA/master/Final/Data2.csv')


def generate_table(dataframe, max_rows=100):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


    
app.layout = html.Div([
   html.Div([ 
   
           html.H4('Inequality in Education vs Percent of GDP (2017)', className = "six columns", style = {"text-align": "center"} ), 
           
   ], className="row"),
 
        
   html.Div([        
    dcc.Graph(
        id='inq-edu-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    y=df[df['REGION'] == i]['Percent_of_GDP'],
                    x=df[df['REGION'] == i]['Inequality_in_Education'],
                    text=df[df['REGION'] == i]['COUNTRY_NAME'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.REGION.unique()
            ],
            'layout': go.Layout(
                #title='Inequality in Education vs Percent of GDP per Capita',    
                yaxis={'type': 'log', 'title': 'Percent of GDP'},
                xaxis={'title': 'Inequality in Education (%)'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
   ]) ,

   html.Div([ 
   
           html.H4('Inequality in Income vs Percent of GDP (2017)', className = "six columns", style = {"text-align": "center"} ), 
           
   ], className="row"),
   html.Div([        
    dcc.Graph(
        id='inq-inc-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    y=df[df['REGION'] == i]['Percent_of_GDP'],
                    x=df[df['REGION'] == i]['Inequality_in_Income'],
                    text=df[df['REGION'] == i]['COUNTRY_NAME'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.REGION.unique()
            ],
            'layout': go.Layout(   
                yaxis={'type': 'log', 'title': 'Percent of GDP'},
                xaxis={'title': 'Inequality in Income (%)'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
   ]) ,
           
   html.Div([ 
   
           html.H4('Inequality in Life Expectancy vs Percent of GDP (2017)', className = "six columns", style = {"text-align": "center"} ), 
           
   ], className="row"),
   html.Div([        
    dcc.Graph(
        id='inq-lex-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    y=df[df['REGION'] == i]['Percent_of_GDP'],
                    x=df[df['REGION'] == i]['Inequality_in_Life_Expectancy'],
                    text=df[df['REGION'] == i]['COUNTRY_NAME'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.REGION.unique()
            ],
            'layout': go.Layout(   
                yaxis={'type': 'log', 'title': 'Percent of GDP'},
                xaxis={'title': 'Inequality in Life Expectancy (%)'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                #legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
   ]) ,
            
            
   html.Div([
   
           html.H4('Raw Data (2017)'),
           generate_table(df)
           
   ])

            
])

if __name__ == '__main__':
    
    app.run_server(debug=True)