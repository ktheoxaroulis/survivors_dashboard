import sys
sys.path.insert(0, '../')

import dash_core_components as dcc
import dash_html_components as html
from utils import Header, make_dash_table
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

symptom_cluster_list=["Head", "Breath" , "Heart", "Gastro", "Well Being" , "Pain"]
symptom_cluster_level=["Mid" , "Sever", "Extreme"]

def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 2
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div([
                            html.H6("Select Symptom-Cluster of Recovered", className="subtitle padded"),
                            dcc.Dropdown(id="symptom-cluster-select", options=[{"label": i, "value": i} for i in symptom_cluster_list], value=symptom_cluster_list[0]),
                            html.H6("Select min Level of Symptom of Recovered", className="subtitle padded"),
                            dcc.Dropdown(id="symptom-cluster-level", options=[{"label": i, "value": i} for i in symptom_cluster_level],value=symptom_cluster_level[1]),
                            dcc.Graph(id='symp-barplot'), ],className="five columns",),

                            html.Div([
                            html.H6(["Surveys' Question of Recovered Patients"], className="subtitle padded",),
                            dcc.RadioItems(id="survey-list-select", options=[{'label': 'Likert Diagram', 'value': 'Lik'},],value='Lik'),
                            dcc.Graph(id='survey-barplot'),
                            ], className="seven columns",),
                        ], className="row"),

                ],
                className="sub-page", id="sub-page"
            ),
        ],
        className="page",
    )
