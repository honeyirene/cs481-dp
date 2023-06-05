import math
import dash
import plotly.graph_objects as go
from component.viewGraphComponent import ViewGraphComponent
from dash import dcc, html
from dash.dependencies import Input, Output
from dataStructure.researchData import ResearchDataFactory


class HomeRightComponent:
    def getFC(self) -> go.Figure:
        factory = ResearchDataFactory()
        data = [
            factory.plotData_emo_ann_ext_av,
            factory.plotData_emo_ann_ext_stress,
            factory.plotData_emo_ann_ext_cBROMP,
            factory.plotData_emo_ann_ext_lcBROMP,
            factory.plotData_emo_ann_pnr_av,
            factory.plotData_emo_ann_pnr_stress,
            factory.plotData_emo_ann_pnr_cBROMP,
            factory.plotData_emo_ann_pnr_lcBROMP,
            factory.plotData_emo_ann_self_av,
            factory.plotData_emo_ann_self_stress,
            factory.plotData_emo_ann_self_cBROMP,
            factory.plotData_emo_ann_self_lcBROMP,
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

        figs, graphComponent = ViewGraphComponent().getFC(data)
        app = dash.get_app()

        @app.callback(
            [Output("graph" + d.title, "figure") for d in data],
            Input("time_slider", "value"),
        )
        def update_plots(values):
            rangeMinSec = values[0]
            currentSec = values[1]
            rangeMaxSec = values[2]

            basetime = 1548206261000
            rangeMin = basetime + rangeMinSec * 1000
            rangeMax = basetime + rangeMaxSec * 1000
            for fig in figs:
                fig.update_layout(xaxis=dict(range=[rangeMin, rangeMax]))

            rangeSize = rangeMaxSec - rangeMinSec
            currentX = (currentSec - rangeMinSec) / rangeSize
            for fig in figs:
                fig.update_layout(
                    shapes=[
                        dict(
                            type="line",
                            xref="paper",
                            # TODO 여기 time 에 맞게 수정 필요
                            yref="paper",
                            # 비디오의 현재 백분율 이후 이부분 수정 필요
                            x0=currentX,
                            x1=currentX,
                            y0=0,
                            y1=1,
                            line_width=1,
                        ),
                    ]
                )
            return figs

        @app.callback(
            [Output("time_slider", "value")],
            Input("player", "currentTime"),
            Input("time_slider", "value"),
        )
        def sync(time, value):
            currTime = math.floor(0 if type(time) == type(None) else time)
            result = [value[0], currTime, value[2]]
            return [result]

        graphContainer = html.Div(
            graphComponent, style={"height": "85%", "overflow": "auto"}
        )

        timeRangeSlider = dcc.RangeSlider(
            id="time_slider",
            min=0,
            max=630,
            marks={
                0: {"label": "00:00"},
                30: {"label": "00:30"},
                60: {"label": "01:00"},
                90: {"label": "01:30"},
                120: {"label": "02:00"},
                150: {"label": "02:30"},
                180: {"label": "03:00"},
                210: {"label": "03:30"},
                240: {"label": "04:00"},
                270: {"label": "04:30"},
                300: {"label": "05:00"},
                330: {"label": "05:30"},
                360: {"label": "06:00"},
                390: {"label": "06:30"},
                420: {"label": "07:00"},
                450: {"label": "07:30"},
                480: {"label": "08:00"},
                510: {"label": "08:30"},
                540: {"label": "09:00"},
                570: {"label": "09:30"},
                600: {"label": "10:00"},
                630: {"label": "10:30"},
            },
            value=[0, 0, 630],
            tooltip={
                "placement": "bottom",
                "always_visible": False,
            },
            allowCross=False,
        )

        timelineContainer = html.Div(
            timeRangeSlider,
            style={
                "height": "15%",
                "margin": "auto",
                "padding": "30px",
            },
        )

        return html.Div(
            [timelineContainer, graphContainer],
            style={"height": "100%", "overflow": "hidden"},
        )


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
