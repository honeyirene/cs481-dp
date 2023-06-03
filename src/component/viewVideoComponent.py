import dash
import dash_player as dp
from dash import html
from dash.dependencies import Input, Output
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

        app = dash.get_app()

        @app.callback(
            [
                # 여기에 다른 파일에 있는 element의 id를 그대로 써서 연결.
                Output("player", "currentTime"),
            ],
            [
                Input("player", "currentTime"),
            ],
        )
        def update(currentTime):
            # print(type(currentTime))
            # print(currentTime)
            return [currentTime]

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
