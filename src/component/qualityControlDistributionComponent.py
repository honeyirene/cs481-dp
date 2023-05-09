import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp
import plotly.figure_factory as ff
from dash import html, dcc
from dash.development.base_component import Component
from plotly.basedatatypes import BaseTraceType


# 공용으로 쓸 타이틀 코드. 예쁘게 만드는 건 나중에.
class QualityControlDistributionComponent:
    datay = [1, 2, 3.1, 3.2, 3.3, 3.7, 3.9, 3.9, 4.1, 4.2, 5, 6.0, 6.1, 7, 8, 9, 10]
    datax = ["x1"] * len(datay)

    # px.strip 코드 뜯어보니 go.Box에서 박스를 투명하게 바꾸고 있....
    def __getStrip(self) -> BaseTraceType:
        return go.Box(
            x=self.datax,
            y=self.datay,
            boxpoints="all",
            pointpos=0,
            hoveron="points",
            fillcolor="rgba(255,255,255,0)",
            line={"color": "rgba(255,255,255,0)"},
            marker=dict(color="rgba(255,0,0,0.5)"),
            x0=" ",
            y0=" ",
        )

    def __getViolin(self) -> BaseTraceType:
        return go.Violin(
            x=self.datax,
            y=self.datay,
            side="positive",
            line=dict(color="rgba(0,0,0,0.5)"),
            fillcolor="rgba(0,0,0,0.2)",
        )

    def getFC(self) -> Component:
        fig = sp.make_subplots(
            rows=1,
            cols=2,
            horizontal_spacing=0,
            subplot_titles=("Scatter", "Distribution"),
        )
        fig.add_trace(
            self.__getStrip(),
            row=1,
            col=1,
        )
        fig.add_trace(
            self.__getViolin(),
            row=1,
            col=2,
        )
        fig.update_layout(
            title_text="Sensor A",
            title_x=0.5,
            height=400,
            width=350,
            margin=dict(l=30, r=30, b=0, t=80),
            showlegend=False,
        )
        fig.update_xaxes(visible=False)
        fig.update_yaxes(showgrid=False, row=1, col=1)
        fig.update_yaxes(visible=False, row=1, col=2)
        return dcc.Graph(id="asdf", figure=fig, style=dict())


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
