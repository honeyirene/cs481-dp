import dash
from dash import html
import dash_bootstrap_components as dbc
from dash import dcc

dash.register_page(
    __name__,
    name="View",
    path="/view",
    top_nav=True,
    top_nav_order=3,
)

colors = {
    'deep color': '#1091DB',
    'basic color': '#59C3FF',
    'white': '#FFFFFF',
    'black': '#000000',
    'background': '#F6FCFF',
    'darkgray': '#585757',
    'lightgray': '#D9D9D9'
}
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
                            html.Img(src="https://i.ibb.co/ctFP3Sg/1.png"), html.Br(),
                            html.Div(dcc.RangeSlider(0, 20, marks=None, value=[5, 15],
                                                         tooltip={"placement":"bottom", "always_visible":True}))])
                    ]
                )
            ]),
        html.Div(html.Div(children=html.B("Data View"), style={'color': colors['deep color']}))
    ]
)

# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
