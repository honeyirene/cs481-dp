import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.development.base_component import Component

from dataStructure.researchDataType import ResearchDataType


class CheckBox:
    def getFC(self) -> Component:
        emotionColumn = dbc.Col(
            [
                html.B("Emotion Annotation"),
                dcc.Checklist(
                    id="emotion-annotation",
                    options=[
                        {
                            "label": "Arousal & Valence (ext)",
                            "value": ResearchDataType.AROUSAL_AND_VALENCE_EXT.value,
                        },
                        {
                            "label": "Stress (ext)",
                            "value": ResearchDataType.STRESS_EXT.value,
                        },
                        {
                            "label": "cBROMP (ext)",
                            "value": ResearchDataType.C_BROMP_EXT.value,
                        },
                        {
                            "label": "lcBROMP (ext)",
                            "value": ResearchDataType.LC_BROMP_EXT.value,
                        },
                        {
                            "label": "Arousal & Valence (pnr)",
                            "value": ResearchDataType.AROUSAL_AND_VALENCE_PNR.value,
                        },
                        {
                            "label": "Stress (pnr)",
                            "value": ResearchDataType.STRESS_PNR.value,
                        },
                        {
                            "label": "cBROMP (pnr)",
                            "value": ResearchDataType.C_BROMP_PNR.value,
                        },
                        {
                            "label": "lcBROMP (pnr)",
                            "value": ResearchDataType.LC_BROMP_PNR.value,
                        },
                        {
                            "label": "Arousal & Valence (self)",
                            "value": ResearchDataType.AROUSAL_AND_VALENCE_SELF.value,
                        },
                        {
                            "label": "Stress (self)",
                            "value": ResearchDataType.STRESS_SELF.value,
                        },
                        {
                            "label": "cBROMP (self)",
                            "value": ResearchDataType.C_BROMP_SELF.value,
                        },
                        {
                            "label": "lcBROMP (self)",
                            "value": ResearchDataType.LC_BROMP_SELF.value,
                        },
                    ],
                    value=[
                        ResearchDataType.AROUSAL_AND_VALENCE_EXT.value,
                        ResearchDataType.STRESS_EXT.value,
                        ResearchDataType.C_BROMP_EXT.value,
                        ResearchDataType.LC_BROMP_EXT.value,
                        ResearchDataType.AROUSAL_AND_VALENCE_PNR.value,
                        ResearchDataType.STRESS_PNR.value,
                        ResearchDataType.C_BROMP_PNR.value,
                        ResearchDataType.LC_BROMP_PNR.value,
                        ResearchDataType.AROUSAL_AND_VALENCE_SELF.value,
                        ResearchDataType.STRESS_SELF.value,
                        ResearchDataType.C_BROMP_SELF.value,
                        ResearchDataType.LC_BROMP_SELF.value,
                    ],
                ),
            ]
        )
        sensorColumn = dbc.Col(
            [
                html.B("Sensor Data"),
                dcc.Checklist(
                    id="sensor-data",
                    options=[
                        {
                            "label": "3 axis acceleration",
                            "value": ResearchDataType.ACC.value,
                        },
                        {
                            "label": "BVP",
                            "value": ResearchDataType.BVP.value,
                        },
                        {
                            "label": "EDA",
                            "value": ResearchDataType.EDA.value,
                        },
                        {
                            "label": "Heart Rate",
                            "value": ResearchDataType.HEARTRATE.value,
                        },
                        {
                            "label": "IBI",
                            "value": ResearchDataType.IBI.value,
                        },
                        {
                            "label": "Temperature",
                            "value": ResearchDataType.TEMPERATURE.value,
                        },
                        {
                            "label": "Brainwave",
                            "value": ResearchDataType.BRAINWAVE.value,
                        },
                        {
                            "label": "Attention & Meditation",
                            "value": ResearchDataType.ATTENTION_AND_MEDITATION.value,
                        },
                    ],
                    value=[
                        ResearchDataType.ACC.value,
                        ResearchDataType.BVP.value,
                        ResearchDataType.EDA.value,
                        ResearchDataType.HEARTRATE.value,
                        ResearchDataType.IBI.value,
                        ResearchDataType.TEMPERATURE.value,
                        ResearchDataType.BRAINWAVE.value,
                        ResearchDataType.ATTENTION_AND_MEDITATION.value,
                    ],
                ),
            ]
        )

        return html.Div(
            [
                html.B("Items to Chart"),
                dbc.Row(
                    [
                        emotionColumn,
                        sensorColumn,
                    ],
                    style={
                        "textAlign": "start",
                    },
                ),
            ]
        )
