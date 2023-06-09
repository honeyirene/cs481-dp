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
    KEY19 = "Brainwave (relative power)"
    KEY20 = "attention & meditation"

    INFO_DESC1 = "Two afective dimensions from Russell’s circumplex model of afect. The value of arousal and valence feelings among the emotions felt by the external observer."
    INFO_DESC2 = "Emotion states described by extenal observer's stress state"
    INFO_DESC3 = "Commonly used Baker Rodrigo Ocumpaugh Monitoring Protocol (BROMP) educationally relevant afective categories observed by external observer"
    INFO_DESC4 = "Less commonly used BROMP educationally relevant afective categories observed by external observer"
    INFO_DESC5 = "Two afective dimensions from Russell’s circumplex model of afect. The value of arousal and valence feelings among the emotions felt by the partner."
    INFO_DESC6 = "Emotion states described by partner's stress state"
    INFO_DESC7 = "Commonly used Baker Rodrigo Ocumpaugh Monitoring Protocol (BROMP) educationally relevant afective categories observed by partner"
    INFO_DESC8 = "Less commonly used BROMP educationally relevant afective categories observed by partner"
    INFO_DESC9 = "Two afective dimensions from Russell’s circumplex model of afect. The value of arousal and valence feelings among the emotions felt by participant himself."
    INFO_DESC10 = "Emotion states described by participant's stress state"
    INFO_DESC11 = "Commonly used Baker Rodrigo Ocumpaugh Monitoring Protocol (BROMP) educationally relevant afective categories choosen by participant himself"
    INFO_DESC12 = "Less commonly used BROMP educationally relevant afective categories choosen by participant himself"
    INFO_DESC13 = "Accelerration of participant's wrist for each 3-axis captured by Empatica E4 Wristband. Sampling rate is 32Hz and Signal range si from -2g to 2g"
    INFO_DESC14 = "Blood Volume Pulse(BVP) captured with photoplethysmography(PPG) in Empatica E4 Wristband. It use a light emitter to emit light onto the human body and then use a photodetector to measure the BVP by measuring the amount of light that is not reflected or absorbed. Sampling rate is 64Hz"
    INFO_DESC15 = "Electrodermal activity caputured by Empatica E4 Wristband. EDA is a characteristic of the human body that continuously changes the electrical properties of the skin. It can be measured by assessing the electrochemical skin conductance to determine the activity of the autonomic nervous system. Sampling rate is 64Hz and signal range is from 0.01 uS to 100uS"
    INFO_DESC16 = "Heart rate is capture from both Empatica E4 Wristband and Polar H7 Bluetooth Heart Rate Sensor. Sampling rate is 1Hz from BVP and 1HZ from ECG"
    INFO_DESC17 = "Interbeat interval(IBI) is the time interval between individual beats of the mammalian heart. "
    INFO_DESC18 = "Body tempterature of participants captured by Empatica E4 Wristband. Sampling rate is 4Hz and Signal range is from -40℃ to 115℃"
    INFO_DESC19 = "The relative strength of brainwaves in each frequency band measured by the NeuroSky. Sampling rate is 125Hz."
    INFO_DESC20 = "Degree of attention & meditation by participant captured by NeuroSky. Sampling rate is 1Hz"

    TENDENCY_DESC1 = "1: very low - 2: low - 3: neutral- 4: high - 5: very high for each value. If the balance value is low, it is unpleasant, if it is high, it is pleasant, if the arousal value is low, it is calm, and if it is high, it is excited."
    TENDENCY_DESC2 = "1: very low - 2: low - 3: high- 4: very high for each value"
    TENDENCY_DESC3 = "Choose one category among Boredom / Confusion / Delight / Engaged concentration/ Frustration / Surprise / None"
    TENDENCY_DESC4 = "Choose one category among Confrustion / Contempt / Dejection / Disgust / Eureka / Pride / Sorrow / None"
    TENDENCY_DESC5 = "1: very low - 2: low - 3: neutral- 4: high - 5: very high for each value. If the balance value is low, it is unpleasant, if it is high, it is pleasant, if the arousal value is low, it is calm, and if it is high, it is excited."
    TENDENCY_DESC6 = "1: very low - 2: low - 3: high- 4: very high for each value"
    TENDENCY_DESC7 = "Choose one category among Boredom / Confusion / Delight / Engaged concentration/ Frustration / Surprise / None"
    TENDENCY_DESC8 = "Choose one category among Confrustion / Contempt / Dejection / Disgust / Eureka / Pride / Sorrow / None"
    TENDENCY_DESC9 = "1: very low - 2: low - 3: neutral- 4: high - 5: very high for each value. If the balance value is low, it is unpleasant, if it is high, it is pleasant, if the arousal value is low, it is calm, and if it is high, it is excited."
    TENDENCY_DESC10 = "1: very low - 2: low - 3: high- 4: very high for each value"
    TENDENCY_DESC11 = "Choose one category among Boredom / Confusion / Delight / Engaged concentration/ Frustration / Surprise / None"
    TENDENCY_DESC12 = "Choose one category among Confrustion / Contempt / Dejection / Disgust / Eureka / Pride / Sorrow / None"
    TENDENCY_DESC13 = "According to each axis, the closer the value is to 0, the less the movement is, and the higher the absolute value, the more quick the movement."
    TENDENCY_DESC14 = "mean BVP for each sampling"
    TENDENCY_DESC15 = "number of peaks exceeding 100 Ω per second, mean peak amplitude from the saddle point preceding the peak, mean rise time for the signal to reach its peak from the saddle point in seconds, mean GSR, and standard deviation of GSR"
    TENDENCY_DESC16 = "mean and standard deviation for each sampling"
    TENDENCY_DESC17 = "mean inter-beat interval from BVP"
    TENDENCY_DESC18 = "There tendency to be a tendency for more comfortable discussions when body temperature is lower"
    TENDENCY_DESC19 = "Delta waves(0.5Hz~2.75Hz): Delta waves have a relative low strength and are primarily associated with deep sleep and the brain's restorative processes. Theta wavesa (3.5~6.75Hz): Theta waves have a moderate strength and are commonly observed during dreaming or meditative states. low-Alpha(7.5~9.25Hz) & high-Alpha(10~11.75Hz) waves: Alpha waves have a moderate strength and are typically present when the brain is in a relaxed state or during closed-eye meditation. low-Beta (13~16.75Hz)& high-Beta(18~29.75Hz) waves: Beta waves have a relatively high strength and are associated with cognitive activity, focused attention, and alertness. low-Gamma(31~39.75Hz) & high-Gamma(41~49.75Hz) waves: Gamma waves have a relatively high strength and are primarily linked to cognitive processing, problem-solving, learning, and concentration."
    TENDENCY_DESC20 = "Attention value means s eSense Attention ranging from 1 to 100, representing how attentive a user was at a given moment. Attention values can be interpreted as the following: 1 to 20 - “strongly lowered”, 20 to 40 - “reduced”, 40 to 60 - “neutral”, 60 to 80 - “slightly elevated”, and 80 to 100 - “elevated”. 0 indicates that the device was unable to calculate a sufciently reliable value, possibly due to a signal contamination with noises. Meditation means  eSense Meditation ranging from 0 to 100, measuring the relaxedness of a user. For their interpretation, use the same ranges and the meanings as those for the attention values."

    tendencyDesc = {
        KEY1: TENDENCY_DESC1,
        KEY2: TENDENCY_DESC2,
        KEY3: TENDENCY_DESC3,
        KEY4: TENDENCY_DESC4,
        KEY5: TENDENCY_DESC5,
        KEY6: TENDENCY_DESC6,
        KEY7: TENDENCY_DESC6,
        KEY8: TENDENCY_DESC8,
        KEY9: TENDENCY_DESC9,
        KEY10: TENDENCY_DESC10,
        KEY11: TENDENCY_DESC11,
        KEY12: TENDENCY_DESC12,
        KEY13: TENDENCY_DESC13,
        KEY14: TENDENCY_DESC14,
        KEY15: TENDENCY_DESC15,
        KEY16: TENDENCY_DESC16,
        KEY17: TENDENCY_DESC17,
        KEY18: TENDENCY_DESC18,
        KEY19: TENDENCY_DESC19,
        KEY20: TENDENCY_DESC20,
    }

    infoDesc = {
        KEY1: INFO_DESC1,
        KEY2: INFO_DESC2,
        KEY3: INFO_DESC3,
        KEY4: INFO_DESC4,
        KEY5: INFO_DESC5,
        KEY6: INFO_DESC6,
        KEY7: INFO_DESC7,
        KEY8: INFO_DESC8,
        KEY9: INFO_DESC9,
        KEY10: INFO_DESC10,
        KEY11: INFO_DESC11,
        KEY12: INFO_DESC12,
        KEY13: INFO_DESC13,
        KEY14: INFO_DESC14,
        KEY15: INFO_DESC15,
        KEY16: INFO_DESC16,
        KEY17: INFO_DESC17,
        KEY18: INFO_DESC18,
        KEY19: INFO_DESC19,
        KEY20: INFO_DESC20,
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
