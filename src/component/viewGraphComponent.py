import plotly.graph_objects as go
from component.draggableList import DraggableList
from component.viewSubGraphTrace import ViewSubGraphTrace
from dash.development.base_component import Component
from models.graphDataModel import GraphPlotDataModel
from typing import List, Tuple


# QualityControl 페이지의 왼쪽 Distribution 그래프 하나.
class ViewGraphComponent:
    def getFC(
        self, plotDatas: List[GraphPlotDataModel]
    ) -> Tuple[List[go.Figure], Component]:
        figs = []
        graphs = []

        for plotData in plotDatas:
            fig, graph = ViewSubGraphTrace().getFigAndFC(plotData)
            figs.append(fig)
            graphs.append(graph)

        return figs, DraggableList().getFC(graphs)


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
