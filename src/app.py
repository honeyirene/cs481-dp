import dash
import dash_bootstrap_components as dbc


app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(dash.page_container, fluid=True, style={"height": "100vh"})
server = app.server

# 드래그 기능을 js 라이브러리에서 가져다가 쓰기 위해 빌드된 파일을 주입한다
app.config.external_stylesheets = app.config.external_stylesheets + [
    "https://epsi95.github.io/dash-draggable-css-scipt/dragula.css"
]
app.config.external_scripts = app.config.external_scripts + [
    "https://cdnjs.cloudflare.com/ajax/libs/dragula/3.7.2/dragula.min.js",
    "https://epsi95.github.io/dash-draggable-css-scipt/script.js",
]

if __name__ == "__main__":
    app.run_server(debug=True)
