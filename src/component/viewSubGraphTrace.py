import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.development.base_component import Component
from plotly.basedatatypes import BaseTraceType
from models.graphDataModel import GraphPlotDataModel
from component.valueModal import ValueModal
from typing import Tuple


class ViewSubGraphTrace:
    def __addTrace(self, fig: go.Figure, trace: BaseTraceType):
        fig.add_trace(trace)

    def __updateLayout(self, fig: go.Figure, title: str):
        fig.update_layout(
            yaxis_title=title,
            margin=dict(t=10, b=10),
            height=200,
            legend=dict(orientation="h"),
            showlegend=True,
            dragmode="turntable",
            shapes=[
                dict(
                    type="line",
                    xref="paper",
                    yref="paper",
                    x0=0,
                    x1=0,
                    y0=0,
                    y1=1,
                    line_width=1,
                ),
            ],
        )

    def getFigAndFC(self, plotData: GraphPlotDataModel) -> Tuple[go.Figure, Component]:
        basetime = 1548206261000
        fig = go.Figure()

        for traceData in plotData.traces:
            gobj = go.Scatter(
                x=plotData.df[traceData.xname].apply(lambda x: (x - basetime) / 1000),
                y=plotData.df[traceData.yname],
                name=traceData.displayName,
                mode="lines",
            )
            self.__addTrace(fig, gobj)

        self.__updateLayout(fig, plotData.title)

        info = ValueModal().getFC(plotData.title)
        graph = dbc.Collapse(
            html.Div(
                [
                    dcc.Graph(
                        id="graph" + str(plotData.id.value),
                        figure=fig,
                        style={"width": "100%"},
                    ),
                    info,
                ],
                style={
                    "width": "100%",
                    "display": "flex",
                    "alignItem": "center",
                },
            ),
            id="collapse-" + str(plotData.id.value),
            is_open=False,
        )

        return fig, graph


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
