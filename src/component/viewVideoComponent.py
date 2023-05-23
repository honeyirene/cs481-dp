from dash import html
from dash.development.base_component import Component
from dash import dcc

#from flask import Flask, Response

#server = Flask(__name__)

# QualityControl 페이지의 왼쪽 Distribution 그래프 하나.
"""class ViewVideoComponent:
    def getFC(self, src=str) -> Component:
        return html.Div(
            children=[
            html.Img(src=src,
                     #style={"height": 150, "width": 240})
                     style={"object-fit": "scale-down"})
            ]
        )"""
class ViewVideoComponent:
    def getFC(self, src=str, filename=str) -> Component:
        return html.Div(
            children=[
            html.Video(
                src="/"+src+"/"+filename,
                controls=True,
                #autoPlay=True,
                style={"object-fit": "cover"},
                #style={"width":300, "height":200, "object-fit": "scale-down"}
            )
            ]
        )


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")

"""html.Video(
    src="/"+src+"/"+filename,
    controls=True,
    #autoPlay=True,
    style={"object-fit": "cover"},
    #style={"width":300, "height":200, "object-fit": "scale-down"}
),"""

"""                html.Br(),
# dcc.Graph(figure=fig_audio.rangeslider),
html.Div(
    dcc.RangeSlider(
        id="time_slider",
        min=0,
        max=600,
        marks=None,
        value=[0, 600],
        tooltip={
            "placement": "bottom",
            "always_visible": True,
        },
    )
),
html.Br(),
html.Br(),"""

"""@server.route('/'+src+'/<path:path>')
def serve_static(path):
    root_dir = os.getcwd()
    return flask.send_from_directory(os.path.join(root_dir, src), path)"""
