import plotly.graph_objects as go
from plotly.basedatatypes import BaseTraceType
from models.graphDataModel import GraphPlotDataModel


# QualityControl 페이지의 왼쪽 Distribution 그래프 하나.
class ViewSubGraphTrace:
    def __addTrace(self, trace: BaseTraceType):
        self.fig.add_trace(trace)

    def __updateLayout(self, title: str):
        self.fig.update_layout(
            yaxis_title=title,
            margin=dict(t=10, b=10),
            height=200,
            legend=dict(orientation="h"),
            showlegend=True,
        )
        # self.fig["layout"][f"yaxis{self.row}"]["title"] = title

    def getFig(self, plotData: GraphPlotDataModel) -> go.Figure:
        self.fig = go.Figure()

        for traceData in plotData.traces:
            self.__addTrace(
                go.Scatter(
                    y=traceData.y,
                    name=traceData.name,
                    mode="lines",
                )
            )

        self.__updateLayout(plotData.title)

        return self.fig


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
