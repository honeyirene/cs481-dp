from dash import html
from dash.development.base_component import Component
import dash_bootstrap_components as dbc
from dash import dcc, html, callback, Input, Output

class SectionComponent:
    section = html.Div()
    isVideoZoom = True
    changePortionButton = html.Button('change', id = 'input', n_clicks=0)
    def getFC(self, leftChildren, rightChildren) -> Component:
        left =html.Div(id="leftChildren",
            children=leftChildren,
            style={
                "width": "45%",
                "margin-right": "1%"
            }
        )

        right = html.Div(id="rightChildren",
            children=rightChildren,
            style={
                "width": "45%",
            }
        )
        
        middle = html.Div([
            html.Div(
                children=[left,right],
                style={
                    "display": "flex",
                },
            ),
            self.changePortionButton,
        ])

        self.section = middle

        return self.section

    @callback(
        Output("leftChildren", "style"),
        Output("rightChildren", "style"),
        Input("input", 'n_clicks'))
    def changePortion(n_clicks):
        if((n_clicks) % 2 ==0):
            leftStyle = {"width" : "35%", "margin-right": "1%"}
            rightStyle = {"width" : " 60%"}
        else:
            leftStyle = {"width" : "45%", "margin-right": "1%"}
            rightStyle = {"width" : " 45%"}
        
        return leftStyle, rightStyle