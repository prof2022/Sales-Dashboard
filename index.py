import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
import numpy as np
import pathlib

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("./data").resolve()

data = pd.read_csv(DATA_PATH.joinpath('sales_data.csv'))

# Remove last row
data.drop(data.index[-1], inplace = True)

# Remove commas from columns
data['Revenues'] = data['Revenues'].str.replace(',', '')
data['Total Cost (Sales & Marketing)'] = data['Total Cost (Sales & Marketing)'].str.replace(',', '')
data['Target'] = data['Target'].str.replace(',', '')

# Change data type of columns
data['Revenues'] = data['Revenues'].astype('int64')
data['Total Cost (Sales & Marketing)'] = data['Total Cost (Sales & Marketing)'].astype('int64')
data['Orders Placed'] = data['Orders Placed'].astype('int64')
data['Customers'] = data['Customers'].astype('int64')
data['Purchased Items'] = data['Purchased Items'].astype('int64')
data['Inquiries'] = data['Inquiries'].astype('int64')
data['Target'] = data['Target'].astype('int64')
data['Lead'] = data['Lead'].astype('int64')
data['Opportunity'] = data['Opportunity'].astype('int64')

# print(data['Conversion Rate'])

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)

app.layout = html.Div((
    html.Div([
        html.Div([
            html.Img(src = app.get_asset_url('statistics.png'),
                     style = {'height': '30px'},
                     className = 'title_image'
                     ),
            html.H6('KPI Sales Dashboard',
                    style = {'color': 'white'},
                    className = 'title'
                    ),
        ], className = 'logo_title'),

        html.Div([
            html.P('Select Month',
                   style = {'color': 'white'},
                   className = 'drop_down_list_title'
                   ),
            dcc.Dropdown(id = 'select_month',
                         multi = False,
                         clearable = True,
                         disabled = False,
                         style = {'display': True},
                         value = 'MAR',
                         placeholder = 'Select Month',
                         options = [{'label': c, 'value': c}
                                    for c in data['Months'].unique()],
                         className = 'drop_down_list'),
        ], className = 'title_drop_down_list'),
    ], className = 'title_and_drop_down_list'),

    html.Div([
        html.Div([
            html.Div(id = 'text1',
                     className = 'card_size'),
            html.Div([
                dcc.Graph(id = 'chart1',
                          config = {'displayModeBar': False}),
            ], className = 'chart')
        ], className = 'text_graph_column'),

        html.Div([
            html.Div(id = 'text2',
                     className = 'card_size'),
            html.Div([
                dcc.Graph(id = 'chart2',
                          config = {'displayModeBar': False}),
            ], className = 'chart')
        ], className = 'text_graph_column'),

        html.Div([
            html.Div(id = 'text3',
                     className = 'card_size'),
            html.Div([
                dcc.Graph(id = 'chart3',
                          config = {'displayModeBar': False}),
            ], className = 'chart')
        ], className = 'text_graph_column'),

        html.Div([
            html.Div(id = 'text4',
                     className = 'card_size'),
            html.Div([
                dcc.Graph(id = 'chart4',
                          config = {'displayModeBar': False}),
            ], className = 'chart')
        ], className = 'text_graph_column'),

        html.Div([
            html.Div(id = 'text5',
                     className = 'card_size'),
            html.Div([
                dcc.Graph(id = 'chart5',
                          config = {'displayModeBar': False}),
            ], className = 'chart')
        ], className = 'text_graph_column'),

        html.Div([
            html.Div(id = 'text6',
                     className = 'card_size'),
            html.Div([
                dcc.Graph(id = 'chart6',
                          config = {'displayModeBar': False}),
            ], className = 'chart')
        ], className = 'text_graph_column'),

    ], className = 'flex_container'),

    html.Div([
        html.Div([
            html.Div([
                dcc.Graph(id = 'donut_chart1',
                          config = {'displayModeBar': False},
                          className = 'donut_chart_size'),
                html.Div(id = 'donut_chart_text1',
                         className = 'donut_chart_text')
            ], className = 'chart_container'),

            html.Div([
                dcc.Graph(id = 'donut_chart2',
                          config = {'displayModeBar': False},
                          className = 'donut_chart_size'),
                html.Div(id = 'donut_chart_text2',
                         className = 'donut_chart_text')
            ], className = 'chart_container'),

            html.Div([
                dcc.Graph(id = 'donut_chart3',
                          config = {'displayModeBar': False},
                          className = 'donut_chart_size'),
                html.Div(id = 'donut_chart_text3',
                         className = 'donut_chart_text')
            ], className = 'chart_container')
        ], className = 'donut_chart_column'),

        html.Div([
            dcc.Graph(id = 'funnel_chart',
                      config = {'displayModeBar': False},
                      className = 'funnel_chart_size'),
            dcc.Graph(id = 'bar_chart',
                      config = {'displayModeBar': False},
                      className = 'bar_chart_size'),
        ], className = 'funnel_bar_chart_column'),

        html.Div([
            dcc.Graph(id = 'stack_bar_chart',
                      config = {'displayModeBar': False},
                      className = 'stack_bar_chart_size'),
            html.Div([
                dcc.Graph(id = 'percent_bar_chart',
                          config = {'displayModeBar': False},
                          className = 'percent_bar_chart_size'),
                html.Div([
                    html.Div([
                        html.Div(className = 'background_size1'),
                        html.Div([
                            html.Div(id = 'chart_text1',
                                     className = 'chart_text1'),
                            dcc.Graph(id = 'average_sales_bar_chart1',
                                      config = {'displayModeBar': False},
                                      className = 'average_sales_bar_chart1'),
                        ], className = 'average_sales_bar_chart_row1')
                    ], className = 'average_sales_bar_chart_column1'),
                    html.Div([
                        html.Div(className = 'background_size2'),
                        html.Div([
                            html.Div(id = 'chart_text2',
                                     className = 'chart_text2'),
                            dcc.Graph(id = 'average_sales_bar_chart2',
                                      config = {'displayModeBar': False},
                                      className = 'average_sales_bar_chart2'),
                        ], className = 'average_sales_bar_chart_row2')
                    ], className = 'average_sales_bar_chart_column2')
                ], className = 'average_sales_chart_column')
            ], className = 'average_sales_row')
        ], className = 'bar_chart_column')
    ], className = 'create_row')

))


