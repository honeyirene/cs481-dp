import dash
import dash_player as dp
from dash import html
from dash.development.base_component import Component


class ViewVideoComponent:
    def getFC(self) -> Component:
        video = dp.DashPlayer(
            id="player",
            url="https://www.youtube.com/watch?v=ZgbEBzqt_lY?feature=share",
            controls=True,
            width="100%",
            height="100%",
        )

        dash.get_app()

        return html.Div(children=[video])


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
