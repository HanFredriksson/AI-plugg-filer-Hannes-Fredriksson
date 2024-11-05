def plot_missing_values(data):
    import plotly_express as px
    import pandas as pd

    data_null = pd.DataFrame({"NaN count": data.isna().sum()})
    data_null = data_null[data_null["NaN count"] != 0].sort_values(by= "NaN count", ascending=False)
    fig = px.bar(data_null, x = data_null.index, y = "NaN count", labels = {"index": "Columns"})

    return fig.show()


def whitespace_remover(dataframe):

    # iterating over the columns
    for i in dataframe.columns:

        # checking datatype of each columns
        if dataframe[i].dtype == 'object':

            # applying replace function on column and removes all whitespaces
            dataframe[i] = dataframe[i].str.replace(" ", "")
        
        else:

            # if condn. is False then it will do nothing.
            pass
