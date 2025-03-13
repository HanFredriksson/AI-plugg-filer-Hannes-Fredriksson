import pickle
import numpy as np
from dash import Dash, html, Input, Output, callback
from dash.exceptions import PreventUpdate
from dash_canvas import DashCanvas
from dash_canvas.utils import (array_to_data_url, parse_jsonstring,
                               watershed_segmentation)
from skimage import io, color, img_as_ubyte


with open(model_pkl_file, 'rb') as file:  
    model = pickle.load(file)


def KNN_model(user_digit):

    y_predict = model.predict(user_digit)

    return y_predict


app = Dash()

filename = 'https://raw.githubusercontent.com/plotly/datasets/master/mitochondria.jpg'

canvas_width = 300

app.layout = html.Div([
    html.H6('Draw on image and press Save to show annotations geometry'),
    html.Div([
        DashCanvas(
            id='canvas',
            lineWidth=5,
            filename=filename,
            width=canvas_width,
        ),
    ], className="five columns"),
    html.Div(html.Img(id='my-iimage', width=300), className="five columns"),
    ])


@callback(Output('my-iimage', 'src'),
              Input('canvas', 'json_data'))

def update_data(string):
    if string:
        mask = parse_jsonstring(string, io.imread(filename, as_gray=True).shape)
    
    else:
        raise PreventUpdate
    
    return array_to_data_url((255 * mask).astype(np.uint8))


if __name__ == '__main__':
    app.run(debug=True)
