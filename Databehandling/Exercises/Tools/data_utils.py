def plot_missing_values(data):
    import plotly_express as px
    import pandas as pd

    data_null = pd.DataFrame({"NaN count": data.isna().sum()})
    data_null = data_null[data_null["NaN count"] != 0].sort_values(by= "NaN count", ascending=False)
    fig = px.bar(data_null, x = data_null.index, y = "NaN count", labels = {"index": "Columns"})

    return fig.show()


def convert_object_to_numbers(dataframe, decimal_point=True):
    
    import pandas as pd
   
    skipped_col = []

    for i in dataframe.columns:

        # checking datatype of each columns
        if dataframe[i].dtype == 'object':
            
            # if there is a . sepreating the digits in 100s
            if decimal_point == False:
                dataframe[i] = dataframe[i].str.replace(".", "", regex=False)

            # removes all whitespaces, commas to punctuation and convert to numeric
            dataframe[i] = dataframe[i].str.replace(r"\s+", "", regex=True)
            dataframe[i] = dataframe[i].str.replace(",", ".")
            
            try:
                dataframe[i] = pd.to_numeric(dataframe[i])
            except ValueError:
                skipped_col.append(i)
                continue

    # gives you the namne of the skipped column
    if skipped_col:
            return f"Columns \"{', '.join(skipped_col)}\" were skipped"
    else:
    # if condn. is False then it will do nothing.
        return
    
def remove_footnote_symbals (dataframe):
    dataframe[i] = dataframe[i].str.replace(r"\[\d+\]", "", regex=True)

    return dataframe