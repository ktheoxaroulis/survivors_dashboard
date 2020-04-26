# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import os
import dash_html_components as html
from dash.dependencies import Input, Output, State
from db import recovered_symptoms, df_survey,df_baseline,df_user
import plotly.graph_objs as go
import plotly.express as px
from urllib.parse import quote as urlquote
from flask import send_file
import zipfile
import dash_bootstrap_components as dbc

# external JavaScript files
external_scripts = [
"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css",
"https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js",
"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"
]

from pages import (
    overview,
    doctors,
    government,
    reseachers,
    newsReviews,
)

app = dash.Dash(
    __name__, external_scripts=external_scripts,external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[{"name": "viewport", "content": "width=device-width"}]
)
app.title = 'Survivors Dashboard'
server = app.server


# Describe the layout/ UI of the app
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")] )

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

@app.callback(
    dash.dependencies.Output('symp-barplot', 'figure'),
    [dash.dependencies.Input('symptom-cluster-select', 'value'),
     dash.dependencies.Input('symptom-cluster-level', 'value')])
def udpate_sym_plot(selection1,selection2):
    symptom_cluster_level=["Mid" , "Sever", "Extreme"]
    sel_index=symptom_cluster_level.index(selection2)

    if (selection1=="Breath") :
        tmp = recovered_symptoms.iloc[:, [0, 11, 12, 13, 14]].groupby("User_ID").max()
        tmp = (tmp[tmp >= sel_index].count() / tmp.count()).to_frame().reset_index()
        tmp = tmp.rename(columns={"index": "Symptoms", 0: "%"})
        tmp['Symptoms'] = tmp['Symptoms'].str.replace('Symp_breath_', '')
        tmp['Symptoms'] = tmp['Symptoms'].str.replace('_', ' ')
        figure = px.bar(tmp, x="Symptoms", y="%" )
        figure.update_layout(uniformtext_minsize=2, font=dict(size =12), title_font_size=11, title_text="% of recovered with symptoms over total recovered", uniformtext_mode='hide', xaxis_tickangle=-35)
        return figure
    elif (selection1=="Heart"):
        tmp = recovered_symptoms.iloc[:, [0, 11, 12, 13, 14]].groupby("User_ID").max()
        tmp = (tmp[tmp >= sel_index].count() / tmp.count()).to_frame().reset_index()
        tmp = tmp.rename(columns={"index": "Symptoms", 0: "%"})
        tmp['Symptoms'] = tmp['Symptoms'].str.replace('Symp_heart_', '')
        tmp['Symptoms'] = tmp['Symptoms'].str.replace('_', ' ')
        figure = px.bar(tmp, x="Symptoms", y="%")
        figure.update_layout(uniformtext_minsize=2, font=dict(size =12), title_font_size=11, title_text="% of recovered with symptoms over total recovered", uniformtext_mode='hide', xaxis_tickangle=-35)
        return figure

    elif(selection1=="Gastro"):
        tmp = recovered_symptoms.iloc[:, [0, 15, 16, 17, 18]].groupby("User_ID").max()
        tmp = (tmp[tmp >= sel_index].count() / tmp.count()).to_frame().reset_index()
        tmp = tmp.rename(columns={"index": "Symptoms", 0: "%"})
        tmp['Symptoms'] = tmp['Symptoms'].str.replace('Symp_gastro_', '')
        tmp['Symptoms'] = tmp['Symptoms'].str.replace('_', ' ')
        figure = px.bar(tmp, x="Symptoms", y="%")
        figure.update_layout(uniformtext_minsize=2, font=dict(size =12), title_font_size=11, title_text="% of recovered with symptoms over total recovered", uniformtext_mode='hide', xaxis_tickangle=-35)
        return figure

    elif(selection1=="Well Being"):
        tmp = recovered_symptoms.iloc[:, [0, 19, 20, 21, 22, 23, 24, 25]].groupby("User_ID").max()
        tmp = (tmp[tmp >= sel_index].count() / tmp.count()).to_frame().reset_index()
        tmp = tmp.rename(columns={"index": "Symptoms", 0: "%"})
        tmp['Symptoms'] = tmp['Symptoms'].str.replace('Symp_well_Being_', '')
        tmp['Symptoms'] = tmp['Symptoms'].str.replace('_', ' ')
        figure = px.bar(tmp, x="Symptoms", y="%")
        figure.update_layout(uniformtext_minsize=2, font=dict(size =12), title_font_size=11, title_text="% of recovered with symptoms over total recovered", uniformtext_mode='hide', xaxis_tickangle=-35)
        return figure

    elif(selection1=="Pain"):
        tmp = recovered_symptoms.iloc[:, [0, 26, 27, 28, 29, 30, 31, 32, 33]].groupby("User_ID").max()
        tmp = (tmp[tmp >= sel_index].count() / tmp.count()).to_frame().reset_index()
        tmp = tmp.rename(columns={"index": "Symptoms", 0: "%"})
        tmp['Symptoms'] = tmp['Symptoms'].str.replace('Symp_pain', '')
        tmp['Symptoms'] = tmp['Symptoms'].str.replace('_', ' ')
        figure = px.bar(tmp, x="Symptoms", y="%")
        figure.update_layout(uniformtext_minsize=2, font=dict(size =12), title_font_size=11, title_text="% of recovered with symptoms over total recovered", uniformtext_mode='hide', xaxis_tickangle=-35)
        return figure

    else:
        tmp = recovered_symptoms.iloc[:, [0, 2, 3, 4, 5, 6]].groupby("User_ID").max()
        tmp = (tmp[tmp >= sel_index].count() / tmp.count()).to_frame().reset_index()
        tmp = tmp.rename(columns={"index": "Symptoms", 0: "%"})
        tmp['Symptoms'] = tmp['Symptoms'].str.replace('Symp_head', '')
        tmp['Symptoms'] = tmp['Symptoms'].str.replace('_', ' ')
        figure = px.bar(tmp, x="Symptoms", y="%" )
        figure.update_layout(uniformtext_minsize=2, font=dict(size =12), title_font_size=11, title_text="% of recovered with symptoms over total recovered", uniformtext_mode='hide', xaxis_tickangle=-35)
        return figure

