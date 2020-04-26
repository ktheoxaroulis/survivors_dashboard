import sys
sys.path.insert(0, '../')

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

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
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Test"],
                                        className="subtitle padded",
                                    ),
                                ],
                                className=" twelve columns",
                            )
                        ],
                        className="row ",
                    ),

                ],
                className="sub-page", id="sub-page"
            ),
        ],
        className="page",
    )
