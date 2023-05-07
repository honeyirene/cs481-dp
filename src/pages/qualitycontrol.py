import dash
from dash import html
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

layout = html.Div(
    children=[
        title,
    ]
)

# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")