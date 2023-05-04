import dash
from dash import html

dash.register_page(
    __name__,
    name="Upload",
    path="/upload",
    top_nav=True,
    top_nav_order=1,
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
