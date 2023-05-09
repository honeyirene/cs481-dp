import plotly.graph_objects as go
from dash import html, dcc
from dash.development.base_component import Component


# 공용으로 쓸 타이틀 코드. 예쁘게 만드는 건 나중에.
class QualityControlDistributionComponent:
    datay = [1, 2, 3.1, 3.2, 3.3, 3.7, 3.9, 3.9, 4.1, 4.2, 5, 6.0, 6.1, 7, 8, 9, 10]
    datax = ["x1"] * len(datay)

    def getFC(self) -> Component:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=self.datax, y=self.datay, mode="markers"))
        return dcc.Graph(id="asdf", figure=fig)


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
