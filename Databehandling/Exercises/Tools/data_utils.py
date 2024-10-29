def plot_missing_values(data):
    import plotly_express as px
    import pandas as pd

    data_null = pd.DataFrame({"NaN count": data.isna().sum()})
    data_null = data_null[data_null["NaN count"] != 0].sort_values(by= "NaN count", ascending=False)
    fig = px.bar(data_null, x = data_null.index, y = "NaN count", labels = {"index": "Columns"})

    return fig.show()
        