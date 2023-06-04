import dash
from dash import html, ClientsideFunction, Input, Output
from dash.development.base_component import Component


# ref: https://probhakar-95.medium.com/plotly-dash-draggable-component-7662318551a4
class DraggableList:
    def getFC(self, children) -> Component:
        dash.get_app().clientside_callback(
            ClientsideFunction(namespace="clientside", function_name="make_draggable"),
            Output("drag-container", "data-drag"),
            Input("drag-container", "id"),
        )

        return html.Div(
            [
                html.Div(children, id="drag-container", style={"width": "100%"}),
                html.Div(style={"width": "20px"}),
            ],
            style={
                "display": "flex",
            },
        )
