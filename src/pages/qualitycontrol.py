import dash
import dash_bootstrap_components as dbc
from dash import html
from component.qualityControlSensorComponent import QualityControlSensorComponent
from component.titleComponent import TitleComponent

dash.register_page(
    __name__,
    name="Quality Control",
    path="/quality_control",
    top_nav=True,
    top_nav_order=2,
)

left = dbc.Accordion(
    [
        dbc.AccordionItem(
            QualityControlSensorComponent().getFC(
                [
                    ["3-axis acceleration", "BVP (PPG)", "EDA"],
                    ["Heart rate (from BVP)", "IBI (from BVP)", "Body temperature"],
                ]
            ),
            title="Empatica E4 Wristband",
        ),
        dbc.AccordionItem(
            QualityControlSensorComponent().getFC(
                [
                    ["Brainwave (fp1 channel EEG)", "Attention & Meditation"],
                ]
            ),
            title="NeuroSky MindWave Headset",
        ),
        dbc.AccordionItem(
            QualityControlSensorComponent().getFC(
                [
                    ["HR (ECG)", "Audio"],
                ]
            ),
            title="Other Measurement",
        ),
    ],
    style={
        "width": "60%",
        "margin-right": "1%",
    },
)
right = dbc.Card(
    [dbc.CardBody()],
    style={
        "width": "35%",
    },
)

title = TitleComponent().getFC("Quality Control")
middle = html.Div(
    children=[left, right],
    style={
        "display": "flex",
        "justify-content": "center",
        "margin-top": "30px",
    },
)

layout = html.Div(
    children=[
        title,
        middle,
    ]
)

# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
