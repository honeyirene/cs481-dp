import dash
import dash_bootstrap_components as dbc
from dash import html
from component.collapseComponent import CollapseComponent
from component.titleComponent import TitleComponent

dash.register_page(
    __name__,
    name="Quality Control",
    path="/quality_control",
    top_nav=True,
    top_nav_order=2,
)

# 퀄리티 컨트롤 페이지
# 아래 TODO들을 layout에 들어가게 짜면 됩니다.
# TODO: 제목 넣기.
# TODO: ....
#

left = dbc.Accordion(
    [
        dbc.AccordionItem(
            [html.P("Sensor 1")],
            title="Sensor 1",
        ),
        dbc.AccordionItem(
            [html.P("Sensor 2")],
            title="Sensor 2",
        ),
        dbc.AccordionItem(
            [html.P("Sensor 3")],
            title="Sensor 3",
        ),
    ],
    style={
        "width": "55%",
        "margin-right": "5%",
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
