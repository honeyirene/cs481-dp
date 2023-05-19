from dash import html
from dash.development.base_component import Component
import dash_bootstrap_components as dbc
from dash import html, callback, Output

class SectionComponent:
    section = html.Div()
    isVideoZoom = True
    changePortionButton = html.Button('change', id = 'input')
    def getFC(self, leftChildren, rightChildren) -> Component:
        left =dbc.Card(id="leftChildren",
            children=leftChildren,
            style={
                "width": "45%",
                "margin-right": "1%"
            }
        )

        right = dbc.Card(id="rightChildren",
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

#    @app.callback(input())
#    def changePortion():