@app.callback(
    dash.dependencies.Output('survey-barplot', 'figure'),
    [dash.dependencies.Input('survey-list-select', 'value')])
def udpate_sym_plot(selection1):
    tmp1 = df_survey.iloc[:, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]].sort_values('dateSubmitted').drop_duplicates(['userId'], keep='last')
    tmp1 = tmp1.drop(['userId', 'dateSubmitted'], axis=1).apply(lambda x: x.value_counts()).fillna(0).astype(int).T
    tmp1 = tmp1.div(tmp1.sum(1), 0).mul(100).round(2).assign(Total=lambda df: df.sum(axis=1))
    tmp1.drop(tmp1.columns[-1], axis=1, inplace=True)

    top_labels = ['No Answer', 'No', 'Mild', 'Medium,','Strong', 'Severe']

    colors = ['rgba(8, 117, 30, 0.8)', 'rgba(28, 112, 50, 0.8)',
              'rgba(34, 149, 57, 0.8)', 'rgba(54, 185, 71, 0.85)',
              'rgba(61, 195, 74, 1)', 'rgba(80, 229, 95, 1)']

    x_data = tmp1.values.tolist()

    y_data = ['Q1. Standing for long <br>' +
              'periods such as 30 minutes?',
              'Q2. Getting out of your home?',
              'Q3. Doing most important household <br>' +
              'tasks well?',
              'Q4. Getting your work done as quickly <br>' +
              ' as needed?',
              'Q5. Learning a new task <br>' +
              'for example learning how <br>' +
              'to get to a new place?',
              'Q6. Concentrating on doing <br> something for ten minutes?',
              'Q7. Staying by yourself for a few days?',
              'Q8. Preparing your own food? ',
              'Q9. Getting along with people <br> who are close to you?',
              'Q10. Making new friends? ',
              'Q11. Joining in community activities<br> (festivities,' +
              'religious or other)<br> in the way that you used to? ',
              'Q12. How much have you been emotionally<br>' +
              'affected by your health problems?']

    fig = go.Figure()

    for i in range(0, len(x_data[0])):
        for xd, yd in zip(x_data, y_data):
            fig.add_trace(go.Bar(
                x=[xd[i]], y=[yd],
                orientation='h',
                marker=dict(
                color=colors[i],
                line=dict(color='rgb(248, 248, 249)', width=1)
               )
            ))

    fig.update_layout(
        xaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
            domain=[0.15, 1]
        ),
        yaxis=dict(
            showgrid=False,
            showline=False,
            showticklabels=False,
            zeroline=False,
        ),
        barmode='stack',
        paper_bgcolor='rgb(248, 248, 255)',
        plot_bgcolor='rgb(248, 248, 255)',
        margin=dict(l=120, r=20, t=70, b=20),
        showlegend=False,
    )

    annotations = []

    for yd, xd in zip(y_data, x_data):
        # labeling the y-axis
        annotations.append(dict(xref='paper', yref='y',
                                x=0.14, y=yd,
                                xanchor='right',
                                text=str(yd),
                                font=dict(family='Arial', size=8,
                                          color='rgb(67, 67, 67)'),
                                showarrow=False, align='right'))
        # labeling the first percentage of each bar (x_axis)
        annotations.append(dict(xref='x', yref='y',
                                x=xd[0] / 2, y=yd,
                                text=str(xd[0]) + '%',
                                font=dict(family='Arial', size=11,
                                          color='rgb(248, 248, 255)'),
                                showarrow=False))
        # labeling the first Likert scale (on the top)
        if yd == y_data[-1]:
            annotations.append(dict(xref='x', yref='paper',
                                    x=xd[0] / 2, y=1.1,
                                    text=top_labels[0],
                                    font=dict(family='Arial', size=11,
                                              color='rgb(67, 67, 67)'),
                                    showarrow=False))
        space = xd[0]
        for i in range(1, len(xd)):
            # labeling the rest of percentages for each bar (x_axis)
            annotations.append(dict(xref='x', yref='y',
                                    x=space + (xd[i] / 2), y=yd,
                                    text=str(xd[i]) + '%',
                                    font=dict(family='Arial', size=11,
                                              color='rgb(248, 248, 255)'),
                                    showarrow=False))
            # labeling the Likert scale
            if yd == y_data[-1]:
                annotations.append(dict(xref='x', yref='paper',
                                        x=space + (xd[i] / 2), y=1.1,
                                        text=top_labels[i],
                                        font=dict(family='Arial', size=11,
                                                  color='rgb(67, 67, 67)'),
                                        showarrow=False))
            space += xd[i]
    fig.update_layout(annotations=annotations)
    return fig

