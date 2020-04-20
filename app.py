# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from pages import (
    overview,
    doctors,
    government,
    reseachers,
    newsReviews,
)


app = dash.Dash(
    __name__, meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
app.title = 'Survivors'
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
server = app.server


# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


# Callback updating backgrounds
@app.callback(
    [
    Output("sub-page", "className"),
    ],
    [Input("toggleTheme", "value")],
)
def update_background(turn_dark):

    if turn_dark:
        return ["dark-sub-page"]
    else:
        return ["light-sub-page"]

# Update page
@app.callback(Output("page-content", "children") , [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/report/doctors":
        return doctors.create_layout(app)
    elif pathname == "/report/government":
        return government.create_layout(app)
    elif pathname == "/report/reseachers":
        return reseachers.create_layout(app)
    elif pathname == "/report/news-and-reviews":
        return newsReviews.create_layout(app)
    else:
        return overview.create_layout(app)

# Update page
@app.callback(Output("tabs", "children"), [Input("url", "pathname")])
def display_menustyle(pathname):
    tabs = [
        dcc.Link("Overview", href="/report/overview",className="tab first"),
        dcc.Link("Doctors Page", href="/report/doctors",className="tab"),
        dcc.Link("Government Page", href="/report/government",className="tab"),
        dcc.Link("Researchers Page", href="/report/reseachers",className="tab"),
        dcc.Link("News & Reviews", href="/report/news-and-reviews",className="tab"),
    ]

    if pathname == "/report/doctors":
        tabs[1] = dcc.Link(
            dcc.Markdown("**&#9632 Doctors Page**"),
            href="/report/doctors",className="tab"
        )
        return tabs
    elif pathname == "/report/government":
        tabs[2] = dcc.Link(
            dcc.Markdown("**&#9632 Government Page**"),
            href="/report/government",className="tab"
        )
        return tabs
    elif pathname == "/report/reseachers":
        tabs[3] = dcc.Link(
            dcc.Markdown("**&#9632 Researchers Page**"),
            href="/report/reseachers",className="tab"
        )
        return tabs
    elif pathname == "/report/news-and-reviews":
        tabs[4] = dcc.Link(
            dcc.Markdown("**&#9632 News & Reviews**"),
            href="/report/news-and-reviews",className="tab"
        )
        return tabs
    else:
        tabs[0] = dcc.Link(
            dcc.Markdown("**&#9632 Overview**"),
            href="/report/Overview",className="tab first"
        )
        return tabs


if __name__ == "__main__":
    app.run_server(debug=False)
