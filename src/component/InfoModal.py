from dash import html, callback, Input, Output, State
from dash.development.base_component import Component
import dash_bootstrap_components as dbc
from dash import dcc


# class InfoModal:
#     def getFC(
#         self,
#     ) -> Component:
#         return html.Div(
#             [
#                 dbc.Button("information", id="open-body-scroll", n_clicks=0),
#                 dbc.Modal(
#                     [
#                         dbc.ModalHeader(
#                             dbc.ModalTitle("Data Information"), close_button=True
#                         ),
#                         dbc.ModalBody(
#                             html.Div(
#                                 [
#                                     html.P(
#                                         "Frontal view of a participant equipped with wearable sensors"
#                                     ),
#                                     html.Img(
#                                         src="https://media.springernature.com/full/springer-static/image/art%3A10.1038%2Fs41597-020-00630-y/MediaObjects/41597_2020_630_Fig2_HTML.png?as=webp",
#                                         style={"width": "100%"},
#                                     ),
#                                     html.Br(),
#                                     html.Br(),
#                                     html.Br(),
#                                     html.Br(),
#                                     html.P(
#                                         "Data collected with each wearable device, with respective sampling rates and signal ranges"
#                                     ),
#                                     html.Img(
#                                         src=("assets/devices_2.png"),
#                                         style={"width": "100%"},
#                                     ),
#                                     html.Br(),
#                                     html.Br(),
#                                     html.Br(),
#                                     html.Br(),
#                                     html.P("Emotion Annotation Description"),
#                                     html.Img(
#                                         src=("assets/emotion_label.png"),
#                                         style={"width": "100%"},
#                                     ),
#                                     html.Br(),
#                                     html.Br(),
#                                     html.Br(),
#                                     html.Br(),
#                                     html.P(
#                                         "Summary of data collection results and the dataset"
#                                     ),
#                                     html.Img(
#                                         src=("assets/summary.png"),
#                                         style={"width": "100%"},
#                                     ),
#                                     html.Br(),
#                                     html.Br(),
#                                     html.Br(),
#                                     html.Br(),
#                                     html.P("Steps for a data collection session"),
#                                     html.Img(
#                                         src=("assets/collection.png"),
#                                         style={"width": "100%"},
#                                     ),
#                                 ]
#                             )
#                         ),
#                         dbc.ModalFooter(
#                             dbc.Button(
#                                 "Close",
#                                 id="close-body-scroll",
#                                 className="ms-auto",
#                                 n_clicks=0,
#                             )
#                         ),
#                     ],
#                     id="modal-body-scroll",
#                     scrollable=True,
#                     # centered=True,
#                     size="xl",
#                     is_open=False,
#                 ),
#             ]
#         )


class InfoModal:
    def getFC(
        self,
    ) -> Component:
        return html.Div(
            [   
                html.Div([
                    html.B('Items to Chart'),
                    dcc.Checklist(
                        id='all-or-none',
                        options=[{'lable': 'Select All', 'value': 'All'}],
                        value=['All'],
                        labelStyle={'display': 'block'},
                    ),
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Div([
                                        html.B("Emotion Annotation"),
                                        dcc.Checklist(
                                            id='emotion annotation',
                                            options=[
                                                {'label': 'Arousal & Valence (ext)', 'value': 'a&v(e)'},
                                                {'label': 'Stress (ext)', 'value': 'stress(e)'},
                                                {'label': 'cBROMP (ext)', 'value': 'cBROMP(e)'},
                                                {'label': 'lcBROMP (ext)', 'value': 'lcBROMP(e)'},
                                                {'label': 'Arousal & Valence (pnr)', 'value': 'a&v(p)'},
                                                {'label': 'Stress (pnr)', 'value': 'stress(p)'},
                                                {'label': 'cBROMP (pnr)', 'value': 'cBROMP(p)'},
                                                {'label': 'lcBROMP (pnr)', 'value': 'lcBROMP(p)'},
                                                {'label': 'Arousal & Valence (self)', 'value': 'a&v(s)'},
                                                {'label': 'Stress (self)', 'value': 'stress(s)'},
                                                {'label': 'cBROMP (self)', 'value': 'cBROMP(s)'},
                                                {'label': 'lcBROMP (self)', 'value': 'lcBROMP(s)'},
                                            ],
                                            value = ['a&v(e)','stress(e)','cBROMP(e)','lcBROMP(e)',
                                                     'a&v(p)','stress(p)','cBROMP(p)','lcBROMP(p)',
                                                     'a&v(s)','stress(s)','cBROMP(s)','lcBROMP(s)'],
                        #labelStyle={'display': 'block'},
                                        )
                                    ]),
                                ),
                                dbc.Col(
                                    html.Div([
                                        html.B("Sensor Data"),
                                        dcc.Checklist(
                                            id='sensor data',
                                            options=[
                                                {'label': '3 axis acceleration', 'value': 'acc'},
                                                {'label': 'BVP', 'value': 'BVP'},
                                                {'label': 'EDA', 'value': 'EDA'},
                                                {'label': 'Heart Rate', 'value': 'HR'},
                                                {'label': 'Temperature', 'value': 'T'},
                                                {'label': 'Brainwave', 'value': 'Bw'},
                                                {'label': 'Attention & Meditation', 'value': 'a&m'},
                                                # {'label': 'Emotion Annotation', 'value': 'EmoAnn'},
                                                # {'label': 'Emotion Annotation', 'value': 'EmoAnn'},
                                                # {'label': 'Emotion Annotation', 'value': 'EmoAnn'},
                                                # {'label': 'Emotion Annotation', 'value': 'EmoAnn'},
                                            ],
                                            value = ['acc','BVP','EDA','HR','T','Bw','a&m'],
                        #labelStyle={'display': 'block'},
                                        )
                                    ]),
                                )
                            ]
                        )
                ])
                # dbc.Button("Emotion annotation", color="primary", className="1"),
                # dbc.Button("External observator", color="primary", className="2"),
                # dbc.Button("Arousal & Valence (ext)", color="primary", className="3"),
                # dbc.Button("Partner", color="primary", className="2"),
                # dbc.Button("Self", color="primary", className="2"),
                # dbc.Button("3 axis acceleration", color="primary", className="2"),
                # dbc.Button("BVP", color="primary", className="2"),
                # dbc.Button("EDA", color="primary", className="2"),
                # dbc.Button("Heart Rate", color="primary", className="2"),
                # dbc.Button("IBI", color="primary", className="2"),
                # dbc.Button("Temperature", color="primary", className="2"),
                # dbc.Button("Brainwave", color="primary", className="2"),
                # dbc.Button("3 axis acceleration", color="primary", className="2"),
                # dbc.Button("3 axis acceleration", color="primary", className="2"),
            ]
        )

    @callback(
        Output("my-checklist", "value"),
        [Input("emotion annotation", "value"),
         Input("sensor data", "value"),
         Input("all-or-none",'value')],
        #[State("my-checklist", "options")],
    )
    # def toggle_modal(n1, n2, is_open):
    #     if n1 or n2:
    #         return not is_open
    #     return is_open

    # def update_result(all,emo,sensor):
    #     updated = 
    def toggle_modal(all_selected, options):
        all_or_none = []
        all_or_none = [option['value'] for option in options if all_selected]
        return all_or_none
