# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from pages import (
    overview,
    doctors,
    government,
    reseachers,
    newsReviews,
)


app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
app.title = 'Survivors'
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
server = app.server


# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


# Callback updating backgrounds
@app.callback(
    [
    Output("sub-page", "className"),
    ],
    [Input("toggleTheme", "value")],
)
def update_background(turn_dark):

    if turn_dark:
        return ["dark-sub-page"]
    else:
        return ["light-sub-page"]


# Update page
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/report/doctors":
        return doctors.create_layout(app)
    elif pathname == "/report/government":
        return government.create_layout(app)
    elif pathname == "/report/reseachers":
        return reseachers.create_layout(app)
    elif pathname == "/report/news-and-reviews":
        return newsReviews.create_layout(app)
    else:
        return overview.create_layout(app)


if __name__ == "__main__":
    app.run_server(debug=False)
