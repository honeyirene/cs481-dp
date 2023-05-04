import dash
from dash import html

dash.register_page(
    __name__,
    name="Home",
    path="/",
    top_nav=True,
    top_nav_order=0,
)

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
