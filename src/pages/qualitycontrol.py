import dash
from dash import html

dash.register_page(
    __name__,
    name="Quality Control",
    path="/quality_control",
    top_nav=True,
    top_nav_order=2,
)

layout = html.Div(
    children=[
        html.H1(children="quality control"),
        html.Div(
            children="""
        quality control
    """
        ),
    ]
)

# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
