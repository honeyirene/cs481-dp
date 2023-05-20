from dash import html
from dash.development.base_component import Component
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Input, Output


class SectionComponent:
    isVideoZoom = True
    changePortionButton = html.Button("change", id="input", n_clicks=0)

    def getFC(self, leftChildren, rightChildren) -> Component:
        left = html.Div(
            id="left-panel",
            children=leftChildren,
            style={
                "width": "45%",
                "margin-right": "1%",
                "border": "1px solid cyan",
            },
        )

        middle = html.Div(id="middle-gap", style={"width": "1%"})

        right = html.Div(
            id="right-panel",
            children=rightChildren,
            style={
                "width": "45%",
                "border": "1px solid cyan",
            },
        )

        return html.Div(
            [
                html.Div(
                    children=[
                        left,
                        middle,
                        right,
                    ],
                    style={
                        "display": "flex",
                    },
                ),
                self.changePortionButton,
            ]
        )

    @callback(
        Output("left-panel", "style"),
        Output("right-panel", "style"),
        Input("input", "n_clicks"),
    )
    def changePortion(n_clicks):
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
