import dash
from dash import html

dash.register_page(
    __name__,
    name="Home",
    path="/",
    top_nav=True,
    top_nav_order=0,
)

# 첫 페이지!
# 가장 처음에 열립니다.
# 아래 TODO들을 layout에 들어가게 짜면 됩니다.
# TODO: 제목 넣기.
# TODO: Info 넣기
# TODO: Image 넣기.
# TODO: 다음 버튼 넣기.
layout = html.Div(
    children=[
        html.H1(children="This is our Home page"),
        html.Div(
            children="""
        This is our Home page content.
    """
        ),
    ]
)

# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
