from dash import html
from dash.development.base_component import Component
from dash import html, callback, Input, Output


class SectionComponent:
    def __upperBar(self) -> Component:
        upperLeft = html.Div(id="upper-left-empty", style={"width": "95%"})
        changePortionButton = html.Div(html.Button("change", id="input", n_clicks=0))
        return html.Div([upperLeft, changePortionButton], style={"display": "flex"})

    def __mainContainer(
        self,
        leftUpperChildren: Component,
        leftLowerChildren: Component,
        rightChildren: Component,
    ) -> Component:
        leftUpper = html.Div(id="left-upper-panel", children=leftUpperChildren)
        leftMiddle = html.Div(id="left-middle-gap", style={"height": "15px"})
        leftLower = html.Div(id="left-lower-panel", children=leftLowerChildren)
        left = html.Div(
            id="left-panel",
            children=[
                leftUpper,
                leftMiddle,
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

    def getFC(
        self,
        leftUpperChildren: Component,
        leftLowerChildren: Component,
        rightChildren: Component,
    ) -> Component:
        return html.Div(
            children=[
                self.__upperBar(),
                self.__mainContainer(
                    leftUpperChildren,
                    leftLowerChildren,
                    rightChildren,
                ),
            ]
        )

    @callback(
        Output("left-panel", "style"),
        Output("left-upper-panel", "style"),
        Output("left-lower-panel", "style"),
        Output("right-panel", "style"),
        Input("input", "n_clicks"),
    )
    def changePortion(n_clicks):
        print(n_clicks)
        if (n_clicks) % 2 == 0:
            leftStyle = {
                "width": "35%",
            }
            rightStyle = {
                "width": "64%",
                "border": "1px solid cyan",
            }
            leftUpperStyle = {
                "height": "300px",
                "border": "1px solid cyan",
            }
            leftLowerStyle = {
                "border": "1px solid cyan",
            }
        else:
            leftStyle = {
                "width": "49.5%",
            }
            rightStyle = {
                "width": "49.5%",
                "border": "1px solid cyan",
            }
            leftUpperStyle = {
                "height": "500px",
                "border": "1px solid cyan",
            }
            leftLowerStyle = {
                "border": "1px solid cyan",
            }

        return leftStyle, leftUpperStyle, leftLowerStyle, rightStyle
