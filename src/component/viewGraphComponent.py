import dash
from component.draggableList import DraggableList
from component.viewSubGraphTrace import ViewSubGraphTrace
from dash import Input, Output, State
from dash.development.base_component import Component
from models.graphDataModel import GraphPlotDataModel
from typing import List


# QualityControl 페이지의 왼쪽 Distribution 그래프 하나.
class ViewGraphComponent:
    def getFC(self, plotDatas: List[GraphPlotDataModel]) -> Component:
        figs = []
        graphs = []

        app = dash.get_app()

        app.clientside_callback(
            """
            function onoff(emo_value, sen_value, ...ids){
                value = [...emo_value, ...sen_value];
                return ids
                    .map(x => parseInt(x.split('-')[1], 10))
                    .map(x => value.includes(x));
            }
            """,
            [
                Output("collapse-" + str(plotData.id.value), "is_open")
                for plotData in plotDatas
            ],
            Input("emotion-annotation", "value"),
            Input("sensor-data", "value"),
            [
                State("collapse-" + str(plotData.id.value), "id")
                for plotData in plotDatas
            ],
        )

        for plotData in plotDatas:
            fig, graph = ViewSubGraphTrace().getFigAndFC(plotData)
            figs.append(fig)
            graphs.append(graph)

        return DraggableList().getFC(graphs)


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
