import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq

def Header(app):
   return html.Div([get_header(app), get_menu()])

def Footer(app):
   return html.Div([get_footer(app)])

def get_header(app):
    header = html.Div(
        [
            html.Div(
                id="header",
                className="header margrow row",
                children=[
                    html.Img( src=app.get_asset_url("logo.png" ),className="logo"),
                    html.A(id="controls", children=[
                        html.Button("Print PDF", className="mbutton button no-print print", id="las-print"),
                    ],
                           ),
                  ],
            ),
            html.Div(
                [
                    html.Div(
                        [


                         html.H4("CoVid-19 Recovered Analysis Report",className="main-title"), ],
                    ),
                ],
                className="banner row",
            ),
        ],
    )
    return header

def get_menu():
    menu = html.Div(
                id="tabs",
                className="row all-tabs",
                children=[
                            dcc.Link("OVERVIEW", href="/report/overview",className="tab first"),
                            dcc.Link("MEDICAL", href="/report/doctors",className="tab"),
                            dcc.Link("GOVERNMENT", href="/report/government",className="tab"),
                            dcc.Link("RESEARCH", href="/report/reseachers",className="tab"),
                            dcc.Link("NEWS + REVIEWS", href="/report/news-and-reviews",className="tab"),
                ],
            )
    return menu

def get_footer(app):
    header =  html.Div(
                        [
                            html.H5("Product Summary",className = "footerTitle"),
                            html.Br([]),
                            html.P(  "The Survivors App is an adaptable application which can be used to track survivors of any pandemic wave or virus.\
                            Individuals input their symptoms which are store to real - time databases.",className = "footerTxt"),
                            html.Button("Learn More", className="lbutton button no-print print", id="las-learn"),
                            html.Div(id="las-learn2", children=[html.P( "The Data collected for this Dashboard has been self-reported from Survivors using the mobile App. The data is organized in 3 distinct categories, namely:" ,className = "footerTitle2"),
                            html.Div([html.P("1. Data collected on registration - Collected Once:"), html.P("On registration, the user anonymously provides baseline information on demographic and socio-economic background as well as current medication and past medical history. Then the patient provides important information regarding the COVID-19 infection period which includes type and results of tests used for diagnosis, symptoms experienced, if they stayed at home or consequently were hospitalized, information on the medical and non-medical treatment received during this period."),
                            html.P("2. Data Collected on a Daily Basis:"),html.P(" After the initial registration, the patient is able to enter the experienced symptoms on a daily basis.These are selected from a wide range of symptoms organized per anatomic region(head, chest, gastrointestinal, etc.) for easier and more intuitive search.Additionally, if the patient has the means, measurements of temperature and blood pressure can be entered as well."),
                            html.P(" 3. Data collected periodically: "), html.P("Patients that survive COVID-19 can have impaired heart and lung function and diminished physical capacity. As with survivors of SARS, potential mental health consequences are to be expected. The evolution of the survivors’ overall disability across 6 functioning domains (cognition, mobility, self-care, getting along, life activities (household and work/school) and participation in society) will be assessed over time. This will be done with the adult self-administered version of the World Health Organization Disability Assessment Schedule 2.0 (WHODAS 2.0) once every 30 days. It is a 36-item measure and each item on the self-administered version of the WHODAS 2.0 asks the individual to rate how much difficulty he or she has had in specific areas of functioning during the past 30 day on a scale ranging from “none” (1) to “extreme” (5). The answers are then summed and scored according to WHO methodology.\
                            Their important anonymous recovery data are immediately available on this dashboard providing insights for doctors, governments and researchers on a worldwide scale.")
                                    ],className="footerTxt2",)
                                                                ])
                        ],
                        className="footer",
                    )

    return header

def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
