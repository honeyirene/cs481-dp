import plotly.graph_objects as go
from plotly.basedatatypes import BaseTraceType
from models.graphDataModel import GraphPlotDataModel


# QualityControl 페이지의 왼쪽 Distribution 그래프 하나.
class ViewSubGraphTrace:
    def __init__(self, fig: go.Figure, row: int, col: int):
        self.fig = fig
        self.row = row
        self.col = col

    def __addTrace(self, trace: BaseTraceType):
        self.fig.add_trace(trace, row=self.row, col=self.col)

    def __updateLayout(self, title: str):
        self.fig["layout"][f"yaxis{self.row}"]["title"] = title

    def update(self, plotData: GraphPlotDataModel) -> None:
        for traceData in plotData.traces:
            self.__addTrace(
                go.Scatter(y=traceData.y, name=traceData.name, mode="lines")
            )
        self.__updateLayout(plotData.title)


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
