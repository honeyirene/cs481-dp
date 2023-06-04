import dash_daq as daq
from dash import html, callback, Input, Output
from dash.development.base_component import Component


class SectionComponent:
    def __upperBar(self, title) -> Component:
        upperLeft = html.Div(
            id="upper-left-empty",
            children=[
                title,
            ],
            style={"width": "90%"},
        )
        changePortionButton = html.Div(
            daq.ToggleSwitch(
                id="input",
                label="Extend Video",
                labelPosition="bottom",
                value=False,
            ),
            style={
                "display": "flex",
                "alignItems": "center",
            },
        )
        return html.Div(
            children=[
                upperLeft,
                changePortionButton,
            ],
            style={"display": "flex", "height": "8%", "background-color": "#59c3ff"},
        )

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
            style={
                "height": "91%",
                "overflow": "hidden",
                "display": "flex",
            },
        )

    def getFC(
        self,
        title: Component,
        leftUpperChildren: Component,
        leftLowerChildren: Component,
        rightChildren: Component,
    ) -> Component:
        return html.Div(
            children=[
                self.__upperBar(title),
                html.Div(style={"height": "1%"}),
                self.__mainContainer(
                    leftUpperChildren,
                    leftLowerChildren,
                    rightChildren,
                ),
            ],
            style={"height": "100%", "overflow": "hidden"},
        )

    @callback(
        Output("left-panel", "style"),
        Output("left-upper-panel", "style"),
        Output("left-lower-panel", "style"),
        Output("right-panel", "style"),
        Input("input", "value"),
    )
    def changePortion(value):
        print(value)
        if not value:
            leftStyle = {
                "width": "25%",
            }
            rightStyle = {
                "width": "74%",
                "height": "100%",
            }
            leftUpperStyle = {
                "aspectRatio": "16 / 9",
                "backgroundColor": "white",
            }
            leftLowerStyle = {
                "backgroundColor": "white",
            }
        else:
            leftStyle = {
                "width": "49.5%",
            }
            rightStyle = {
                "width": "49.5%",
                "height": "100%",
            }
            leftUpperStyle = {
                "aspectRatio": "16 / 9",
                "backgroundColor": "white",
            }
            leftLowerStyle = {
                "backgroundColor": "white",
            }

        return leftStyle, leftUpperStyle, leftLowerStyle, rightStyle
