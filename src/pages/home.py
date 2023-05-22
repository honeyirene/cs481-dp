#########################################
### <view page>
### mainly managed by Minhyeok Seo.
#########################################

import dash
from dash import html
from component.titleComponent import TitleComponent
from component.sectionComponent import SectionComponent
import dash_bootstrap_components as dbc

from component.viewGraphComponent import ViewGraphComponent
from dataStructure.fakeData import FakeDataFactory

dash.register_page(
    __name__,
    name="Home",
    path="/",
)

title = TitleComponent().getFC("EmoViz", "white")

leftUpper = html.Div(
    [
        dbc.Col(
            [
                html.Div(
                    children=[
                        html.H2("Purpose"),
                        html.Br(),
                        html.H5("Tracking your K-emocon Data with our tool."),
                        html.H5(
                            "We provide simple views and quality controls for catching trend of multi-modal data."
                        ),
                        html.Br(),
                        html.Br(),
                    ],
                )
            ]
        )
    ],
    style={"background-color":"white"}
)

leftLower = (
    html.Div(
        children=[
            html.H2("Purpose"),
            html.Br(),
            html.Ul(
                html.Li(
                    html.A(
                        "K-EmoCon, a multimodal sensor dataset for continuous emotion recognition in naturalistic conversations",
                        href="https://www.nature.com/articles/s41597-020-00630-y",
                    )
                )
            ),
        ],
        style={"background-color":"white"}
    ),
)

factory = FakeDataFactory()
right = ViewGraphComponent().getFC(
    [
        factory.plotData_acc,
        factory.plotData_bvp,
        factory.plotData_eda,
        factory.plotData_hr,
        factory.plotData_ibi,
        factory.plotData_temp,
        factory.plotData_bw,
        factory.plotData_etc,
        factory.plotData_audio,
    ]
)

mainContainer = SectionComponent().getFC(title, leftUpper, leftLower, right)

layout = html.Div(
    children=[
        mainContainer,
    ],
    style={"height": "100vh",
        #"border": "1px solid cyan",
        "background-color": "#f6fcff"},
)

# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
