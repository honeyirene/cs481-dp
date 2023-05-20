#########################################
### <view page>
### mainly managed by SaeYeon Na.
#########################################

import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
import plotly.graph_objects as go
import random
import plotly
from dash.dependencies import Input, Output

# from dash_draggable import Draggable


app = dash.get_app()

dash.register_page(
    __name__,
    name="View",
    path="/view",
)


################ generate fake data #########################
# https://stackoverflow.com/questions/67977231/how-to-generate-random-time-series-data-with-noise-in-python-3
def random_timeseries(initial_value: float, volatility: float, count: int) -> list:
    time_series = [
        initial_value,
    ]
    for _ in range(count):
        time_series.append(
            time_series[-1] + initial_value * random.gauss(0, 1) * volatility
        )
    return time_series


data_x = random_timeseries(0.01, 4, 600)  # 19200
data_y = random_timeseries(0.01, 4, 600)  # 19200
data_z = random_timeseries(0.01, 4, 600)  # 19200
data_bvp = random_timeseries(0.01, 4, 600)  # 38400
data_eda = random_timeseries(0.01, 4, 600)  # 2400
data_hr_e4 = random_timeseries(0.01, 4, 600)
data_ibi = random_timeseries(0.01, 4, 600)  # 38400
data_temp = random_timeseries(36.5, 0.01, 600)  # 2400
data_brainwave_delta = random_timeseries(0.01, 4, 600)  # 75000
data_brainwave_theta = random_timeseries(0.01, 4, 600)  # 75000
data_brainwave_low_alpha = random_timeseries(0.01, 4, 600)  # 75000
data_brainwave_high_alpha = random_timeseries(0.01, 4, 600)  # 75000
data_brainwave_low_beta = random_timeseries(0.01, 4, 600)  # 75000
data_brainwave_high_beta = random_timeseries(0.01, 4, 600)  # 75000
data_brainwave_low_gamma = random_timeseries(0.01, 4, 600)  # 75000
data_brainwave_middle_gamma = random_timeseries(0.01, 4, 600)  # 75000
data_att = random_timeseries(50, 0.025, 600)
data_med = random_timeseries(50, 0.025, 600)
data_hr_ecg = random_timeseries(0.01, 4, 600)
data_audio = random_timeseries(0.01, 4, 600)
###########################################################
########### create line plot with the data ##################
# fig = make_subplots(rows=2, cols=1)
fig_acc = go.Figure()
fig_acc.add_trace(go.Scatter(y=data_x, mode="lines", name="x axis"))
fig_acc.add_trace(go.Scatter(y=data_y, mode="lines", name="y axis"))
fig_acc.add_trace(go.Scatter(y=data_z, mode="lines", name="z axis"))
fig_acc.update_layout(
    yaxis_title="g", margin=dict(l=1, r=1, t=1, b=1), height=100, legend_font_size=20
)

fig_bvp = go.Figure()
fig_bvp.add_trace(go.Scatter(y=data_bvp, mode="lines", name="BVP", showlegend=True))
fig_bvp.update_layout(
    yaxis_title="PPG", margin=dict(l=1, r=1, t=1, b=1), height=100, legend_font_size=30
)

fig_eda = go.Figure()
fig_eda.add_trace(go.Scatter(y=data_eda, mode="lines", name="EDA", showlegend=True))
fig_eda.update_layout(
    yaxis_title="uS", margin=dict(l=1, r=1, t=1, b=1), height=100, legend_font_size=30
)

fig_hr = go.Figure()
fig_hr.add_trace(go.Scatter(y=data_hr_e4, mode="lines", name="E4"))
fig_hr.add_trace(go.Scatter(y=data_hr_ecg, mode="lines", name="ECG"))
fig_hr.update_layout(
    yaxis_title="Heart Rate",
    margin=dict(l=1, r=1, t=1, b=1),
    height=100,
    legend_font_size=30,
)

fig_ibi = go.Figure()
fig_ibi.add_trace(go.Scatter(y=data_ibi, mode="lines", name="IBI", showlegend=True))
fig_ibi.update_layout(
    yaxis_title="IBI", margin=dict(l=1, r=1, t=1, b=1), height=100, legend_font_size=40
)

fig_temp = go.Figure()
fig_temp.add_trace(
    go.Scatter(y=data_temp, mode="lines", name="Temperature", showlegend=True)
)
fig_temp.update_layout(
    yaxis_title="C", margin=dict(l=1, r=1, t=1, b=1), height=100, legend_font_size=9
)

