import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import plotly.figure_factory as ff
from dash import html, dcc
from dash.development.base_component import Component


# 공용으로 쓸 타이틀 코드. 예쁘게 만드는 건 나중에.
class QualityControlDistributionComponent:
    datay = [1, 2, 3.1, 3.2, 3.3, 3.7, 3.9, 3.9, 4.1, 4.2, 5, 6.0, 6.1, 7, 8, 9, 10]
    datax = ["x1"] * len(datay)

    def getFC(self) -> Component:
        fig = sp.make_subplots(rows=1, cols=2, horizontal_spacing=0)
        fig.add_trace(
            go.Box(
                x=self.datax,
                y=self.datay,
                boxpoints="all",
                pointpos=0,
                hoveron="points",
                fillcolor="rgba(255,255,255,0)",
                line={"color": "rgba(255,255,255,0)"},
                marker=dict(color="rgb(0,0,0)"),
                x0=" ",
                y0=" ",
            ),
            row=1,
            col=1,
        )
        fig.add_trace(
            go.Violin(x=self.datax, y=self.datay, side="positive"),
            row=1,
            col=2,
        )
        fig.update_yaxes(showgrid=False, row=1, col=1)
        fig.update_yaxes(visible=False, row=1, col=2)
        return dcc.Graph(id="asdf", figure=fig)


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
