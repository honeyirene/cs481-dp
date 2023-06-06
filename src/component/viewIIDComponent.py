from dash import html
from dash.development.base_component import Component
from component.checkBox import CheckBox


# QualityControl 페이지의 왼쪽 Distribution 그래프 하나.
class ViewIIDComponent:
    def getFC(self, IID: str, description: str) -> Component:
        checkBox = CheckBox().getFC()

        return html.Div(
            children=[
                html.Div(
                    IID,
                    style={
                        "height": "3%",
                        "fontSize": "24px",
                        # "margin-top": "12px",
                        "marginLeft": "12px",
                        "marginRight": "12px",
                        # "margin-bottom": "12px",
                    },
                ),
                html.Div(
                    description,
                    style={
                        "fontSize": "20px",
                        "marginLeft": "12px",
                        "marginRight": "12px",
                    },
                ),
                html.Br(),
                html.Br(),
                html.Div(checkBox, style={"textAlign": "center"}),
            ]
        )


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
