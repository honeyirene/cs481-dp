import plotly.subplots as sp
from typing import List
from dash import dcc
from dash.development.base_component import Component
from component.viewSubGraphTrace import ViewSubGraphTrace
from models.graphDataModel import GraphPlotDataModel


# QualityControl 페이지의 왼쪽 Distribution 그래프 하나.
class ViewGraphComponent:
    def getFC(self, plotDatas: List[GraphPlotDataModel]) -> Component:
        # https://stackoverflow.com/questions/69306288/how-to-limit-update-layout-margins-only-to-one-subplot-in-plotly-dash
        # 크기 조절 관련된건 이거 봐야할듯?
        self.fig = sp.make_subplots(
            rows=len(plotDatas),
            cols=1,
        )

        for idx, plotData in enumerate(plotDatas):
            trace = ViewSubGraphTrace(self.fig, row=idx + 1, col=1)
            trace.update(plotData)

        self.fig["layout"]["legend_tracegroupgap"] = 100
        # 그래프 크기 조절하면서 legend 간격을 조절해야 할텐데, 사이에 아무것도 없는 그룹 끼워넣기...?

        return dcc.Graph(id="asdf", figure=self.fig, style=dict())


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
