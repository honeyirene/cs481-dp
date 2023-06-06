import dash
import dash_bootstrap_components as dbc
from dash import html, Input, Output, State
from dash.development.base_component import Component


class ValueModal:
    KEY1 = "arousal & valence (ext)"
    KEY2 = "stress (ext)"
    KEY3 = "educational 1 (e)"
    KEY4 = "educational 2 (e)"
    KEY5 = "arousal & valence (pnr)"
    KEY6 = "stress (pnr)"
    KEY7 = "educational 1 (p)"
    KEY8 = "educational 2 (p)"
    KEY9 = "arousal & valence (self)"
    KEY10 = "stress (self)"
    KEY11 = "educational 1 (s)"
    KEY12 = "educational 2 (s)"
    KEY13 = "3 axis acceleration (g)"
    KEY14 = "BVP (PPG)"
    KEY15 = "EDA (uS)"
    KEY16 = "Heart Rate"
    KEY17 = "IBI"
    KEY18 = "Temperature (℃)"
    KEY19 = "relative power"
    KEY20 = "attention & meditation"

    INFO_DESC1 = "The value of arousal and valence feelings among the emotions felt by the external observer."
    INFO_DESC2 = "stress (ext) info"
    INFO_DESC3 = "educational 1 (e) info"
    INFO_DESC4 = "educational 2 (e) info"
    INFO_DESC5 = "arousal & valence (pnr) info"
    INFO_DESC6 = "stress (pnr) info"
    INFO_DESC7 = "educational 1 (p) info"
    INFO_DESC8 = "educational 2 (p) info"
    INFO_DESC9 = "arousal & valence (self) info"
    INFO_DESC10 = "stress (self) info"
    INFO_DESC11 = "educational 1 (s) info"
    INFO_DESC12 = "educational 2 (s) info"
    INFO_DESC13 = "axis acceleration (g) info"
    INFO_DESC14 = "BVP (PPG) info"
    INFO_DESC15 = "EDA (uS) info"
    INFO_DESC16 = "Heart Rate info"
    INFO_DESC17 = "IBI info"
    INFO_DESC18 = "Temperature (℃) info"
    INFO_DESC19 = "relative power info"
    INFO_DESC20 = "attention & meditation info"

    TENDENCY_DESC1 = "If the balance value is low, it is unpleasant, if it is high, it is pleasant, if the arousal value is low, it is calm, and if it is high, it is excited."
    TENDENCY_DESC2 = "stress (ext) TENDENCY"
    TENDENCY_DESC3 = "educational 1 (e) TENDENCY"
    TENDENCY_DESC4 = "educational 2 (e) TENDENCY"
    TENDENCY_DESC5 = "arousal & valence (pnr) TENDENCY"
    TENDENCY_DESC6 = "stress (pnr) TENDENCY"
    TENDENCY_DESC7 = "educational 1 (p) TENDENCY"
    TENDENCY_DESC8 = "educational 2 (p) TENDENCY"
    TENDENCY_DESC9 = "arousal & valence (self) TENDENCY"
    TENDENCY_DESC10 = "stress (self) TENDENCY"
    TENDENCY_DESC11 = "educational 1 (s) TENDENCY"
    TENDENCY_DESC12 = "educational 2 (s) TENDENCY"
    TENDENCY_DESC13 = "axis acceleration (g) TENDENCY"
    TENDENCY_DESC14 = "BVP (PPG) TENDENCY"
    TENDENCY_DESC15 = "EDA (uS) TENDENCY"
    TENDENCY_DESC16 = "Heart Rate TENDENCY"
    TENDENCY_DESC17 = "IBI TENDENCY"
    TENDENCY_DESC18 = "Temperature (℃) TENDENCY"
    TENDENCY_DESC19 = "relative power TENDENCY"
    TENDENCY_DESC20 = "attention & meditation TENDENCY"

    tendencyDesc = {KEY1:TENDENCY_DESC1,
        KEY2:TENDENCY_DESC2,
        KEY3:TENDENCY_DESC3,
        KEY4:TENDENCY_DESC4,
        KEY5:TENDENCY_DESC5,
        KEY6:TENDENCY_DESC6,
        KEY7:TENDENCY_DESC6,
        KEY8:TENDENCY_DESC8,
        KEY9:TENDENCY_DESC9,
        KEY10:TENDENCY_DESC10,
        KEY11:TENDENCY_DESC11,
        KEY12:TENDENCY_DESC12,
        KEY13:TENDENCY_DESC13,
        KEY14:TENDENCY_DESC14,
        KEY15:TENDENCY_DESC15,
        KEY16:TENDENCY_DESC16,
        KEY17:TENDENCY_DESC17,
        KEY18:TENDENCY_DESC18,
        KEY19:TENDENCY_DESC19,
        KEY20:TENDENCY_DESC20,
    }

    infoDesc = {KEY1:INFO_DESC1,
        KEY2:INFO_DESC2,
        KEY3:INFO_DESC3,
        KEY4:INFO_DESC4,
        KEY5:INFO_DESC5,
        KEY6:INFO_DESC6,
        KEY7:INFO_DESC7,
        KEY8:INFO_DESC8,
        KEY9:INFO_DESC9,
        KEY10:INFO_DESC10,
        KEY11:INFO_DESC11,
        KEY12:INFO_DESC12,
        KEY13:INFO_DESC13,
        KEY14:INFO_DESC14,
        KEY15:INFO_DESC15,
        KEY16:INFO_DESC16,
        KEY17:INFO_DESC17,
        KEY18:INFO_DESC18,
        KEY19:INFO_DESC19,
        KEY20:INFO_DESC20,
    }
    def getFC(self, id: str) -> Component:
        app = dash.get_app()

        @app.callback(
            Output("value-modal-body-" + str(id), "is_open"),
            [
                Input("value-modal-button-" + str(id), "n_clicks"),
                Input("value-modal-body-footer-" + str(id), "n_clicks"),
            ],
            [State("value-modal-body-" + str(id), "is_open")],
        )
        def toggle_modal(n1, n2, is_open):
            if n1 or n2:
                return not is_open
            return is_open
        
        info = "key missing"
        if str(id) in self.infoDesc:
            info = self.infoDesc[str(id)]

        tendency = "key missing"
        if str(id) in self.tendencyDesc:
            tendency = self.tendencyDesc[str(id)]


        return html.Div(
            [
                dbc.Button(
                    "i",
                    id="value-modal-button-" + str(id),
                    n_clicks=0,
                    style={
                        "paddingLeft": "10px",
                        "paddingRight": "10px",
                        "paddingTop": "0px",
                        "paddingBottom": "0px",
                    },
                ),
                dbc.Modal(
                    [
                        dbc.ModalHeader(dbc.ModalTitle("EmoVis"), close_button=True),
                        dbc.ModalBody(
                            html.Div(
                                [
                                    html.Div(
                                        [
                                            html.H4("Information"),
                                            html.P(info),
                                        ]
                                    ),
                                    html.Div(
                                        [
                                            html.H4("Common Tendency Analysis"),
                                            html.P(tendency),
                                        ]
                                    ),
                                ]
                            )
                        ),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Close",
                                id="value-modal-body-footer-" + str(id),
                                className="ms-auto",
                                n_clicks=0,
                            )
                        ),
                    ],
                    id="value-modal-body-" + str(id),
                    scrollable=True,
                    size="xl",
                    is_open=False,
                ),
            ],
        )
