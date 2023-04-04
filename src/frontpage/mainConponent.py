from dash import Dash, html
from frontpage.subComponent import SubComponent

class MainComponent:
    def register(app: Dash ) -> None:
        sub1: html.Div = SubComponent.getFC()

        app.layout = html.Div(className="mainContainer", children=[
            sub1,
        ])
        return

# 코드 돌아가는지 테스트용
if __name__ == '__main__':
    print('skip')
