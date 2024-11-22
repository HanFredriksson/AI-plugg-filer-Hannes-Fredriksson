from FetchOSData import OsDataFetcher
import dash
import pandas as pd
import plotly.express as px 
from dash import Dash, dcc, html, dash_table
import pandas as pd
# The variabels we need
os_data = OsDataFetcher("../Projekt-OS/Data/athlete_events.csv", "Name")
sports = ["Swimming", "Alpine Skiing", "Rowing", "Cross Country Skiing"]
sex = {"Female": "F", "Male": "M"}
medals = ["Gold", "Silver", "Bronze"]

app = dash.Dash(__name__)
# Dicts with key for what we want to filter for showing in the graphs.
# Keys get picked from a meny in dashboard
# Do we need to move the filter function from the class?
# Or filter funktion of the class is a general filter making smaller dataframes, like one for each sport
# 

app.layout = [
    html.Div(children='My First App with Data'),
    dash_table.DataTable(data=os_data.data.to_dict('records'), page_size=10)
        dcc.Graph(figure={}, id='controls-and-graph')
]


@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')

def show_graf(data, cat, graf):
    """
    param data: data frame to plot
    peram cat: the span of the data
    peram graf: type of graf "bar", "line", "histo"
    """
    
    if graf == "bar":
        fig = px.bar(data, x=data.index, y= cat, barmode= "stack")
    if graf == "line":
        fig = px.line(data, x=data.index, y= cat)
    if graf == "histo":
        fig = px.histogram(data, x=data.index, y= cat, nbins = 14)
    return fig


def calc_averge():
    # Calculate on averag how many medals in each denomination each genader has gotten
    pass


def medal_counter(pick, filter, count_in):
    """Counts the medals from picked country or sport from
    a grouped column. 
    Retruns a data frame with total and each variation of medal 
    with count_in as index

    param pick: are sport or country
    param filter: Wich sport or country
    param count_in: For wich columne to count medals

    """
    dff = os_data.os_filtered_dataframe(pick, filter)

    gold_medal = dff[dff["Medal"] == "Gold"].groupby(count_in).size()
    silver_medal = dff[dff["Medal"] == "Silver"].groupby(count_in).size()
    bronze_medal = dff[dff["Medal"] == "Bronze"].groupby(count_in).size()

    medal_count = pd.DataFrame({"Gold medals": gold_medal,
                                "Silver medals": silver_medal,
                                "Bronze Medals": bronze_medal,
                                "Total": gold_medal + silver_medal + bronze_medal
                                }).fillna(0).astype(int)

    return medal_count




if __name__ == '__main__':
    app.run_server(debug=True)