fig_bw = go.Figure()
fig_bw.add_trace(go.Scatter(y=data_brainwave_delta, mode="lines", name="delta"))
fig_bw.add_trace(go.Scatter(y=data_brainwave_theta, mode="lines", name="theta"))
fig_bw.add_trace(go.Scatter(y=data_brainwave_low_alpha, mode="lines", name="low-alpha"))
fig_bw.add_trace(
    go.Scatter(y=data_brainwave_high_alpha, mode="lines", name="high-alpha")
)
fig_bw.add_trace(go.Scatter(y=data_brainwave_low_beta, mode="lines", name="low-beta"))
fig_bw.add_trace(go.Scatter(y=data_brainwave_high_beta, mode="lines", name="high-beta"))
fig_bw.add_trace(go.Scatter(y=data_brainwave_low_gamma, mode="lines", name="low-gamma"))
fig_bw.add_trace(
    go.Scatter(y=data_brainwave_middle_gamma, mode="lines", name="middle-gamma")
)
fig_bw.update_layout(
    yaxis_title="relative power",
    margin=dict(l=1, r=1, t=1, b=1),
    height=100,
    legend_itemwidth=30,
    legend_font_size=7,
)

fig_att_med = go.Figure()
fig_att_med.add_trace(go.Scatter(y=data_att, mode="lines", name="attention"))
fig_att_med.add_trace(go.Scatter(y=data_med, mode="lines", name="meditation"))
fig_att_med.update_layout(
    yaxis_title="attention & meditation",
    margin=dict(l=1, r=1, t=1, b=1),
    height=100,
    legend_font_size=10,
)

fig_audio = go.Figure()
fig_audio.add_trace(
    go.Scatter(y=data_audio, mode="lines", name="audio", showlegend=True)
)
fig_audio.update_layout(
    yaxis_title="audio",
    margin=dict(l=1, r=1, t=1, b=1),
    height=100,
    legend_font_size=20,
)
#######################################################################################
###### emotion label ###################
emotion_label = [
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="200",
        y0="-2",
        x1="300",
        y1="2",
        fillcolor="lightslategray",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="500",
        y0="-2",
        x1="600",
        y1="2",
        fillcolor="gray",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="0",
        y0="-2",
        x1="100",
        y1="2",
        fillcolor="black",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="100",
        y0="-2",
        x1="200",
        y1="2",
        fillcolor="darkslategray",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="400",
        y0="-2",
        x1="500",
        y1="2",
        fillcolor="lightslategray",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
]

emotion_label_temp = [
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="200",
        y0="-40",
        x1="300",
        y1="115",
        fillcolor="lightslategray",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="500",
        y0="-40",
        x1="600",
        y1="115",
        fillcolor="gray",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="0",
        y0="-40",
        x1="100",
        y1="115",
        fillcolor="black",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="100",
        y0="-40",
        x1="200",
        y1="115",
        fillcolor="darkslategray",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="400",
        y0="-40",
        x1="500",
        y1="115",
        fillcolor="lightslategray",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
]

emotion_label_am = [
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="200",
        y0="0",
        x1="300",
        y1="100",
        fillcolor="lightslategray",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="500",
        y0="0",
        x1="600",
        y1="100",
        fillcolor="gray",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="0",
        y0="0",
        x1="100",
        y1="100",
        fillcolor="black",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="100",
        y0="0",
        x1="200",
        y1="100",
        fillcolor="darkslategray",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
    dict(
        type="rect",
        xref="x",
        yref="y",
        x0="400",
        y0="0",
        x1="500",
        y1="100",
        fillcolor="lightslategray",
        opacity=0.4,
        line_width=0,
        layer="below",
    ),
]
fig_acc.update_layout(shapes=emotion_label)
fig_acc.update_layout(
    {"plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)"}
)
fig_bvp.update_layout(shapes=emotion_label)
fig_bvp.update_layout(
    {"plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)"}
)
fig_eda.update_layout(shapes=emotion_label)
fig_eda.update_layout(
    {"plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)"}
)
fig_hr.update_layout(shapes=emotion_label)
fig_hr.update_layout(
    {"plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)"}
)
fig_ibi.update_layout(shapes=emotion_label)
fig_ibi.update_layout(
    {"plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)"}
)
fig_temp.update_layout(shapes=emotion_label_temp)
fig_temp.update_layout(
    {"plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)"}
)
fig_att_med.update_layout(shapes=emotion_label_am)
fig_att_med.update_layout(
    {"plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)"}
)
fig_bw.update_layout(shapes=emotion_label)
fig_bw.update_layout(
    {"plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)"}
)
fig_audio.update_layout(shapes=emotion_label)
fig_audio.update_layout(
    {"plot_bgcolor": "rgba(0,0,0,0)", "paper_bgcolor": "rgba(0,0,0,0)"}
)
################################################
################ style #########################
colors = {
    "deep color": "#1091DB",
    "basic color": "#59C3FF",
    "white": "#FFFFFF",
    "black": "#000000",
    "background": "#F6FCFF",
    "darkgray": "#585757",
    "lightgray": "#D9D9D9",
}
##################################################


layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(
                    html.Div(html.B("User Data")), style={"color": colors["deep color"]}
                ),
                dbc.Col(html.Div("")),
                dbc.Col(
                    html.Div(html.B("Video")), style={"color": colors["deep color"]}
                ),
            ]
        ),
        html.Div(html.Br()),
        html.Div(
            children=[
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.P(
                                    children=[
                                        html.B("Name: Yu Jae-Seok"),
                                        html.Br(),
                                        html.B("    UID: U20230421003"),
                                        html.Br(),
                                        html.B("    Date: 2023-04-21"),
                                    ]
                                )
                            ]
                        ),
                        dbc.Col(html.Div("")),
                        dbc.Col(
                            children=[
                                html.Img(
                                    src="https://i.ibb.co/ctFP3Sg/1.png",
                                    style={"height": 150, "width": 240},
                                ),
                                html.Br(),
                                # dcc.Graph(figure=fig_audio.rangeslider),
                                html.Div(
                                    dcc.RangeSlider(
                                        id="time_slider",
                                        min=0,
                                        max=600,
                                        marks=None,
                                        value=[0, 600],
                                        tooltip={
                                            "placement": "bottom",
                                            "always_visible": True,
                                        },
                                    )
                                ),
                            ]
                        ),
                    ]
                )
            ]
        ),
        html.Div(
            html.Div(
                children=html.B("Data View"), style={"color": colors["deep color"]}
            )
        ),
        html.Div(html.Br()),
        html.Div(
            # [
            # Draggable(
            [
                dbc.Accordion(
                    [
                        dbc.AccordionItem(
                            dcc.Graph(figure=fig_acc, id="acc"),
                            title="3-axis Acceleration",
                            item_id="acc",
                        ),
                        dbc.AccordionItem(
                            dcc.Graph(figure=fig_bvp, id="bvp"),
                            title="BVP",
                            item_id="bvp",
                        ),
                        dbc.AccordionItem(
                            dcc.Graph(figure=fig_eda, id="eda"),
                            title="EDA",
                            item_id="eda",
                        ),
                        dbc.AccordionItem(
                            dcc.Graph(figure=fig_hr, id="hr"),
                            title="Heart Rates",
                            item_id="hr",
                        ),
                        dbc.AccordionItem(
                            dcc.Graph(figure=fig_ibi, id="ibi"),
                            title="IBI",
                            item_id="ibi",
                        ),
                        dbc.AccordionItem(
                            dcc.Graph(figure=fig_temp, id="temp"),
                            title="Body Temperature",
                            item_id="temp",
                        ),
                        dbc.AccordionItem(
                            dcc.Graph(figure=fig_att_med, id="a&m"),
                            title="Attention and Meditation",
                            item_id="a&m",
                        ),
                        dbc.AccordionItem(
                            dcc.Graph(figure=fig_bw, id="bw"),
                            title="BrainWave",
                            item_id="bw",
                        ),
                        dbc.AccordionItem(
                            dcc.Graph(figure=fig_audio, id="audio"),
                            title="Audio",
                            item_id="audio",
                        ),
                    ],
                    always_open=True,
                    active_item=[
                        "acc",
                        "bvp",
                        "eda",
                        "hr",
                        "ibi",
                        "temp",
                        "a&m",
                        "bw",
                        "audio",
                    ],
                )
            ]
        ),
    ]
)

# ]
# )


@app.callback(
    [
        dash.dependencies.Output("acc", "figure"),
        dash.dependencies.Output("bvp", "figure"),
        dash.dependencies.Output("eda", "figure"),
        dash.dependencies.Output("hr", "figure"),
        dash.dependencies.Output("ibi", "figure"),
        dash.dependencies.Output("temp", "figure"),
        dash.dependencies.Output("a&m", "figure"),
        dash.dependencies.Output("bw", "figure"),
        dash.dependencies.Output("audio", "figure"),
    ],
    [dash.dependencies.Input("time_slider", "value")],
)
def update_plots(active_range):
    for fig in [
        fig_acc,
        fig_bvp,
        fig_eda,
        fig_hr,
        fig_ibi,
        fig_temp,
        fig_att_med,
        fig_bw,
        fig_audio,
    ]:
        fig.update_layout(xaxis=dict(range=active_range))
    return (
        fig_acc,
        fig_bvp,
        fig_eda,
        fig_hr,
        fig_ibi,
        fig_temp,
        fig_att_med,
        fig_bw,
        fig_audio,
    )


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    # view.run_server(debug=True)
    print("skip")