@app.callback(Output('text1', 'children'),
              [Input('select_month', 'value')])
def update_text(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        # Calculate difference between two months
        data['Revenues_Difference'] = data['Revenues'].diff()
        # Calculate percentage change difference between two months
        data['pct_Difference'] = (data['Revenues'].pct_change()) * 100
        data['Revenues_Difference'] = data['Revenues_Difference'].fillna(0)
        filter_month = data[data['Months'] == select_month]
        revenues = filter_month['Revenues'].iloc[0]
        revenues_difference = filter_month['Revenues_Difference'].iloc[0]
        revenues_pct_change = filter_month['pct_Difference'].iloc[0]

    if revenues_difference > 0:
        return [
            html.P('Revenues',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('${0:,.0f}'.format(revenues),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),

                html.Div([
                    html.I(className = "fas fa-caret-up",
                           style = {"font-size": "35px",
                                    'color': '#00cc00'},
                           ),
                ], className = 'value_indicator'),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('+${0:,.2f}'.format(revenues_difference),
                           style = {
                               'color': '#00cc00',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('+{0:,.1f}%'.format(revenues_pct_change),
                           style = {
                               'color': '#00cc00',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]

    elif revenues_difference < 0:
        return [
            html.P('Revenues',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('${0:,.0f}'.format(revenues),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),

                html.Div([
                    html.I(className = "fas fa-caret-down",
                           style = {"font-size": "35px",
                                    'color': '#EC1E3D'},
                           ),
                ], className = 'value_indicator'),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('-${0:,.2f}'.format(abs(revenues_difference)),
                           style = {
                               'color': '#EC1E3D',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('{0:,.1f}%'.format(revenues_pct_change),
                           style = {
                               'color': '#EC1E3D',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]

    elif revenues_difference == 0:
        return [
            html.P('Revenues',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('${0:,.0f}'.format(revenues),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('0.00',
                           style = {
                               'color': 'white',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('0.0%',
                           style = {
                               'color': 'white',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]


@app.callback(Output('chart1', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        month = data['Months']
        value = data['Revenues']

    return {
        'data': [go.Scatter(
            x = month,
            y = value,
            mode = 'lines',
            line = dict(width = 3, color = '#00b300'),
            hoverinfo = 'skip',
        )],

        'layout': go.Layout(
            height = 50,
            width = 150,
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            margin = dict(t = 0, b = 0, r = 0, l = 0),
            xaxis = dict(showline = False,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),

            yaxis = dict(showline = False,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),
        )

    }

@app.callback(Output('text2', 'children'),
              [Input('select_month', 'value')])
def update_text(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        # Calculate profit
        data['Profit'] = data['Revenues'] - data['Total Cost (Sales & Marketing)']
        # Calculate difference between two months
        data['Profit_Difference'] = data['Profit'].diff()
        # Calculate percentage change difference between two months
        data['Profit_pct_Difference'] = (data['Profit'].pct_change()) * 100
        data['Profit_Difference'] = data['Profit_Difference'].fillna(0)
        filter_month = data[data['Months'] == select_month]
        profit = filter_month['Profit'].iloc[0]
        profit_difference = filter_month['Profit_Difference'].iloc[0]
        profit_pct_change = filter_month['Profit_pct_Difference'].iloc[0]

    if profit_difference > 0:
        return [
            html.P('Profit',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('${0:,.0f}'.format(profit),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),

                html.Div([
                    html.I(className = "fas fa-caret-up",
                           style = {"font-size": "35px",
                                    'color': '#00cc00'},
                           ),
                ], className = 'value_indicator'),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('+${0:,.2f}'.format(profit_difference),
                           style = {
                               'color': '#00cc00',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('+{0:,.1f}%'.format(profit_pct_change),
                           style = {
                               'color': '#00cc00',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]

    elif profit_difference < 0:
        return [
            html.P('Profit',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('${0:,.0f}'.format(profit),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),

                html.Div([
                    html.I(className = "fas fa-caret-down",
                           style = {"font-size": "35px",
                                    'color': '#EC1E3D'},
                           ),
                ], className = 'value_indicator'),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('-${0:,.2f}'.format(abs(profit_difference)),
                           style = {
                               'color': '#EC1E3D',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('{0:,.1f}%'.format(profit_pct_change),
                           style = {
                               'color': '#EC1E3D',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]

    elif profit_difference == 0:
        return [
            html.P('Profit',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('${0:,.0f}'.format(profit),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('0.00',
                           style = {
                               'color': 'white',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('0.0%',
                           style = {
                               'color': 'white',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]


@app.callback(Output('chart2', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        month = data['Months']
        value = data['Profit']

    return {
        'data': [go.Scatter(
            x = month,
            y = value,
            mode = 'lines',
            line = dict(width = 3, color = '#00b300'),
            hoverinfo = 'skip',
        )],

        'layout': go.Layout(
            height = 50,
            width = 150,
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            margin = dict(t = 0, b = 0, r = 0, l = 0),
            xaxis = dict(showline = False,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),

            yaxis = dict(showline = False,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),
        )

    }

@app.callback(Output('text3', 'children'),
              [Input('select_month', 'value')])
def update_text(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        # Calculate difference between two months
        data['Orders_Difference'] = data['Orders Placed'].diff()
        # Calculate percentage change difference between two months
        data['Orders_pct_Difference'] = (data['Orders Placed'].pct_change()) * 100
        data['Orders_Difference'] = data['Orders_Difference'].fillna(0)
        filter_month = data[data['Months'] == select_month]
        orders_placed = filter_month['Orders Placed'].iloc[0]
        orders_difference = filter_month['Orders_Difference'].iloc[0]
        orders_pct_change = filter_month['Orders_pct_Difference'].iloc[0]

    if orders_difference > 0:
        return [
            html.P('Orders Placed',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('{0:,.0f}'.format(orders_placed),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),

                html.Div([
                    html.I(className = "fas fa-caret-up",
                           style = {"font-size": "35px",
                                    'color': '#00cc00'},
                           ),
                ], className = 'value_indicator'),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('+{0:,.2f}'.format(orders_difference),
                           style = {
                               'color': '#00cc00',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('+{0:,.1f}%'.format(orders_pct_change),
                           style = {
                               'color': '#00cc00',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]

    elif orders_difference < 0:
        return [
            html.P('Orders Placed',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('{0:,.0f}'.format(orders_placed),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),

                html.Div([
                    html.I(className = "fas fa-caret-down",
                           style = {"font-size": "35px",
                                    'color': '#EC1E3D'},
                           ),
                ], className = 'value_indicator'),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('-{0:,.2f}'.format(abs(orders_difference)),
                           style = {
                               'color': '#EC1E3D',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('{0:,.1f}%'.format(orders_pct_change),
                           style = {
                               'color': '#EC1E3D',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]

    elif orders_difference == 0:
        return [
            html.P('Orders Placed',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('{0:,.0f}'.format(orders_placed),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('0.00',
                           style = {
                               'color': 'white',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('0.0%',
                           style = {
                               'color': 'white',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]


@app.callback(Output('chart3', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        month = data['Months']
        value = data['Orders Placed']

    return {
        'data': [go.Scatter(
            x = month,
            y = value,
            mode = 'lines',
            line = dict(width = 3, color = '#00b300'),
            hoverinfo = 'skip',
        )],

        'layout': go.Layout(
            height = 50,
            width = 150,
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            margin = dict(t = 0, b = 0, r = 0, l = 0),
            xaxis = dict(showline = False,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),

            yaxis = dict(showline = False,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),
        )

    }

@app.callback(Output('text4', 'children'),
              [Input('select_month', 'value')])
def update_text(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        # Calculate difference between two months
        data['Customers_Difference'] = data['Customers'].diff()
        # Calculate percentage change difference between two months
        data['Customers_pct_Difference'] = (data['Customers'].pct_change()) * 100
        data['Customers_Difference'] = data['Customers_Difference'].fillna(0)
        filter_month = data[data['Months'] == select_month]
        customers = filter_month['Customers'].iloc[0]
        Customers_difference = filter_month['Customers_Difference'].iloc[0]
        Customers_pct_change = filter_month['Customers_pct_Difference'].iloc[0]

    if Customers_difference > 0:
        return [
            html.P('Customers',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('{0:,.0f}'.format(customers),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),

                html.Div([
                    html.I(className = "fas fa-caret-up",
                           style = {"font-size": "35px",
                                    'color': '#00cc00'},
                           ),
                ], className = 'value_indicator'),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('+{0:,.2f}'.format(Customers_difference),
                           style = {
                               'color': '#00cc00',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('+{0:,.1f}%'.format(Customers_pct_change),
                           style = {
                               'color': '#00cc00',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]

    elif Customers_difference < 0:
        return [
            html.P('Customers',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('{0:,.0f}'.format(customers),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),

                html.Div([
                    html.I(className = "fas fa-caret-down",
                           style = {"font-size": "35px",
                                    'color': '#EC1E3D'},
                           ),
                ], className = 'value_indicator'),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('-{0:,.2f}'.format(abs(Customers_difference)),
                           style = {
                               'color': '#EC1E3D',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('{0:,.1f}%'.format(Customers_pct_change),
                           style = {
                               'color': '#EC1E3D',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]

    elif Customers_difference == 0:
        return [
            html.P('Revenues',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('{0:,.0f}'.format(customers),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('0.00',
                           style = {
                               'color': 'white',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('0.0%',
                           style = {
                               'color': 'white',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]


@app.callback(Output('chart4', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        month = data['Months']
        value = data['Customers']

    return {
        'data': [go.Scatter(
            x = month,
            y = value,
            mode = 'lines',
            line = dict(width = 3, color = '#00b300'),
            hoverinfo = 'skip',
        )],

        'layout': go.Layout(
            height = 50,
            width = 150,
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            margin = dict(t = 0, b = 0, r = 0, l = 0),
            xaxis = dict(showline = False,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),

            yaxis = dict(showline = False,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),
        )

    }

@app.callback(Output('text5', 'children'),
              [Input('select_month', 'value')])
def update_text(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        # Calculate difference between two months
        data['Items_Difference'] = data['Purchased Items'].diff()
        # Calculate percentage change difference between two months
        data['Items_pct_Difference'] = (data['Purchased Items'].pct_change()) * 100
        data['Items_Difference'] = data['Items_Difference'].fillna(0)
        filter_month = data[data['Months'] == select_month]
        items = filter_month['Purchased Items'].iloc[0]
        items_difference = filter_month['Items_Difference'].iloc[0]
        items_pct_change = filter_month['Items_pct_Difference'].iloc[0]

    if items_difference > 0:
        return [
            html.P('Purchased Items',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('{0:,.0f}'.format(items),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),

                html.Div([
                    html.I(className = "fas fa-caret-up",
                           style = {"font-size": "35px",
                                    'color': '#00cc00'},
                           ),
                ], className = 'value_indicator'),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('+{0:,.2f}'.format(items_difference),
                           style = {
                               'color': '#00cc00',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('+{0:,.1f}%'.format(items_pct_change),
                           style = {
                               'color': '#00cc00',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]

    elif items_difference < 0:
        return [
            html.P('Purchased Items',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('{0:,.0f}'.format(items),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),

                html.Div([
                    html.I(className = "fas fa-caret-down",
                           style = {"font-size": "35px",
                                    'color': '#EC1E3D'},
                           ),
                ], className = 'value_indicator'),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('-{0:,.2f}'.format(abs(items_difference)),
                           style = {
                               'color': '#EC1E3D',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('{0:,.1f}%'.format(items_pct_change),
                           style = {
                               'color': '#EC1E3D',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]

    elif items_difference == 0:
        return [
            html.P('Purchased Items',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('{0:,.0f}'.format(items),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('0.00',
                           style = {
                               'color': 'white',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('0.0%',
                           style = {
                               'color': 'white',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]


@app.callback(Output('chart5', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        month = data['Months']
        value = data['Purchased Items']

    return {
        'data': [go.Scatter(
            x = month,
            y = value,
            mode = 'lines',
            line = dict(width = 3, color = '#00b300'),
            hoverinfo = 'skip',
        )],

        'layout': go.Layout(
            height = 50,
            width = 150,
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            margin = dict(t = 0, b = 0, r = 0, l = 0),
            xaxis = dict(showline = False,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),

            yaxis = dict(showline = False,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),
        )

    }

@app.callback(Output('text6', 'children'),
              [Input('select_month', 'value')])
def update_text(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        # Calculate sales
        data['Sales'] = data['Orders Placed']
        # Calculate conversion rate
        data['Conversion Rate'] = ((data['Sales']) / (data['Inquiries'])) * 100
        # Calculate difference between two months
        data['Conversion_Difference'] = data['Conversion Rate'].diff()
        # Calculate percentage change difference between two months
        data['Conversion_pct_Difference'] = (data['Conversion Rate'].pct_change()) * 100
        data['Conversion_Difference'] = data['Conversion_Difference'].fillna(0)
        filter_month = data[data['Months'] == select_month]
        conversion = filter_month['Conversion Rate'].iloc[0]
        conversion_difference = filter_month['Conversion_Difference'].iloc[0]
        conversion_pct_change = filter_month['Conversion_pct_Difference'].iloc[0]

    if conversion_difference > 0:
        return [
            html.P('Conversion Rate',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('{0:,.1f}%'.format(conversion),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),

                html.Div([
                    html.I(className = "fas fa-caret-up",
                           style = {"font-size": "35px",
                                    'color': '#00cc00'},
                           ),
                ], className = 'value_indicator'),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('+{0:,.2f}%'.format(conversion_difference),
                           style = {
                               'color': '#00cc00',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('+{0:,.1f}%'.format(conversion_pct_change),
                           style = {
                               'color': '#00cc00',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]

    elif conversion_difference < 0:
        return [
            html.P('Conversion Rate',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('{0:,.1f}%'.format(conversion),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),

                html.Div([
                    html.I(className = "fas fa-caret-down",
                           style = {"font-size": "35px",
                                    'color': '#EC1E3D'},
                           ),
                ], className = 'value_indicator'),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('{0:,.2f}%'.format(conversion_difference),
                           style = {
                               'color': '#EC1E3D',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('{0:,.1f}%'.format(conversion_pct_change),
                           style = {
                               'color': '#EC1E3D',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]

    elif conversion_difference == 0:
        return [
            html.P('Conversion Rate',
                   style = {
                       'color': 'white',
                       'fontSize': 17,
                       'font-weight': 'bold'
                   },
                   className = 'card_title'
                   ),

            html.Div([
                html.P('{0:,.1f}%'.format(conversion),
                       style = {
                           'color': 'white',
                           'fontSize': 25,
                           'font-weight': 'bold'
                       }, className = 'monthly_value'
                       ),
            ], className = 'value_and_indicator'),

            html.Div([
                html.Div([
                    html.P('0.00%',
                           style = {
                               'color': 'white',
                               'fontSize': 14,
                           }, className = 'monthly_difference_value'
                           ),

                    html.P('0.0%',
                           style = {
                               'color': 'white',
                               'fontSize': 14,
                           }, className = 'monthly_pct_change'
                           ),
                ], className = 'difference_value_row'),

                html.P('vs previous month',
                       style = {
                           'color': 'white',
                           'fontSize': 13,
                           'font-weight': 'bold'
                       },
                       className = 'text_previous_month'
                       ),
            ], className = 'difference_value_column')
        ]


@app.callback(Output('chart6', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        month = data['Months']
        value = data['Conversion Rate']

    return {
        'data': [go.Scatter(
            x = month,
            y = value,
            mode = 'lines',
            line = dict(width = 3, color = '#00b300'),
            hoverinfo = 'skip',
        )],

        'layout': go.Layout(
            height = 50,
            width = 150,
            plot_bgcolor = 'rgba(0, 0, 0, 0)',
            paper_bgcolor = 'rgba(0, 0, 0, 0)',
            margin = dict(t = 0, b = 0, r = 0, l = 0),
            xaxis = dict(showline = False,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),

            yaxis = dict(showline = False,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')

                         ),
        )

    }


@app.callback(Output('donut_chart1', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        # Calculate % profit
        data['% Profit'] = (data['Profit'] / data['Revenues']) * 100
        filter_month = data[data['Months'] == select_month]
        percentage_profit = filter_month['% Profit'].iloc[0]
        remaining_percentage_profit = 100 - (filter_month['% Profit'].iloc[0])
        colors = ['#DEB340', '#335476']

    return {
        'data': [go.Pie(labels = ['', ''],
                        values = [percentage_profit, remaining_percentage_profit],
                        marker = dict(colors = colors,
                                      line=dict(color='#DEB340', width=2)),
                        hoverinfo = 'skip',
                        textinfo = 'text',
                        hole = .7,
                        rotation = 90
                        )],

        'layout': go.Layout(
            plot_bgcolor = 'rgba(0,0,0,0)',
            paper_bgcolor = 'rgba(0,0,0,0)',
            margin = dict(t = 35, b = 10, r = 0, l = 0),
            showlegend = False,
            title={'text': '% Sales Profit',
                   'y': 0.95,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            titlefont = {'color': 'white',
                         'size': 15},
        ),

    }


@app.callback(Output('donut_chart_text1', 'children'),
              [Input('select_month', 'value')])
def update_text(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        filter_month = data[data['Months'] == select_month]
        percentage_profit = filter_month['% Profit'].iloc[0]

    return [
        html.P('{0:,.0f}%'.format(percentage_profit),
               style = {
                   'color': '#DEB340',
                   'fontSize': 25,
                   'font-weight': 'bold'
               }),
    ]

@app.callback(Output('donut_chart2', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        # Calculate % target
        data['% Target'] = (data['Revenues'] / data['Target']) * 100
        filter_month = data[data['Months'] == select_month]
        percentage_target = filter_month['% Target'].iloc[0]
        percentage_target1 = float(100.00)
        remaining_percentage_target = 100 - (filter_month['% Target'].iloc[0])
        colors = ['#DEB340', '#335476']

    if percentage_target > 100:
        return {
            'data': [go.Pie(labels=['', ''],
                            values=[percentage_target1],
                            marker=dict(colors=colors,
                                        line=dict(color='#DEB340', width=2)),
                            hoverinfo='skip',
                            textinfo='text',
                            hole=.7,
                            rotation=0
                            )],

            'layout': go.Layout(
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                margin=dict(t=35, b=10, r=0, l=0),
                showlegend=False,
                title={'text': 'Monthly Goal',
                       'y': 0.95,
                       'x': 0.5,
                       'xanchor': 'center',
                       'yanchor': 'top'},
                titlefont={'color': 'white',
                           'size': 15},
            ),

        }
    else:
        return {
        'data': [go.Pie(labels = ['', ''],
                        values = [percentage_target, remaining_percentage_target],
                        marker = dict(colors = colors,
                                      line=dict(color='#DEB340', width=2)),
                        hoverinfo = 'skip',
                        textinfo = 'text',
                        hole = .7,
                        rotation = 0
                        )],

        'layout': go.Layout(
            plot_bgcolor = 'rgba(0,0,0,0)',
            paper_bgcolor = 'rgba(0,0,0,0)',
            margin = dict(t = 35, b = 10, r = 0, l = 0),
            showlegend = False,
            title={'text': 'Monthly Goal',
                   'y': 0.95,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            titlefont = {'color': 'white',
                         'size': 15},
        ),

    }


@app.callback(Output('donut_chart_text2', 'children'),
              [Input('select_month', 'value')])
def update_text(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        filter_month = data[data['Months'] == select_month]
        percentage_target = filter_month['% Target'].iloc[0]

    return [
        html.P('{0:,.0f}%'.format(percentage_target),
               style = {
                   'color': '#DEB340',
                   'fontSize': 25,
                   'font-weight': 'bold'
               }),
    ]


@app.callback(Output('donut_chart3', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    total_revenues = data['Revenues'].sum()
    total_target = data['Target'].sum()
    ytd_goal = (total_revenues / total_target) * 100
    colors = ['#DEB340']

    return {
        'data': [go.Pie(labels = [''],
                        values = [ytd_goal],
                        marker = dict(colors = colors,
                                      line=dict(color='#DEB340', width=2)),
                        hoverinfo = 'skip',
                        textinfo = 'text',
                        hole = .7,
                        rotation = 90
                        )],

        'layout': go.Layout(
            plot_bgcolor = 'rgba(0,0,0,0)',
            paper_bgcolor = 'rgba(0,0,0,0)',
            margin = dict(t = 35, b = 10, r = 0, l = 0),
            showlegend = False,
            title={'text': 'YTD Goal',
                   'y': 0.95,
                   'x': 0.5,
                   'xanchor': 'center',
                   'yanchor': 'top'},
            titlefont = {'color': 'white',
                         'size': 15},
        ),

    }


@app.callback(Output('donut_chart_text3', 'children'),
              [Input('select_month', 'value')])
def update_text(select_month):
    total_revenues = data['Revenues'].sum()
    total_target = data['Target'].sum()
    ytd_goal = (total_revenues / total_target) * 100

    return [
        html.P('{0:,.0f}%'.format(ytd_goal),
               style = {
                   'color': '#DEB340',
                   'fontSize': 25,
                   'font-weight': 'bold'
               }),
    ]


@app.callback(Output('funnel_chart', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        filter_month = data[data['Months'] == select_month]
        inquiries = filter_month['Inquiries'].iloc[0]
        lead = filter_month['Lead'].iloc[0]
        opportunity = filter_month['Opportunity'].iloc[0]
        sales = filter_month['Sales'].iloc[0]
        object_data = [['Inquiries', inquiries], ['Lead', lead], ['Opportunity', opportunity], ['Sales', sales]]
        df = pd.DataFrame(object_data, columns = ['Text', 'Value'])
        df1 = df.sort_values(by = ['Value'], ascending = False)

    return {
        'data':[
            go.Funnel(
                x = df1['Value'],
                y = df1['Text'],
                textposition = "inside",
                textinfo = "value",
                textfont = dict(
                    family = "Arial Black",
                    size = 14,
                    color = "#A23C33"
                ),
                marker = {"color": '#DEB340'},
                hoverinfo = 'skip',
            )],


        'layout': go.Layout(
             plot_bgcolor='rgba(0,0,0,0)',
             paper_bgcolor='rgba(0,0,0,0)',
             margin = dict(r = 0, t = 30, b = 30),
             title = {'text': 'Sales Funnel',
                      'y': 0.97,
                      'x': 0.5,
                      'xanchor': 'center',
                      'yanchor': 'top'},
             titlefont = {'color': 'white',
                          'size': 15},

             yaxis = dict(title = '<b></b>',
                          visible = True,
                          color = 'white',
                          showline = True,
                          showgrid = False,
                          showticklabels = True,
                          linecolor = 'white',
                          linewidth = 1,
                          ticks = 'outside',
                          tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')
                          ),
        )

    }


@app.callback(Output('bar_chart', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        filter_month = data[data['Months'] == select_month]
        target = filter_month['Target'].iloc[0]
        revenues = filter_month['Revenues'].iloc[0]
        object_data = [['Target', target], ['Revenues', revenues]]
        df2 = pd.DataFrame(object_data, columns = ['Text', 'Value'])

    return {
        'data': [go.Bar(x = df2['Value'],
                        y = df2['Text'],
                        text = df2['Value'],
                        texttemplate = '$' + '%{text:,.0f}',
                        textposition = 'inside',
                        marker = dict(color='#DEB340'),
                        width = 0.5,
                        textfont = dict(
                            family = "Arial Black",
                            size = 14,
                            color = "#A23C33"
                        ),
                        orientation = 'h',
                        hoverinfo = 'skip'
                        )],

        'layout': go.Layout(
            plot_bgcolor = 'rgba(0,0,0,0)',
            paper_bgcolor = 'rgba(0,0,0,0)',
            title = {'text': 'Revenue vs Target',
                     'y': 0.97,
                     'x': 0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
            titlefont = {'color': 'white',
                         'size': 15},
            margin = dict(r = 20, t = 50, b = 50),
            xaxis = dict(title = '<b></b>',
                         tickprefix = '$',
                         tickformat = ',.0f',
                         visible = True,
                         color = 'white',
                         showline = False,
                         showgrid = True,
                         showticklabels = True,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = '',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')
                         ),

            yaxis = dict(title = '<b></b>',
                         visible = True,
                         color = 'white',
                         showline = True,
                         showgrid = False,
                         showticklabels = True,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')
                         ),

                )
    }


@app.callback(Output('stack_bar_chart', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    sales_target = data['Target']
    above_the_target = data['Revenues']
    data['Below the Target'] = np.where(data['Revenues'] < data['Target'], data['Revenues'], 0)
    months = data['Months']

    return {
        'data': [go.Bar(x = months,
                        y = above_the_target,
                        name = 'Above the Target',
                        marker = dict(color='#00B0F0'),
                        width = 0.5,
                        orientation = 'v',
                        hoverinfo = 'skip'
                        ),
                 go.Bar(x = months,
                        y = data['Below the Target'],
                        name = 'Below the Target',
                        marker = dict(color = '#EBD18C'),
                        width = 0.5,
                        orientation = 'v',
                        hoverinfo = 'skip'
                        ),
                 go.Scatter(x = months,
                            y = sales_target,
                            name = 'Sales Target',
                            mode = 'markers',
                            marker = dict(color = '#7030A0', size = 25, symbol = 'line-ew',
                                          line = dict(color = '#E6314C', width = 5)),
                            hoverinfo = 'skip'
                            )],

        'layout': go.Layout(
            barmode = 'overlay',
            plot_bgcolor = 'rgba(0,0,0,0)',
            paper_bgcolor = 'rgba(0,0,0,0)',
            title = {'text': 'Sales vs Goal',
                     'y': 0.97,
                     'x': 0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
            titlefont = {'color': 'white',
                         'size': 15},
            margin = dict(r = 20, t = 30, b = 10),
            xaxis = dict(title = '<b></b>',
                         visible = True,
                         color = 'white',
                         showline = True,
                         showgrid = False,
                         showticklabels = True,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')
                         ),

            yaxis = dict(title = '<b></b>',
                         tickprefix = '$',
                         tickformat = ',.0f',
                         visible = True,
                         color = 'white',
                         showline = True,
                         showgrid = False,
                         showticklabels = True,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')
                         ),
            legend = {
                'orientation': 'h',
                'bgcolor': '#335476',
                'xanchor': 'center', 'x': 0.5, 'y': -0.2},
            font = dict(
                family = "sans-serif",
                size = 12,
                color = 'white'),
        )
    }


@app.callback(Output('percent_bar_chart', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    monthly_sales_growth = data['pct_Difference']
    months = data['Months']
    data['Color'] = np.where(data['pct_Difference'] > 0, '#DEB340', '#A23C33')


    return {
        'data': [go.Bar(x = months,
                        y = monthly_sales_growth,
                        text = monthly_sales_growth,
                        texttemplate = '%{text:.1f}%',
                        textposition = "outside",
                        textfont = dict(
                            family = "sans-serif",
                            size = 14,
                            color = "white"
                        ),
                        marker = dict(color=data['Color']),
                        width = 0.9,
                        orientation = 'v',
                        hoverinfo = 'skip'
                        )],

        'layout': go.Layout(
            plot_bgcolor = 'rgba(0,0,0,0)',
            paper_bgcolor = 'rgba(0,0,0,0)',
            title = {'text': 'Monthly Sales Growth',
                     'y': 0.97,
                     'x': 0.5,
                     'xanchor': 'center',
                     'yanchor': 'top'},
            titlefont = {'color': 'white',
                         'size': 15},
            margin = dict(l = 20, r = 20, t = 20, b = 20),
            xaxis = dict(title = '<b></b>',
                         visible = True,
                         color = 'white',
                         showline = True,
                         showgrid = False,
                         showticklabels = True,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = '',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')
                         ),

            yaxis = dict(title = '<b></b>',
                         visible = True,
                         color = 'white',
                         showline = False,
                         showgrid = False,
                         showticklabels = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = '',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')
                         ),
        )
    }


@app.callback(Output('chart_text1', 'children'),
              [Input('select_month', 'value')])
def update_text(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        data['AVG Sales / Customer'] = data['Revenues'] / data['Customers']
        filter_month = data[data['Months'] == select_month]
        average_sales_per_customer = filter_month['AVG Sales / Customer'].iloc[0]

    return [
        html.Div([
            html.P('AVG Sales / Customer',
                   style = {
                       'color': 'white',
                       'fontSize': 15,
                       'font-weight': 'bold'
                   }, className = 'average_sales_text'),
            html.P('${0:,.0f}'.format(average_sales_per_customer),
                   style = {
                       'color': 'white',
                       'fontSize': 25,
                       'font-weight': 'bold'
                   }, className = 'average_sales_value')
        ], className = 'average_sales_column'),
    ]


@app.callback(Output('average_sales_bar_chart1', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    average_sales = data['AVG Sales / Customer']
    months = data['Months']

    return {
        'data': [go.Scatter(x = months,
                            y = average_sales,
                            mode = 'lines',
                            line = dict(shape = "spline", smoothing = 1.3, width = 3, color = '#00B0F0'),
                            hoverinfo = 'skip'
                            )],

        'layout': go.Layout(
            plot_bgcolor = 'rgba(0,0,0,0)',
            paper_bgcolor = 'rgba(0,0,0,0)',
            xaxis = dict(title = '<b></b>',
                         visible = True,
                         color = 'white',
                         showline = True,
                         showgrid = False,
                         showticklabels = True,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')
                         ),

            yaxis = dict(title = '<b></b>',
                         visible = True,
                         color = 'white',
                         showline = False,
                         showgrid = False,
                         showticklabels = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = '',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')
                         ),
        )
    }

@app.callback(Output('chart_text2', 'children'),
              [Input('select_month', 'value')])
def update_text(select_month):
    if select_month is None:
        raise PreventUpdate
    else:
        data['AVG Ticket Sales'] = data['Revenues'] / data['Orders Placed']
        filter_month = data[data['Months'] == select_month]
        average_ticket_sales = filter_month['AVG Ticket Sales'].iloc[0]

    return [
        html.Div([
            html.P('AVG Ticket Sales',
                   style = {
                       'color': 'white',
                       'fontSize': 15,
                       'font-weight': 'bold'
                   }, className = 'average_sales_text'),
            html.P('${0:,.0f}'.format(average_ticket_sales),
                   style = {
                       'color': 'white',
                       'fontSize': 25,
                       'font-weight': 'bold'
                   }, className = 'average_sales_value')
        ], className = 'average_sales_column'),
    ]


@app.callback(Output('average_sales_bar_chart2', 'figure'),
              [Input('select_month', 'value')])
def update_graph(select_month):
    average_sales = data['AVG Ticket Sales']
    months = data['Months']

    return {
        'data': [go.Scatter(x = months,
                            y = average_sales,
                            mode = 'lines',
                            line = dict(shape = "spline", smoothing = 1.3, width = 3, color = '#00B0F0'),
                            hoverinfo = 'skip'
                            )],

        'layout': go.Layout(
            plot_bgcolor = 'rgba(0,0,0,0)',
            paper_bgcolor = 'rgba(0,0,0,0)',
            xaxis = dict(title = '<b></b>',
                         visible = True,
                         color = 'white',
                         showline = True,
                         showgrid = False,
                         showticklabels = True,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')
                         ),

            yaxis = dict(title = '<b></b>',
                         visible = True,
                         color = 'white',
                         showline = False,
                         showgrid = False,
                         showticklabels = False,
                         linecolor = 'white',
                         linewidth = 1,
                         ticks = '',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white')
                         ),
        )
    }


if __name__ == "__main__":
    app.run_server(debug = True, port = 9021)
