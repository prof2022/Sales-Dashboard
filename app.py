import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd



airport = pd.read_csv('df1.csv')
airport = airport[airport.region_txt=='Sub-Saharan Africa']
airport.reset_index(inplace = True, drop = True)
airport.drop(columns = 'region_txt',inplace = True)
#airport.dropna(inplace=True)

airport1 = airport[['provstate', 'latitude', 'longitude']]

list_locations = airport1.set_index('provstate')[['latitude', 'longitude']].T.to_dict('dict')


app = dash.Dash(__name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}])


app.layout = html.Div([
        html.Div([
            html.Div([
                html.H2("Subsaharan Africa Data", style = {'text-align': 'center'}),
                html.P('Select Country'),
                html.Div([
                   dcc.Dropdown(
                                id = 'select_country',
                                multi = False,
                                clearable = True,
                                disabled = False,
                                style = {'display': True},
                                value = 'Zaire',
                                placeholder = 'Select country',
                                options = [{'label': c, 'value': c}
                                           for c in (airport['country_txt'].unique())]),

                ], className='fix_dropdown'),
                
            html.P('Select State'),
            dcc.Dropdown(id = 'select_state',
                         multi = False,
                         clearable = True,
                         disabled = False,
                         style = {'display': True},
                         placeholder = 'Select state',
                         options = [], className = 'fix_dropdown'),

    ], className="three columns left_pane"),

            html.Div([
                    dcc.Graph(id='map_chart'),
                    dcc.Graph(id='bar_chart'),

                ], className="nine columns fix_charts charts_bg"),

            ], className="row"),

 ])
@app.callback(
    Output('select_state', 'options'),
    Input('select_country', 'value'))
def get_state_options(select_country):
    terr3 = airport[airport['country_txt'] == select_country]
    return [{'label': i, 'value': i} for i in terr3['provstate'].unique()]


@app.callback(
    Output('select_state', 'value'),
    Input('select_state', 'options'))
def get_state_value(select_state):
    return [k['value'] for k in select_state][1]

@app.callback(Output('map_chart', 'figure'),
              [Input('select_state', 'value')])
        
def update_graph(select_state):
    airport4 = airport.groupby(['provstate','latitude', 'longitude'])['nkill'].sum().reset_index()
    airport5 = airport4[airport4['provstate'] == select_state]


    return {
        'data': [go.Scattermapbox(
            lon = airport5['longitude'],
            lat = airport5['latitude'],
            mode = 'markers',
            marker=go.scattermapbox.Marker(
                size = 12,
                color = airport5['nkill'],
                colorscale = 'HSV',
                showscale = False,
                sizemode = 'area'),

            hoverinfo = 'text',
            hovertext =
            '<b>State</b>: ' + airport5['provstate'].astype(str) + '<br>' +
            '<b>Lat</b>: ' + [f'{x:.4f}' for x in airport5['latitude']] + '<br>' +
            '<b>Long</b>: ' + [f'{x:.4f}' for x in airport5['longitude']] + '<br>' +

            '<b>Deaths</b>: ' + [f'{x:,.0f}' for x in airport5['nkill']] + '<br>'

        )],

        'layout': go.Layout(
             margin={"r": 0, "t": 0, "l": 0, "b": 0},
             hovermode='closest',
             mapbox=dict(
                accesstoken='pk.eyJ1IjoicXM2MjcyNTI3IiwiYSI6ImNraGRuYTF1azAxZmIycWs0cDB1NmY1ZjYifQ.I1VJ3KjeM-S613FLv3mtkw',  # Create free account on Mapbox site and paste here access token
                center=dict(lat=list_locations[select_state]['latitude'], lon=list_locations[select_state]['longitude']),
                style='open-street-map',
                # style='dark',
                zoom=5,
                bearing = 0
             ),
             autosize=True,

        )

    }



@app.callback(Output('bar_chart', 'figure'),
              [Input('select_state', 'value')])
def update_graph(select_state):
    airport2 = airport.groupby(['country_txt', 'gname','provstate','latitude','longitude'])['nkill'].sum().reset_index()
    airport3 = airport2[airport2['provstate'] == select_state]


    return {
        'data': [go.Bar(
            x = airport3['gname'],
            y = airport3['nkill'],
            text = airport3['nkill'],
            texttemplate = '%{text:,.0f}',
            textposition = 'auto',


            marker = dict(color=airport3['nkill'],
                          colorscale = 'phase',
                          showscale = False
                          ),

            hoverinfo = 'text',
            hovertext =
            '<b>Country</b>: ' + airport3['country_txt'].astype(str) + '<br>' +
            '<b>State</b>: ' + airport3['provstate'].astype(str) + '<br>' +
            '<b>Group</b>: ' + airport3['gname'].astype(str) + '<br>'+
            '<b>Deaths</b>: ' + [f'{x:,.0f}' for x in airport3['nkill']] + '<br>'
            

        )],

        'layout': go.Layout(
            plot_bgcolor = '#343332',
            paper_bgcolor = '#343332',
            title = {
                'text': 'Total Deaths in' + ' ' + (select_state) + ' ' + 'State',

                'y': 0.95,
                'x': 0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            titlefont = {
                'color': 'white',
                'size': 15},

            hovermode = 'x',
            margin = dict(b=140),



            xaxis = dict(title = '<b></b>',
                         color = 'white',
                         showline = True,
                         showgrid = False,
                         linecolor = 'white',
                         linewidth = 1,
                         showticklabels = True,
                         ticks = 'outside',
                         tickfont = dict(
                             family = 'Arial',
                             size = 12,
                             color = 'white'
                         )

                         ),

            yaxis = dict(title = '<b></b>',


                         color = 'white',
                         showline = False,
                         showgrid = False,
                         showticklabels = False,
                         linecolor = 'white',

                         ),

            legend = {
                'orientation': 'h',
                'bgcolor': '#F2F2F2',
                'x': 0.5,
                'y': 1.25,
                'xanchor': 'center',
                'yanchor': 'top'},

            font = dict(
                family = "sans-serif",
                size = 15,
                color = 'white'),

        )

            }

if __name__ == "__main__":
    app.run_server(debug=True)
