#########################################
### <view page>
### mainly managed by Minhyeok Seo.
#########################################

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
        html.H1(children=html.B("EmoViz")),
        html.Div(html.Br()),
        html.Br(),
        html.Div(
            children=[
                html.H2("Purpose"),
                html.Br(),
                html.H5("Tracking your K-emocon Data with our tool."),
                html.H5("We provide simple views and quality controls for catching trend of multi-modal data."),
                html.Br(),
                html.Br(),
            ],
        ),
        html.Div(
            children=[
                html.H2("Caution"),
                html.Br(),
                html.H5("This tool is based on K-emocon dataset."),
                html.H5("So, you must keep data format."),
                html.H5("Please refer to the thesis in the reference section below."),
                html.Br(),
                html.Br(),
            ],
        ),html.Div(
            children=[
                html.H2("Purpose"),
                html.Br(),
                html.Ul(html.Li(html.A("K-EmoCon, a multimodal sensor dataset for continuous emotion recognition in naturalistic conversations", href="https://www.nature.com/articles/s41597-020-00630-y")))
            ],
        ),
    ]
)

# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
