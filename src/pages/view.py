#view page. mainly managed by SaeYeon Na.

import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc
import plotly.graph_objects as go
import random

dash.register_page(
    __name__,
    name="View",
    path="/view",
    top_nav=True,
    top_nav_order=3,
)

################ generate fake data #########################
#https://stackoverflow.com/questions/67977231/how-to-generate-random-time-series-data-with-noise-in-python-3
def random_timeseries(initial_value: float, volatility: float, count: int) -> list:
    time_series = [initial_value, ]
    for _ in range(count):
        time_series.append(time_series[-1] + initial_value * random.gauss(0, 1)*volatility)
    return time_series
    
data_x = random_timeseries(0.01, 4, 19200)
data_y = random_timeseries(0.01, 4, 19200)
data_z = random_timeseries(0.01, 4, 19200)
data_bvp = random_timeseries(0.01, 4, 38400)
data_eda = random_timeseries(0.01, 4, 2400)
data_hr_e4 = random_timeseries(0.01, 4, 600)
data_ibi = random_timeseries(0.01, 4, 38400)
data_temp = random_timeseries(36.5, 155, 2400)
data_brainwave_delta = random_timeseries(0.01, 4, 75000)
data_brainwave_theta = random_timeseries(0.01, 4, 75000)
data_brainwave_low_alpha = random_timeseries(0.01, 4, 75000)
data_brainwave_high_alpha = random_timeseries(0.01, 4, 75000)
data_brainwave_low_beta = random_timeseries(0.01, 4, 75000)
data_brainwave_high_beta = random_timeseries(0.01, 4, 75000)
data_brainwave_low_gamma = random_timeseries(0.01, 4, 75000)
data_brainwave_middle_gamma = random_timeseries(0.01, 4, 75000)
data_att = random_timeseries(50, 100, 600)
data_med = random_timeseries(50, 100, 600)
data_hr_ecg = random_timeseries(0.01, 4, 600)
data_audio = random_timeseries(0.01, 4, 600)
###########################################################
########### create line plot with the data ##################
fig_acc = go.Figure()
fig_acc.add_trace(go.Scatter(y=data_x,
                        mode='lines',
                        name='x'))
fig_acc.add_trace(go.Scatter(y=data_y,
                         mode='lines',
                         name='y'))
fig_acc.add_trace(go.Scatter(y=data_z,
                         mode='lines',
                         name='z'))
fig_acc.update_layout(
    yaxis_title='g',
)

fig_bvp = go.Figure()
fig_bvp.add_trace(go.Scatter(y=data_bvp, mode='lines',name='BVP'))
fig_acc.update_layout(yaxis_title='PPG')

fig_eda = go.Figure()
fig_eda.add_trace(go.Scatter(y=data_eda, mode='lines',name='EDA'))
fig_eda.update_layout(yaxis_title='uS')

fig_hr = go.Figure()
fig_hr.add_trace(go.Scatter(y=data_hr_e4, mode='lines',name='E4'))
fig_hr.add_trace(go.Scatter(y=data_hr_ecg, mode='lines',name='ECG'))

fig_ibi = go.Figure()
fig_ibi.add_trace(go.Scatter(y=data_ibi, mode='lines',name='IBI'))

fig_temp = go.Figure()
fig_temp.add_trace(go.Scatter(y=data_temp, mode='lines',name='Body Temperature'))
fig_temp.update_layout(yaxis_title='C')

fig_bw = go.Figure()
fig_bw.add_trace(go.Scatter(y=data_brainwave_delta, mode='lines',name='delta'))
fig_bw.add_trace(go.Scatter(y=data_brainwave_theta, mode='lines',name='theta'))
fig_bw.add_trace(go.Scatter(y=data_brainwave_low_alpha, mode='lines',name='low-alpha'))
fig_bw.add_trace(go.Scatter(y=data_brainwave_high_alpha, mode='lines',name='high-alpha'))
fig_bw.add_trace(go.Scatter(y=data_brainwave_low_beta, mode='lines',name='low-beta'))
fig_bw.add_trace(go.Scatter(y=data_brainwave_high_beta, mode='lines',name='high-beta'))
fig_bw.add_trace(go.Scatter(y=data_brainwave_low_gamma, mode='lines',name='low-gamma'))
fig_bw.add_trace(go.Scatter(y=data_brainwave_middle_gamma, mode='lines',name='middle-gamma'))
fig_bw.update_layout(yaxis_title='relative power')

fig_att_med = go.Figure()
fig_att_med.add_trace(go.Scatter(y=data_att, mode='lines',name='attention'))
fig_att_med.add_trace(go.Scatter(y=data_med, mode='lines',name='meditation'))

fig_audio = go.Figure()
fig_audio.add_trace(go.Scatter(y=data_audio, mode='lines', name='audio'))
fig_audio.update_layout(
    xaxis=
        dict(
        rangeslider=
        dict(
        visible=True
        ),
        )
)
#######################################################################################

################ style #########################
colors = {
    'deep color': '#1091DB',
    'basic color': '#59C3FF',
    'white': '#FFFFFF',
    'black': '#000000',
    'background': '#F6FCFF',
    'darkgray': '#585757',
    'lightgray': '#D9D9D9'
}
##################################################

layout = html.Div(
    children=[
        dbc.Row(
            [
                dbc.Col(html.Div(html.B("User Data")), style={'color': colors['deep color']}),
                dbc.Col(html.Div("")),
                dbc.Col(html.Div(html.B("Video")), style={'color': colors['deep color']}),
             ]),
        html.Div(html.Br()),
        html.Div(
            children=[
                dbc.Row(
                    [
                        dbc.Col([html.P(children=[html.B("Name: Yu Jae-Seok"), html.Br(), html.B("    UID: U20230421003"), html.Br(), html.B("    Date: 2023-04-21")])]),
                        dbc.Col(html.Div("")),
                        dbc.Col(children = [
                            html.Img(src="https://i.ibb.co/ctFP3Sg/1.png", style={'height': 150, 'width': 240}), html.Br(),
                            #dcc.Graph(figure=fig_audio.rangeslider),
                            html.Div(dcc.RangeSlider(0, 600, marks=None, value=[0, 600],
                                                         tooltip={"placement":"bottom", "always_visible":True}))])
                        ]
                )
            ]),
        html.Div(html.Div(children=html.B("Data View"), style={'color': colors['deep color']})),
        html.Div(html.Br()),
        html.Div(
            dbc.Accordion(
                [
                    dbc.AccordionItem(
                        dcc.Graph(figure=fig_acc),
                        title="3-axis Acceleration",
                    ),
                    dbc.AccordionItem(
                        dcc.Graph(figure=fig_bvp),
                        title="BVP",
                    ),
                    dbc.AccordionItem(
                        dcc.Graph(figure=fig_eda),
                        title="EDA",
                    ),
                    dbc.AccordionItem(
                        dcc.Graph(figure=fig_hr),
                        title="Heart Rates",
                    ),
                    dbc.AccordionItem(
                        dcc.Graph(figure=fig_ibi),
                        title="IBI",
                    ),
                    dbc.AccordionItem(
                        dcc.Graph(figure=fig_temp),
                        title="Body Temperature",
                    ),
                    dbc.AccordionItem(
                        dcc.Graph(figure=fig_att_med),
                        title="Attention and Meditation",
                    ),
                    dbc.AccordionItem(
                        dcc.Graph(figure=fig_bw),
                        title="BrainWave",
                    ),
                    dbc.AccordionItem(
                        dcc.Graph(figure=fig_audio),
                        title="Audio",
                    ),
                ],
                always_open=True,
            )
        )

    ]
)


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
