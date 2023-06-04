import dash
import dash_bootstrap_components as dbc
from dash import html, Input, Output, State
from dash.development.base_component import Component


class ValueModal:
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
                                            html.P("TODO:"),
                                        ]
                                    ),
                                    html.Div(
                                        [
                                            html.H4("Common Tendency Analysis"),
                                            html.P("TODO:"),
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
