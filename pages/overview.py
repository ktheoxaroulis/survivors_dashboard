import sys
sys.path.insert(0, '../')

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from datetime import date
# import plotly.figure_factory as ff
import seaborn as sns


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


######### datewise number of registered users#########
reg_counts = df_user['dateUpdate'].value_counts()
reg_percent = df_user['dateUpdate'].value_counts(normalize=True)
reg_percent100 = df_user['dateUpdate'].value_counts(normalize=True).mul(100).round(decimals = 1).astype(str) + '%'
regSumm = pd.DataFrame({'nusers': reg_counts, '%Users': reg_percent})
p = regSumm.index.values
regSumm.insert(0, column="date",value = p)
regSumm.reset_index(drop=True, inplace=True)
regSumm.sort_values(by="date")


######### code for gender distribution#######

gen_counts = df_user['geneticGender'].value_counts()
gen_percent = df_user['geneticGender'].value_counts(normalize=True)
gen_percent100 = df_user['geneticGender'].value_counts(normalize=True).mul(100).round(decimals = 1).astype(str) + '%'
genSumm = pd.DataFrame({'nusers': gen_counts, '%Users': gen_percent100})
genSumm.sort_values('%Users')

p = genSumm.index.values
genSumm.insert(0, column="gender",value = p)
genSumm.reset_index(drop=True, inplace=True)


###### calculating age & plotting distribution of age######
base = df_user
base['age'] = date.today().year - base['birthYear']
chart1 = px.histogram(data_frame=base,
             x="age",
             color="geneticGender",
             title="Distribution of age by gender",
             hover_data=base.columns)


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

######### plotting maps #######
# country = pd.DataFrame(db.df_precovid['d_country,'])
coun_counts = db.df_precovid['d_country,'].value_counts()
coun_percent = db.df_precovid['d_country,'].value_counts(normalize=True)
coun_percent100 = db.df_precovid['d_country,'].value_counts(normalize=True).mul(100).round(decimals = 1).astype(str) + '%'
counSumm = pd.DataFrame({'nusers': coun_counts, '%Users': coun_percent100})
country = counSumm.index.values
counSumm.insert(0, column="country", value=country)
counSumm.reset_index(drop=True, inplace=True)

fig_map = px.choropleth(counSumm, locations="country", locationmode='country names',
                     color="nusers", hover_name="country",hover_data=[counSumm.nusers], projection="mercator",
                     # animation_frame="Date",width=1000, height=700,
                     # color_continuous_scale='Reds',
                     range_color=[1,40],
                     title='World Map of Coronavirus')

fig_map.update(layout_coloraxis_showscale=True)
# # py.offline.iplot(fig_map)

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
                                                    ["Registered Users"], className="subtitle padded"
                                                ),
                                                # html.Table(make_dash_table(regSumm)),
                                                dcc.Graph(
                                                    id='GrapGo',
                                                    figure=
                                                    {
                                                        'data':
                                                        [
                                                            go.Scatter
                                                            (
                                                                x=(regSumm['date']),
                                                                y=(regSumm['nusers']),
                                                                mode="markers+lines",
                                                                name='scatter'
                                                            )

                                                        ],
                                                        'layout': go.Layout
                                                        (
                                                            title="# of registered users",
                                                            xaxis={'title': 'Date'},
                                                            yaxis={'title': '# of users'},
                                                            yaxis_type='category'

                                                        ),
                                                    },
                                                ),

                                            ],
                                            className="five columns",
                                        ),
                                        html.Div(
                                            [html.H6(["Gender Distribution"], className="subtitle padded"),
                                             dcc.Graph(id='gender_pie',
                                                       figure={'data': [
                                                           go.Pie(labels=genSumm['gender'], values=genSumm['nusers'], hole=0.3)
                                                           ],
                                                               'layout': layout},
                                                       ),
                                             ],
                                            style={"height": "0.5%"},
                                            className="seven columns"
                                        ),
                        ],
                        className="row",
                        # style={"margin-bottom": "35px"},
                    ),


                    # Row 5
                    # Age histogram/density plot
                            html.Div
                                (
                                    [
                                        html.Div(
                                            [html.H6(["Age Histogram by Gender"], className="subtitle padded"),
                                             dcc.Graph(id='age_dist',
                                                       figure=chart1,
                                                       ),
                                             ],
                                            # style={"height": "1%", "width": "50%"},
                                            className="five columns"
                                        ),
                                        html.Div(
                                            [html.H6(["Number of cases by country"], className="subtitle padded"),
                                             dcc.Graph(id='map_country',
                                                       figure=fig_map,
                                                       ),
                                             ],
                                            # style={"height": "10%", "width": "75%"},
                                            className="seven columns"
                                        ),
                                    ],
                                    className="row"
                                ),
                            ],
                            className="sub-page", id="sub-page",
                ),
        ],
        className="page",
    )
