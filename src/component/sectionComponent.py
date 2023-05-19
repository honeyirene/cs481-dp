from dash import html
from dash.development.base_component import Component
import dash_bootstrap_components as dbc
from dash import html, callback, Output

class SectionComponent:
    section = html.Div()
    
    def getFC(self, leftChildren, rightChildren) -> Component:
        left =html.Div(id="leftChildren",
            children=leftChildren,
            style={
                "width": "45%",
                "margin-right": "1%"
            }
        )

        right = html.Div(id="rightChildren",
            children=leftChildren,
            style={
                "width": "45%",
            }
        )
        
        middle = html.Div(
            children=[left,right],
            style={
                "display": "flex",
            },
        )

        self.section = middle

        return self.section
