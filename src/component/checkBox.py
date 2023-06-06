from dash import html, callback, Input, Output, State
from dash.development.base_component import Component
import dash_bootstrap_components as dbc
from dash import dcc


class CheckBox:
    def getFC(self) -> Component:
        return html.Div(
            [
                html.B("Items to Chart"),
                dcc.Checklist(
                    id="all-or-none",
                    options=[{"lable": "Select All", "value": "All"}],
                    value=["All"],
                    labelStyle={"display": "block"},
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.Div(
                                [
                                    html.B("Emotion Annotation"),
                                    dcc.Checklist(
                                        id="emotion annotation",
                                        options=[
                                            {
                                                "label": "Arousal & Valence (ext)",
                                                "value": "a&v(e)",
                                            },
                                            {
                                                "label": "Stress (ext)",
                                                "value": "stress(e)",
                                            },
                                            {
                                                "label": "cBROMP (ext)",
                                                "value": "cBROMP(e)",
                                            },
                                            {
                                                "label": "lcBROMP (ext)",
                                                "value": "lcBROMP(e)",
                                            },
                                            {
                                                "label": "Arousal & Valence (pnr)",
                                                "value": "a&v(p)",
                                            },
                                            {
                                                "label": "Stress (pnr)",
                                                "value": "stress(p)",
                                            },
                                            {
                                                "label": "cBROMP (pnr)",
                                                "value": "cBROMP(p)",
                                            },
                                            {
                                                "label": "lcBROMP (pnr)",
                                                "value": "lcBROMP(p)",
                                            },
                                            {
                                                "label": "Arousal & Valence (self)",
                                                "value": "a&v(s)",
                                            },
                                            {
                                                "label": "Stress (self)",
                                                "value": "stress(s)",
                                            },
                                            {
                                                "label": "cBROMP (self)",
                                                "value": "cBROMP(s)",
                                            },
                                            {
                                                "label": "lcBROMP (self)",
                                                "value": "lcBROMP(s)",
                                            },
                                        ],
                                        value=[
                                            "a&v(e)",
                                            "stress(e)",
                                            "cBROMP(e)",
                                            "lcBROMP(e)",
                                            "a&v(p)",
                                            "stress(p)",
                                            "cBROMP(p)",
                                            "lcBROMP(p)",
                                            "a&v(s)",
                                            "stress(s)",
                                            "cBROMP(s)",
                                            "lcBROMP(s)",
                                        ],
                                    ),
                                ]
                            ),
                        ),
                        dbc.Col(
                            html.Div(
                                [
                                    html.B("Sensor Data"),
                                    dcc.Checklist(
                                        id="sensor data",
                                        options=[
                                            {
                                                "label": "3 axis acceleration",
                                                "value": "acc",
                                            },
                                            {"label": "BVP", "value": "BVP"},
                                            {"label": "EDA", "value": "EDA"},
                                            {
                                                "label": "Heart Rate",
                                                "value": "HR",
                                            },
                                            {
                                                "label": "Temperature",
                                                "value": "T",
                                            },
                                            {
                                                "label": "Brainwave",
                                                "value": "Bw",
                                            },
                                            {
                                                "label": "Attention & Meditation",
                                                "value": "a&m",
                                            },
                                        ],
                                        value=[
                                            "acc",
                                            "BVP",
                                            "EDA",
                                            "HR",
                                            "T",
                                            "Bw",
                                            "a&m",
                                        ],
                                    ),
                                ]
                            ),
                        ),
                    ]
                ),
            ]
        )

    @callback(
        Output("my-checklist", "value"),
        [
            Input("emotion annotation", "value"),
            Input("sensor data", "value"),
            Input("all-or-none", "value"),
        ],
    )
    def toggle_modal(all_selected, options):
        all_or_none = []
        all_or_none = [option["value"] for option in options if all_selected]
        return all_or_none
