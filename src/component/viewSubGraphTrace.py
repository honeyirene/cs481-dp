import plotly.graph_objects as go
from dash import dcc
from plotly.basedatatypes import BaseTraceType
from models.graphDataModel import GraphPlotDataModel


# QualityControl 페이지의 왼쪽 Distribution 그래프 하나.
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
            xaxis=dict(rangeslider=dict(visible=True), type="date"),
        )

    def getFC(self, plotData: GraphPlotDataModel) -> go.Figure:
        fig = go.Figure()

        for traceData in plotData.traces:
            gobj = go.Scatter(y=traceData.y, name=traceData.name, mode="lines")
            self.__addTrace(fig, gobj)

        self.__updateLayout(fig, plotData.title)

        graph = dcc.Graph(id="graph" + str(plotData.title), figure=fig, style=dict())

        return graph


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
