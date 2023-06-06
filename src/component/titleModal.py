import dash
import dash_bootstrap_components as dbc
from dash import html, Input, Output, State
from dash.development.base_component import Component


class TitleModal:
    def getFC(self) -> Component:
        app = dash.get_app()

        @app.callback(
            Output("title-modal-body", "is_open"),
            [
                Input("title-modal-button", "n_clicks"),
                Input("title-modal-body-footer", "n_clicks"),
            ],
            [State("title-modal-body", "is_open")],
        )
        def toggle_modal(n1, n2, is_open):
            if n1 or n2:
                return not is_open
            return is_open

        return html.Div(
            [
                dbc.Button(
                    "i",
                    id="title-modal-button",
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
                                            html.H4("Introduce"),
                                            html.P("Emo-Viz is a tool that helps researchers handle multi-modal data at once."),
                                        ]
                                    ),
                                    html.Div(
                                        [
                                            html.H4("Purpose"),
                                            html.P("Tracking your K-emocon Data with our tool. We provide simple views for catching trendency of multi-modal data."),
                                        ]
                                    ),
                                    html.Div(
                                        [
                                            html.H4("How to use"),
                                            html.P(" - The graph shows when the current video is running."),
                                            html.P(" - You can change the ratio between graph and video with the toggle on the top."),
                                            html.P(" - You can change the order of the graphs by dragging them."),
                                            html.P(" - You can check the information by pressing the 'i' and 'information' button."),
                                            
                                        ]
                                    ),
                                ]
                            )
                        ),
                        dbc.ModalFooter(
                            dbc.Button(
                                "Close",
                                id="title-modal-body-footer",
                                className="ms-auto",
                                n_clicks=0,
                            )
                        ),
                    ],
                    id="title-modal-body",
                    scrollable=True,
                    size="xl",
                    is_open=False,
                ),
            ]
        )
