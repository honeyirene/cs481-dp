import dash_bootstrap_components as dbc
from dash import html, Input, Output, State, Dash
from dash.development.base_component import Component


# quality contorol 쪽에 전체를 접고 펴는 ui용 컴포넌트
# collapse ref: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/collapse/
# functional component with callback: https://community.plotly.com/t/reusable-dash-components-with-callback-functions/49540
class CollapseComponent:
    def getFC(self, app: Dash, id: str, title: str, children: None) -> Component:
        buttonId = "collapse-button-" + id
        collapseId = "collapse-" + id

        collapse = html.Div(
            [
                dbc.Button(
                    children=title,
                    id=buttonId,
                    className="mb-3",
                    color="primary",
                    n_clicks=0,
                ),
                dbc.Collapse(
                    children=children,
                    id=collapseId,
                    is_open=False,
                ),
            ]
        )

        @app.callback(
            Output(collapseId, "is_open"),
            [Input(buttonId, "n_clicks")],
            [State(collapseId, "is_open")],
        )
        def toggle(n, is_open):
            if n:
                return not is_open
            return is_open

        return collapse


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
