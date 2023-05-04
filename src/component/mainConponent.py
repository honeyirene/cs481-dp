from dash import Dash, html
from .subComponent import SubComponent
from .testGraphComponent import TestGraphComponent, TestGraphProps

class MainComponent:
    def register(app: Dash ) -> None:
        sub1: html.Div = SubComponent.getFC()

        testProps: TestGraphProps = TestGraphProps(0)
        test: html.Div = TestGraphComponent.getFC(testProps)

        app.layout = html.Div(className="mainContainer", children=[
            sub1,test,
        ])
        return

# 코드 돌아가는지 테스트용
if __name__ == '__main__':
    print('skip')
