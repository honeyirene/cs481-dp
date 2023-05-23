from dash import html
from dash.development.base_component import Component


# 공용으로 쓸 타이틀 코드. 예쁘게 만드는 건 나중에.
class TitleComponent:
    def getFC(self, title: str, color: str) -> Component:
        return html.Div(
            children=title,
            style={
                "height": "100%",
                "fontSize": "36px",
                "fontWeight": "bold",
                "color": color,
                "display": "flex",
                "alignItems": "center",
                "marginLeft": "36px",
                "marginRight": "36px",
            },
        )


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
