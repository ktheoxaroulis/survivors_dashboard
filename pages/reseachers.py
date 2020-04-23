import sys
sys.path.insert(0, '../')
import os
import dash_html_components as html
from utils import Header, make_dash_table
from urllib.parse import quote as urlquote
from db import DATA_PATH

def create_layout(app):
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(["File List"], className="subtitle padded"),
                                    html.Ul([html.P(file_download_link(filename)) for filename in download_files()]),
                                ],
                                className="row",
                            ),
                        ],
                        className="row",
                    ),
                ],
                className="sub-page", id="sub-page"
            ),
        ],
        className="page"
    )



def download_files():
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(DATA_PATH):
        path = os.path.join(DATA_PATH, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files

def file_download_link(filename):
    location = "/data/{}".format(urlquote(filename))
    return html.A(filename, href=location)