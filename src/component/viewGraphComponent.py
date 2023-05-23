from typing import List
from dash.development.base_component import Component
from component.draggableList import DraggableList
from component.viewSubGraphTrace import ViewSubGraphTrace
from models.graphDataModel import GraphPlotDataModel


# QualityControl 페이지의 왼쪽 Distribution 그래프 하나.
class ViewGraphComponent:
    def getFC(self, plotDatas: List[GraphPlotDataModel]) -> Component:
        graphs = []

        for plotData in plotDatas:
            graph = ViewSubGraphTrace().getFC(plotData)
            graphs.append(graph)

        return DraggableList().getFC(graphs)


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
