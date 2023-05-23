#########################################
### <view page>
### mainly managed by Minhyeok Seo.
#########################################

import dash
import os
from dash import html
from component.nextButtonComponent import nextButtonComponent
from component.titleComponent import TitleComponent
from component.sectionComponent import SectionComponent
from component.viewIIDComponent import ViewIIDComponent
from component.viewVideoComponent import ViewVideoComponent
import dash_bootstrap_components as dbc
from dash import dcc

# from app import app

from flask import Flask, Response

server = Flask(__name__)

from flask import Flask, Response
from component.viewIIDComponent import ViewIIDComponent

from component.viewVideoComponent import ViewVideoComponent

server = Flask(__name__)

from component.viewGraphComponent import ViewGraphComponent
from dataStructure.researchData import ResearchDataFactory

dash.register_page(
    __name__,
    name="Home",
    path="/",
)


title = TitleComponent().getFC("EmoViz", "white")

leftUpper = ViewVideoComponent().getFC("assets", "p4_688.mp4")

leftLower = ViewIIDComponent().getFC(
    "Participant 4",
    "gender: male, age: 25." + "\n" + "\n" + "All participants were students at KAIST.",
)


factory = ResearchDataFactory()
right = ViewGraphComponent().getFC(
    [
        factory.plotData_emo_ann_ext,
        factory.plotData_emo_ann_pnr,
        factory.plotData_emo_ann_self,
        factory.plotData_acc,
        factory.plotData_bvp,
        factory.plotData_eda,
        factory.plotData_hr,
        factory.plotData_ibi,
        factory.plotData_temp,
        factory.plotData_bw,
        factory.plotData_etc,
        # factory.plotData_audio,
    ]
)

mainContainer = SectionComponent().getFC(title, leftUpper, leftLower, right)

layout = html.Div(
    children=[
        mainContainer,
    ],
    style={"height": "100vh"},
)

# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
