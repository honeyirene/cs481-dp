import dash
import datetime

from dash.dependencies import Input, Output, State
from dash import dcc, html, Dash

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

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

layout = html.Div(
    children=[
        html.H1(children="This is our Home page"),
        html.Div(
            children="""
                This is our Home page content.
                """
        ),
        dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),

        
    ]
)


def parse_contents(contents, filename, date):
    return html.Div([
        html.H5(filename),
        html.H6(datetime.datetime.fromtimestamp(date)),

        # HTML images accept base64 encoded strings in the same format
        # that is supplied by the uploadSS
        html.Img(src=contents),
        html.Hr(),
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])
@app.callback(Output('output-image-upload', 'children'),
              Input('upload-image', 'contents'),
              State('upload-image', 'filename'),
              State('upload-image', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
