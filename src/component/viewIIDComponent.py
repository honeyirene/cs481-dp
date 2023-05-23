from dash import html
from dash.development.base_component import Component
from component.InfoModal import InfoModal
import dash_bootstrap_components as dbc

infoModal = InfoModal().getFC()


# QualityControl 페이지의 왼쪽 Distribution 그래프 하나.
class ViewIIDComponent:
    def getFC(self, IID: str, description: str) -> Component:
        return html.Div(
            children=[
                html.Div(IID,
                    style={
                        "height": "3%",
                        "font-size": "24px",
                        # "margin-top": "12px",
                        "margin-left": "12px",
                        "margin-right": "12px",
                        # "margin-bottom": "12px",
                    }
                ),
                html.Div(description,
                         style={
                             "font-size": "20px",
                             "margin-left": "12px",
                             "margin-right": "12px"

                         }
                        ),
                html.Br(),
                html.Br(),
                html.Div(infoModal,
                         style={'textAlign':'center'})
            ]
        )




# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
