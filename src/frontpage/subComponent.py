from dash import html
from dash.development.base_component import Component

# 예시 코드
class SubComponent:
    # FC: Functional Component 함수형 컴포넌트.
    # 함수 호출로 html element 를 뱉어서 받아다 쓰게 구조화.
    def getFC() -> Component:
        return html.Div(className="subContainer", children=[
            html.H1(className="test", children="test text")
        ])
        


# 코드 돌아가는지 테스트용
if __name__ == '__main__':
    print('skip')
