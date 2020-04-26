import sys
sys.path.insert(0, '../')

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc


from utils import Header, make_dash_table
import pandas as pd
import pathlib


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 3
            html.Div(
                [

                    # Row 3
                    html.Br([]),
                    dbc.Container(
                        [
                            dbc.Row([
                                dbc.Col([dbc.Jumbotron([html.H6(children="Select", className="display-5")])], md=4, align="center"),
                                dbc.Col([dbc.Card( [dbc.CardHeader(html.H6("Test right"))])], md=8),])

                        ],
                        className="row ",
                    ),
                ],
                className="sub-page", id="sub-page"
            ),
        ],
        className="page",
    )
