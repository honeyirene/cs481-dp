from dash import html
from dash.development.base_component import Component
from typing import List
from component.qualityControlDistributionComponent import (
    QualityControlDistributionComponent,
)


# QualityControl 페이지의 왼쪽 Distribution 그래프 묶음 (센서 별)
class QualityControlSensorComponent:
    def __getRow(self, info1d: List[str]) -> Component:
        component = QualityControlDistributionComponent()
        children = [component.getFC() for info in info1d]

        return html.Div(
            children,
            style={
                "display": "flex",
                "justify-content": "center",
            },
        )

    def getFC(self, info2d: List[List[str]]) -> Component:
        children = [self.__getRow(info1d) for info1d in info2d]
        return html.Div(children)


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
