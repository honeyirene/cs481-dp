from dash import html
from dash.development.base_component import Component
from dash import dcc


class ViewVideoComponent:
    def getFC(self, src=str, filename=str) -> Component:
        return html.Div(
            children=[
                html.Video(
                    src="/" + src + "/" + filename,
                    controls=True,
                    # autoPlay=True,
                    style={"width": "100%", "height": "100%"},
                ),
            ]
        )


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
