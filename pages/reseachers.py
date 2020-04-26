import sys
sys.path.insert(0, '../')
import os
import dash_html_components as html
from utils import Header, make_dash_table
import dash_bootstrap_components as dbc


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
                                    html.Div(
                                        [
                                            html.H5("Data"),
                                            html.Br([]),
                                            html.P([" The Survivors public data set constitutes patient data from the Survivors App after a data cleaning process:" , html.P(),
                                                "Variables included are:" ,html.P(),"Epidimiological Data such as : ", html.Li("age",style={"color": "#ffffff"}), html.Li("genetic gender",style={"color": "#ffffff"}),
                                               html.Li("date of COVID diagnosis",style={"color": "#ffffff"}),html.Li("Country of redicence",style={"color": "#ffffff"}),"Historical medical data such as : "
                                               , html.Li("medical hitory of patient",style={"color": "#ffffff"}), html.Li("drugs",style={"color": "#ffffff"}), "Accute Phase data such as :",
                                                html.Li("symptoms",style={"color": "#ffffff"}), html.Li("dates of sickness",style={"color": "#ffffff"}), "Recovered Phase data such as :",
                                                html.Li("symptoms in the recovery phase",style={"color": "#ffffff"}), html.Li("WHODAS survey in the recovery phase",style={"color": "#ffffff"}), html.P(),
                                                "The public data set is anonymized using our data protection concept."
                                            ], style={"color": "#ffffff"}
                                             ),
                                        ], className="six columns product"),
                                    html.Div(
                                        [
                                    html.H6(["Data File Zip"], className="subtitle padded"),
                                            dbc.Button("Download Zip File", id="open"),
                                            dbc.Modal(
                                                [
                                                    dbc.ModalHeader(html.P(["Download", html.Br(),"Survivors Data public data set"])),
                                                    dbc.ModalBody(html.P(["PUBLIC DATA SET TERMS OF AGREEMENT",
                                                    html.Li("I will only use the Survivors Team  public data set for personal research on COVID - 19."),
                                                    html.Li("I agree to preserve, at all times, the confidentiality of the information.In particular, I undertake not to attempt to compromise or otherwise infringe the confidentiality of information of patients."),
                                                    html.Li("I agree that I have expertise to analyse and interpret the Survivors  data based on statistical guidelines."),
                                                    html.Li("I agree to recognize the contribution of the  Survivors Team  study group and to include a proper acknowledgement in any work based on the Survivors data.")
                                                    ])),
                                                    dbc.ModalFooter( [ html.A(dbc.Button( "AGREE", id="bclose", className="ml-auto", style={'margin':'auto','align':'left'}), id='download-link'),
                                                                     dbc.Button("DISAGREE", id="bclose2", className="ml-auto",style={'margin-left':'5%','align-items': 'flex-end','align':'right'})], className="row "

                                                                     ),
                                                ],


                                                id="modal",
                                                size="lg",
                                                scrollable=True,
                                            ),
                                        ], className="six columns",
                                    ),
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


