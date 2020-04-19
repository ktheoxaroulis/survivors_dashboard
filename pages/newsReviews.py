import dash_html_components as html
from utils import Header


def create_layout(app):
    return html.Div(
        [
            Header(app),
            # page 6
            html.Div(
                [
                    # Row 1
                    html.Div(
                        [
                            html.Div(
                                [
                                    html.H6("News", className="subtitle padded"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.P(
                                                "18/04/2020    The rise of webppage analysis"
                                            ),
                                        ],
                                    ),
                                ],
                                className="row",
                            ),
                            html.Div(
                                [
                                    html.H6("Reviews", className="subtitle padded"),
                                    html.Br([]),
                                    html.Div(
                                        [
                                            html.P("Launched in 2020."),
                                                                                   ],
                                    ),
                                ],
                                className="row",
                            ),
                        ],
                        className="row ",
                    )
                ],
                className="sub-page", id="sub-page"
            ),
        ],
        className="page",
    )
