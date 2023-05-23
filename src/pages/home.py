#########################################
### <view page>
### mainly managed by Minhyeok Seo.
#########################################

import dash
from dash import dcc, html
from component.titleComponent import TitleComponent
from component.sectionComponent import SectionComponent
import dash_bootstrap_components as dbc

from flask import Flask, Response
from component.viewIIDComponent import ViewIIDComponent

from component.viewVideoComponent import ViewVideoComponent

server = Flask(__name__)

from component.viewGraphComponent import ViewGraphComponent
from dataStructure.fakeData import FakeDataFactory

dash.register_page(
    __name__,
    name="Home",
    path="/",
)

title = TitleComponent().getFC("EmoViz", "white")

leftUpper = ViewVideoComponent().getFC("static", "p4_688.mp4")

leftLower = ViewIIDComponent().getFC(
    "Participant 4",
    "gender: male, age: 25." + "\n" + "\n" + "All participants were students at KAIST.",
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
    style={
        "height": "100vh",
        # "border": "1px solid cyan",
        "background-color": "#f6fcff",
    },
)

# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
