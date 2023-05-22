from dash import html
from dash.development.base_component import Component


# 공용으로 쓸 타이틀 코드. 예쁘게 만드는 건 나중에.
class TitleComponent:
    def getFC(self, title: str, color: str ) -> Component:
        return html.Div(
            children=title,
            style={
                "height": "3%",
                "font-size": "36px",
                "font-weight": "bold",
                "color": color,
                # "margin-top": "12px",
                "margin-left": "36px",
                "margin-right": "36px",
                # "margin-bottom": "12px",
            },
        )


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
