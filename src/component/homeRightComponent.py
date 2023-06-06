import dash
import plotly.graph_objects as go
from component.viewGraphComponent import ViewGraphComponent
from dash import dcc, html
from dash.dependencies import Input, Output, State, ClientsideFunction
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

        graphComponent = ViewGraphComponent().getFC(data)
        app = dash.get_app()

        app.clientside_callback(
            ClientsideFunction(namespace="clientside", function_name="updateGraphs"),
            [Output("graph" + str(d.id.value), "figure") for d in data],
            Input("time_slider", "value"),
            [State("graph" + str(d.id.value), "figure") for d in data],
        )

        app.clientside_callback(
            """
            function (time, value) {
                const currTime = Math.floor(time ?? 0);
                const result = [value[0], currTime, value[2]];
                return result;
            }
            """,
            Output("time_slider", "value"),
            Input("player", "currentTime"),
            State("time_slider", "value"),
        )

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
            updatemode="drag",
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
