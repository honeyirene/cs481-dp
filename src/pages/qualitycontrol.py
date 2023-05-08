import dash
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

title = TitleComponent().getFC("Quality Control")
collapse1 = CollapseComponent().getFC(
    app=dash.get_app(),
    id="1",
    title="title1",
    children=[html.H1("Testest")],
)
collapse2 = CollapseComponent().getFC(
    app=dash.get_app(),
    id="2",
    title="title2",
    children=[html.H1("Testest")],
)

layout = html.Div(
    children=[
        title,
        collapse1,
        collapse2,
    ]
)

# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
