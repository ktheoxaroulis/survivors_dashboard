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
                    dcc.Link("OVERVIEW", href="",className="tab first"),
                    dcc.Link("MEDICAL", href="",className="tab"),
                    dcc.Link("GOVERNMENT", href="",className="tab"),
                    dcc.Link("RESEARCH", href="",className="tab"),
                    dcc.Link("NEWS + REVIEWS", href="",className="tab"),
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
