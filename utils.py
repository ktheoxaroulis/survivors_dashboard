import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq

def Header(app):
   return html.Div([get_header(app), get_menu()])

def get_header(app):
    header = html.Div(
        [
            html.Div(
                id="header",
                className="banner row",
                children=[
                    html.Img( src=app.get_asset_url("dash-financial-logo.png" ),style={'width':'30%'},),
                    html.A(id="controls", children=[
                    html.Button("Print PDF", className="button no-print print",style={'position': "absolute", 'top': '-40',  'right': '0'}, id="las-print"),
                    ],
                    ),

                  ],
            ),
            html.Div(
                [
                    html.Div(
                        [ daq.ToggleSwitch(id="toggleTheme", className="no-print", value=False, color="#3BB539",style={"position": "absolute", "top": "1", 'right': '0'}),
                         html.H4("CoVid-19 Recovered Analysis Report",className="main-title"), ],
                    ),
                ],
                className="banner row",
            ),
        ],
        className="row",
    )
    return header

def get_menu():
    menu = html.Div(
                id="tabs",
                className="row all-tabs",
                children=[
                    dcc.Link("Overview", href="",className="tab first"),
                    dcc.Link("Doctors Page", href="",className="tab"),
                    dcc.Link("Government Page", href="",className="tab"),
                    dcc.Link("Researchers Page", href="",className="tab"),
                    dcc.Link("News & Reviews", href="",className="tab"),
                    # dcc.Link("Overview", href="/report/overview", className="tab first"),
                    # dcc.Link("Doctors Page", href="/report/doctors", className="tab"),
                    # dcc.Link("Government Page", href="/report/government", className="tab"),
                    # dcc.Link("Researchers Page", href="/report/reseachers", className="tab"),
                    # dcc.Link("News & Reviews", href="/report/news-and-reviews", className="tab"),
                ],
            )
    return menu


def make_dash_table(df):
    """ Return a dash definition of an HTML table for a Pandas dataframe """
    table = []
    for index, row in df.iterrows():
        html_row = []
        for i in range(len(row)):
            html_row.append(html.Td([row[i]]))
        table.append(html.Tr(html_row))
    return table
