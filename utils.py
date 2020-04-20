import dash_html_components as html
import dash_core_components as dcc
import dash_daq as daq

def Header(app):
   return html.Div([get_header(app), html.Br([]), get_menu()])

def get_header(app):
    header = html.Div(
        [
            html.Div(
                id="header",
                className="banner row",
                children=[
                    html.Img( src=app.get_asset_url("dash-financial-logo.png" ),style={'height':'10%', 'width':'10%'},),
                    html.A(id="controls", children=[
                        html.Button("Print PDF", className="button no-print print",style={'position': "absolute", 'top': '-40',  'right': '0'}, id="las-print"),
                        html.A(daq.ToggleSwitch(id="toggleTheme", className="no-print", style={'position': "absolute", 'top': '-45',  'right': '0'}, value=False, color="#98151b")),
                    ],),

                  ],
            ),
            html.Div(
                [
                    html.Div(
                        [html.H5("CoVid-19 Recovered Analysis Report")],
                        className="seven columns main-title",
                    ),
                ],
                className="twelve columns",
                style={"padding-left": "0"},
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
                    dcc.Link("Overview", href="/"),
                    dcc.Link("Doctors Page", href="/"),
                    dcc.Link("Government Page", href="/"),
                    dcc.Link("Researchers Page", href="/"),
                    dcc.Link("News & Reviews", href="/"),
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
