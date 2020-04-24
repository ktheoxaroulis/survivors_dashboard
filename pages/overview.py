import sys
sys.path.insert(0, '../')

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from datetime import date


import db
from utils import Header, make_dash_table
import pandas as pd
import pathlib

# get relative data folder
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()

df_user = pd.read_csv(DATA_PATH.joinpath("user.csv"))
df_baseline = pd.read_csv(DATA_PATH.joinpath("baseline.csv"))

# df_user1 = df_user.loc[:,['userId','birthYear']]
# df_user1 = df_user1.head(n=6)
# def load_ep_data():
#     ep_data = db.get_ep_data()
#     return ep_data
# def load_ac_data():
#     ac_data = db.get_ac_data()
#     return ac_data
# def load_symp_data():
#      symp_data = db.get_symp_survey_data()
#      return symp_data

######### code for gender distribution#######

gen_counts = df_user['geneticGender'].value_counts()
gen_percent = df_user['geneticGender'].value_counts(normalize=True)
gen_percent100 = df_user['geneticGender'].value_counts(normalize=True).mul(100).round(decimals = 1).astype(str) + '%'
genSumm = pd.DataFrame({'nusers': gen_counts, '%Users': gen_percent100})
genSumm.sort_values('%Users')

p = genSumm.index.values
genSumm.insert(0, column="gender",value = p)
genSumm.reset_index(drop=True, inplace=True)


###### calculating age ######
base = df_baseline
base['year'] = pd.DatetimeIndex(base['dateUpdate']).year
base['age']= base['year'] - base['birthYear']
age = pd.DataFrame(base['age'])
# ageFig = ff.create_distplot([age[c] for c in age.columns], age.columns, bin_size=3)


# data = [
#     {
#         'values': genSumm['gender'],
#         'type': 'pie',
#     }],

# fig = px.pie(genSumm,
#                                                         values='#users',
#                                                         names='gender',
#                                                         title='gender distribution',
#                                                         hole=0.3
#                                                               )

# fig = go.Figure(data=[go.Pie(labels=genSumm['gender'], values=genSumm['#users'], hole=.3)])
# fig.update_layout(title='Gender distribution')
# fig.show()

layout = go.Layout(
    margin = go.layout.Margin(t=0, l=0, r=0, b=0)
)
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
                                    html.Table(make_dash_table(df_user)),
                                ],
                                className="six columns",
                            ),
                        ],
                            className="row",
                        style={"margin-bottom": "35px"},
                    ),
                    #PIe chart
                    html.Div
                    (
                        [
                                html.Div(
                                            [html.H6(["Gender Distribution"], className="subtitle padded"),
                                                dcc.Graph(id='gender_pie',
                                                          figure={'data': [go.Pie(labels=genSumm['gender'],values=genSumm['nusers'])
                                                                          ],
                                                                   'layout' : layout},
                                                         ),
                                            ],
                                  style={"height": "10%", "width": "25%"},
                                ),
                        ],
                        className="sub-page", id="sub-page"
                    ),
                    # Age histogram/density plot
                    html.Div
                        (
                        [
                            html.Div(
                                [html.H6(["Age Density plot"], className="subtitle padded"),
                                 dcc.Graph(id='age_dist',
                                           figure={'data': [ff.create_distplot([age[c] for c in age.columns], age.columns, bin_size=3)
                                                            ],
                                           ),
                                 ],
                                style={"height": "10%", "width": "25%"},
                            ),
                        ],
                        className="sub-page", id="sub-page"
                    ),

                ]
            ),
        ],
        className="page",
    )
