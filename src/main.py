from dash import Dash
from frontpage.mainConponent import MainComponent

def main() -> None:
    app: Dash = Dash(__name__)
    MainComponent.register(app)
    app.run_server(debug=True)
    return

if __name__ == '__main__':
    main()
