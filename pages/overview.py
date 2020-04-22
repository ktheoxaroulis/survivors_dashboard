import sys
sys.path.insert(0, '../')

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import db
from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_user = pd.read_csv(DATA_PATH.joinpath("user.csv"))
df_fund_facts = pd.read_csv(DATA_PATH.joinpath("df_fund_facts.csv"))
df_price_perf = pd.read_csv(DATA_PATH.joinpath("df_price_perf.csv"))
df_user1 = df_user.loc[:,['userId','birthYear']]
df_user1 <- df_user1.head(n=6)
# def load_ep_data():
#     ep_data = db.get_ep_data()
#     return ep_data
# def load_ac_data():
#     ac_data = db.get_ac_data()
#     return ac_data
# def load_symp_data():
#      symp_data = db.get_symp_survey_data()
#      return symp_data


def create_layout(app):
    # Page layouts
    return html.Div(
        [
            html.Div([Header(app)]),
            # page 1
            html.Div(
                [
                    # Row 3
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H5("Product Summary"),
                                    html.Br([]),
                                    html.P(
                                    "\
                                    As we can see from the current facts, recovery from Covid-19 depends on several factors ( supportive care , patient’s response e.t.c ) and of course investigational treatments are currently increasing.\
									\
									Those who do or will recover probably will develop antibodies. It is not known yet if people who recover are immune for life or if they can  later become infected with a different species of Covid virus. Some recovered patients may have long-term complications.\
									\
                                    The idea was to create a simple app where those who were recovered will fill periodically a survey, tracking down several possible health issues \
									Here you ll find the on-going results and the analysis of these data",
                                        style={"color": "#ffffff"},
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    # Row 4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        ["Symptom Facts"], className="subtitle padded"
                                    ),
                                    html.Table(make_dash_table(df_fund_facts)),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    # Row 5
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6(
                                        "Price & Performance (%)",
                                        className="subtitle padded",
                                    ),
                                    html.Table(make_dash_table(df_price_perf)),
                                ],
                                className="six columns",
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        "Risk Potential", className="subtitle padded"
                                    ),
                                    html.Img(
                                        src=app.get_asset_url("risk_reward.png"),
                                        className="risk-reward",
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row ",
                    ),
                ],
                className="sub-page", id="sub-page"
             ),
        ],
        className="page",
    )
