import datetime
import dash
import pandas as pd
import plotly.graph_objects as go
from component.viewGraphComponent import ViewGraphComponent
from dash import dcc, html
from dash.dependencies import Input, Output
from dataStructure.researchData import ResearchDataFactory


class HomeRightComponent:
    def getFC(self) -> go.Figure:
        factory = ResearchDataFactory()
        data = [
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

        figs, graphComponent = ViewGraphComponent().getFC(data)
        app = dash.get_app()

        @app.callback(
            [Output("graph" + d.title, "figure") for d in data],
            [Input("time_slider", "value")],
        )
        def update_plots(active_range):
            for fig in figs:
                fig.update_layout(xaxis=dict(range=active_range))
            return figs

        graphContainer = html.Div(
            graphComponent, style={"height": "94%", "overflow": "auto"}
        )

        timeRangeSlider = dcc.RangeSlider(
            id="time_slider",
            min=factory.plotData_acc.df["timestamp"][0],
            max=factory.plotData_acc.df["timestamp"].iat[-1],
            marks=None,
            value=[
                factory.plotData_acc.df["timestamp"][0],
                factory.plotData_acc.df["timestamp"].iat[-1],
            ],
            tooltip={
                "placement": "bottom",
                "always_visible": True,
            },
            # display_format="mm:ss",
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
