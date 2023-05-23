from dash import html, callback, Input, Output, State
from dash.development.base_component import Component
import dash_bootstrap_components as dbc


class InfoModal:
    def getFC(
        self,
    ) -> Component:
        return html.Div(
            [
                dbc.Button("information", id="open-body-scroll", n_clicks=0),
                dbc.Modal(
                    [
                        dbc.ModalHeader(dbc.ModalTitle("Data Information"), close_button=True),
                        dbc.ModalBody(
                            html.Div([
                                html.P("Frontal view of a participant equipped with wearable sensors"),
                                html.Img(src="https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41597-020-00630-y/MediaObjects/41597_2020_630_Fig2_HTML.png?as=webp",
                                         style={"width":"100%"}),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                html.P("Data collected with each wearable device, with respective sampling rates and signal ranges"),
                                html.Img(src=("assets/devices_2.png"),
                                         style={"width":"100%"}
                                         ),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                html.P("Emotion Annotation Description"),
                                html.Img(src=("assets/emotion_label.png"),
                                         style={"width":"100%"}
                                         ),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                html.P("Summary of data collection results and the dataset"),
                                html.Img(src=("assets/summary.png"),
                                         style={"width":"100%"}
                                         ),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                html.Br(),
                                html.P("Steps for a data collection session"),
                                html.Img(src=("assets/collection.png"),
                                         style={"width":"100%"}
                                         ),

                            
                            ])),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Close",
                                id="close-body-scroll",
                                className="ms-auto",
                                n_clicks=0,
                            )
                        ),
                    ],
                    id="modal-body-scroll",
                    scrollable=True,
                    #centered=True,
                    is_open=False,
                ),
            ]
        )


    
    @callback(
        Output("modal-body-scroll", "is_open"),
        [
            Input("open-body-scroll", "n_clicks"), 
            Input("close-body-scroll", "n_clicks")
        ],
        [State("modal-body-scroll", "is_open")]
    )

    def toggle_modal(n1, n2, is_open):
        if n1 or n2:
            return not is_open
        return is_open