@app.server.route('/data/download/Data.zip')
def download_csv():
    print("Test")
    return send_file('data/download/Data.zip', attachment_filename='Data.zip', as_attachment=True)

@app.callback(Output('download-link','href'),[ Input('bclose', 'n_clicks')])
def generate_report_url(k):
    directory = 'data/output/'
    # file_paths = get_all_file_paths(directory)
    # with ZipFile('data/download/Data.zip','w') as zip:
    #     for file in file_paths:
    #        zip.write(file)
    zip_dir(directory,"Data.zip")
    location = "/data/download/{}".format(urlquote("Data.zip"))
    return location

def zip_dir(directory, zipname):
    """
    Compress a directory (ZIP file).
    """
    if os.path.exists(directory):
        outZipFile = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)

        rootdir = os.path.basename(directory)

        for dirpath, dirnames, filenames in os.walk(directory):
            for filename in filenames:

                # Write the file named filename to the archive,
                # giving it the archive name 'arcname'.
                filepath   = os.path.join(dirpath, filename)
                parentpath = os.path.relpath(filepath, directory)
                arcname    = os.path.join(rootdir, parentpath)

                outZipFile.write(filepath, arcname)

    outZipFile.close()

def get_all_file_paths(directory):
    # initializing empty file paths list
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths

@app.callback( Output("modal", "is_open"),
    [Input("open", "n_clicks"), Input("bclose", "n_clicks"), Input("bclose2", "n_clicks")],
    [State("modal", "is_open")],
)
def toggle_modal(n1, n2, n3, is_open):
    if n1 or n2 or  n3:
        return not is_open
    return is_open



if __name__ == "__main__":
    app.run_server(debug=False)
