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
df_age_hosp = pd.read_csv(DATA_PATH.joinpath("anova.csv"))
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
regSumm = regSumm.sort_values(by="date")


######### code for gender distribution#######

gen_counts = df_user['geneticGender'].value_counts()
gen_percent = df_user['geneticGender'].value_counts(normalize=True)
gen_percent100 = df_user['geneticGender'].value_counts(normalize=True).mul(100).round(decimals = 1).astype(str) + '%'
genSumm = pd.DataFrame({'nusers': gen_counts, '%Users': gen_percent100})
genSumm.sort_values('%Users')

p = genSumm.index.values
genSumm.insert(0, column="gender",value = p)
genSumm.reset_index(drop=True, inplace=True)
gen_pie = px.pie(genSumm, values='nusers', names='gender',hole=.3, color_discrete_sequence=px.colors.sequential.Blugrn)


###### calculating age & plotting distribution of age######
base = df_user
base['age'] = date.today().year - base['birthYear']
age_histogram = px.histogram(data_frame=base,
             x="age",
             color="geneticGender",
             # title="Distribution of age by gender",
             hover_data=base.columns,
             marginal="box",
             color_discrete_sequence = px.colors.colorbrewer.Pastel1)

age_histogram.layout.font = dict(family="Helvetica", size = 10)


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
                     range_color=[1,40]
                     # title='World Map of Coronavirus'
                        )

fig_map.update(layout_coloraxis_showscale=True)
# # py.offline.iplot(fig_map)

layout = go.Layout(
    margin = go.layout.Margin(t=40, l=30, r=30, b=40)
)

#### boxplots for association between age and hospital duration #######
age_hospital = px.box(df_age_hosp, x="age", y="hospitalDuration", points="all",
            color="age",
            color_discrete_sequence=px.colors.colorbrewer.Pastel1,
            category_orders={"age": ["<10", "11-20", "21-35", "36-49", ">50"]},
            template='presentation'
            )
age_hospital.layout.font = dict(family="Helvetica", size=10)


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
                                        "The Survivors App is an adaptable application which can be used to track survivors of any pandemic wave or virus.\
                                         Individuals input their symptoms which are store to real - time databases."),
                                    html.P("These data are organized in 3 distinct categories, namely: " ),
                                    html.Li( "Data collected on registration - Collected Once: On registration, the user anonymously provides \
                                    baseline information on demographic and socio-economic background as well as current medication and past medical history.\
                                     Then the patient provides important information regarding the COVID-19 infection period which includes type and results of \
                                     tests used for diagnosis, symptoms experienced, if they stayed at home or consequently were hospitalized, information on the \
                                     medical and non-medical treatment received during this period."  ),
                                    html.Li("Data collected on a daily basis :  After the initial registration, the patient is able to enter the experienced \
                                    symptoms on a daily basis.These are selected from a wide range of symptoms organized per anatomic region(head, chest, gastrointestinal,\
                                     etc.) for easier and more intuitive search.Additionally, if the patient has the means, measurements of temperature and blood pressure \
                                     can be entered as well."  ),
                                    html.Li("Data collected periodically: Patients that survive COVID-19 can have impaired heart and lung function and diminished physical \
                                    capacity. As with survivors of SARS, potential mental health consequences are to be expected. The evolution of the survivors’ overall \
                                    disability across 6 functioning domains (cognition, mobility, self-care, getting along, life activities (household and work/school) and \
                                    participation in society) will be assessed over time. This will be done with the adult self-administered version of the World Health\
                                     Organization Disability Assessment Schedule 2.0 (WHODAS 2.0) once every 30 days. It is a 36-item measure and each item on the self-administered \
                                     version of the WHODAS 2.0 asks the individual to rate how much difficulty he or she has had in specific areas of functioning during the past \
                                     30 day on a scale ranging from  “none” (1) to “extreme” (5). The answers are then summed and scored according to WHO methodology." ),
                                    html.P("Their important anonymous recovery data are immediately available on this dashboard providing insights for doctors, governments \
                                    and researchers on a worldwide scale."),
                                       ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),
                    ##Row4
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("Association between Age and Hospital Duration"),
                                    html.Br([]),
                                    dcc.Graph(id='age_hosp',
                                              figure=age_hospital,
                                              ),
                                ],
                                className="twelve columns",
                            )
                        ],
                        className="row",
                    ),
                    # Row 5
                    html.Div(
                        [
                                        html.Div(
                                            [
                                                html.H6(
                                                    ["Registered Users"], className="subtitle padded"
                                                ),
                                                # html.Table(make_dash_table(regSumm)),
                                                dcc.Graph(
                                                    id='user_trend',
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
                                                            title="Number of registered users",
                                                            xaxis={'title': 'Date'},
                                                            yaxis={'title': '# of users'}
                                                            # xaxis_type='category',
                                                            # yaxis_type='category'

                                                        ),
                                                    },
                                                ),

                                            ],
                                            className="five columns",
                                        ),
                                        html.Div(
                                            [html.H6(["Gender Distribution"], className="subtitle padded"),
                                             dcc.Graph(id='gender_pie',
                                                       figure=gen_pie,
                                                       ),
                                             ],
                                            # style={"height": "0.05%"},
                                            className="seven columns"
                                        ),
                        ],
                        className="row",
                        # style={"margin-bottom": "35px"},
                    ),


                    # Row 6
                    # Age histogram/density plot
                            html.Div
                                (
                                    [
                                        html.Div(
                                            [html.H6(["Age Histogram by Gender"], className="subtitle padded"),
                                             dcc.Graph(id='age_dist',
                                                       figure=age_histogram,
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
