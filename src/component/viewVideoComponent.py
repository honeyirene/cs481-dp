import dash_player as dp
from dash import html
from dash.development.base_component import Component


class ViewVideoComponent:
    def getFC(self) -> Component:
        video = dp.DashPlayer(
            id="player",
            url="https://youtu.be/yB5uNJt4y90",
            controls=True,
            width="100%",
            height="100%",
        )

        return html.Div(
            children=[video],
            style={
                "width": "100%",
                "height": "100%",
            },
        )


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
