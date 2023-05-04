import dash
from dash import html

dash.register_page(
    __name__,
    name="Upload",
    path="/upload",
    top_nav=True,
    top_nav_order=1,
)

# 데이터 업로드 페이지!
# 아래 TODO들을 layout에 들어가게 짜면 됩니다.
# TODO: 제목 넣기.
# TODO: drag and drop 구현하기.
# TODO: 그에 맞는 UI 구성.
# TODO: 데이터 받아서 사람별로 구별하는거 구현하기.
# 여기 작업은 어느정도 진행하면서 고민 할 부분이 많을거같아요.
# 첫번째로 헤매게 될 부분 - 어떻게 데이터를 받지?
# 두번째로 해매게 될 부분 - 받은 데이터를 어떻게 코드로 관리하지..?
#  - 다른 페이지에서도 데이터를 받아야 해서 이걸 어떻게 처리할지가 관건.
#  - 참조
#    - https://dash.plotly.com/dash-core-components/store
#    - https://dash.plotly.com/sharing-data-between-callbacks

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
