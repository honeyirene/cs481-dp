from dash import html
from dash.development.base_component import Component
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Input, Output


class SectionComponent:
    isVideoZoom = True
    changePortionButton = html.Button("change", id="input", n_clicks=0)

    def getFC(
        self,
        leftUpperChildren: Component,
        leftLowerChildren: Component,
        rightChildren: Component,
    ) -> Component:
        leftUpper = html.Div(id="left-upper-panel", children=leftUpperChildren)
        leftLower = html.Div(id="left-lower-panel", children=leftLowerChildren)
        left = html.Div(
            id="left-panel",
            children=[
                leftUpper,
                self.changePortionButton,
                leftLower,
            ],
        )

        middle = html.Div(id="middle-gap", style={"width": "1%"})
        right = html.Div(id="right-panel", children=rightChildren)

        return html.Div(
            children=[
                left,
                middle,
                right,
            ],
            style={"display": "flex"},
        )

    @callback(
        Output("left-panel", "style"),
        Output("right-panel", "style"),
        Input("input", "n_clicks"),
    )
    def changePortion(n_clicks):
        print(n_clicks)
        if (n_clicks) % 2 == 0:
            leftStyle = {
                "width": "35%",
                "border": "1px solid cyan",
            }
            rightStyle = {
                "width": " 65%",
                "border": "1px solid cyan",
            }
        else:
            leftStyle = {
                "width": "50%",
                "border": "1px solid cyan",
            }
            rightStyle = {
                "width": " 50%",
                "border": "1px solid cyan",
            }

        return leftStyle, rightStyle
