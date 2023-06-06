import dash
from component.homeRightComponent import HomeRightComponent
from component.titleComponent import TitleComponent
from component.sectionComponent import SectionComponent
from component.viewIIDComponent import ViewIIDComponent
from component.viewVideoComponent import ViewVideoComponent
from dash import html
from flask import Flask

# from app import app


server = Flask(__name__)

from flask import Flask
from component.viewIIDComponent import ViewIIDComponent

from component.viewVideoComponent import ViewVideoComponent

server = Flask(__name__)

dash.register_page(
    __name__,
    name="Home",
    path="/",
)


title = TitleComponent().getFC("EmoViz", "white")

leftUpper = ViewVideoComponent().getFC()

leftLower = ViewIIDComponent().getFC(
    "Participant 5",
    "gender: male, age: 22." + "\n" + "\n" + "All participants were students at KAIST.",
)

right = HomeRightComponent().getFC()

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
