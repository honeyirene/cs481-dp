import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

# TODO: navbar
navbar = dbc.NavbarSimple()
app.layout = dbc.Container([navbar, dash.page_container], fluid=True)

if __name__ == '__main__':
    app.run_server(debug=True)
