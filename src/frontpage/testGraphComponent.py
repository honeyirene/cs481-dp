from dataclasses import dataclass
from dash import html, dcc, Dash
from dash.development.base_component import Component
import pandas as pd
import plotly.graph_objects as go

from store.pickleStore import PickleStore
from dataStructure.researchData import ResearchData

@dataclass
class TestGraphProps:
    a: int

# 예시 코드
class TestGraphComponent:
    app: Dash

    # def __init__(self, app: Dash):
    #     self.app = app

    # FC: Functional Component 함수형 컴포넌트.
    # 함수 호출로 html element 를 뱉어서 받아다 쓰게 구조화.
    def getFC(props: TestGraphProps) -> Component:
        store: PickleStore = PickleStore()
        data: ResearchData = store.load()

        temperature_data = data.get('X')[0].get('e4.temp')
        temperature_stat = data.get('baseline').get(4).get('e4.temp')

        df = pd.DataFrame({
            'time': [i * 0.25 for i in range(20)],
            'temperature': temperature_data,
        })

        fig = go.Figure()
        fig.add_traces(go.Scatter(name='Test', x=df['time'], y=df['temperature'], marker_color='rgb(205, 127, 50)'))

        return html.Div(className="subContainer", children=[
            dcc.Graph(id='test-graph', 
                figure=fig
            )
        ])
    
    # @app.callback(Output('test-graph', 'figure'),Input())
    # def update_graph():


# 코드 돌아가는지 테스트용
if __name__ == '__main__':
    print('skip')
