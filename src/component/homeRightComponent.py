import plotly.graph_objects as go
from component.viewGraphComponent import ViewGraphComponent
from dash import dcc, html
from dataStructure.researchData import ResearchDataFactory


class HomeRightComponent:
    def getFC(self) -> go.Figure:
        factory = ResearchDataFactory()
        graphComponent = ViewGraphComponent().getFC(
            [
                factory.plotData_emo_ann_ext,
                factory.plotData_emo_ann_pnr,
                factory.plotData_emo_ann_self,
                factory.plotData_acc,
                factory.plotData_bvp,
                factory.plotData_eda,
                factory.plotData_hr,
                factory.plotData_ibi,
                factory.plotData_temp,
                factory.plotData_bw,
                factory.plotData_etc,
                # factory.plotData_audio,
            ]
        )
        graphContainer = html.Div(
            graphComponent, style={"height": "94%", "overflow": "auto"}
        )

        timeRangeSlider = dcc.RangeSlider(
            id="time_slider",
            min=0,
            max=600,
            marks=None,
            value=[0, 600],
            tooltip={
                "placement": "bottom",
                "always_visible": True,
            },
        )
        timelineContainer = html.Div(
            timeRangeSlider,
            style={
                "height": "6%",
                "margin": "auto",
                "padding": "30px",
            },
        )

        return html.Div(
            [graphContainer, timelineContainer],
            style={"height": "100%", "overflow": "hidden"},
        )


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
