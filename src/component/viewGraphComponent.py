from typing import List
from dash import dcc, html
from dash.development.base_component import Component
from component.viewSubGraphTrace import ViewSubGraphTrace
from models.graphDataModel import GraphPlotDataModel


# QualityControl 페이지의 왼쪽 Distribution 그래프 하나.
class ViewGraphComponent:
    def getFC(self, plotDatas: List[GraphPlotDataModel]) -> Component:
        graphs = []

        for idx, plotData in enumerate(plotDatas):
            fig = ViewSubGraphTrace().getFig(plotData)
            graph = dcc.Graph(id="graph" + str(idx), figure=fig, style=dict())
            graphs.append(graph)

        return html.Div(children=graphs)


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
