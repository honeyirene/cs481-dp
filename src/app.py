import dash
import dash_bootstrap_components as dbc
from component.navbarComponent import NavbarComponent

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container(dash.page_container, fluid=True, style={"height": "100vh"})

if __name__ == "__main__":
    app.run_server(debug=True)
