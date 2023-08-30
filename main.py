import dash_bootstrap_components as dbc
from dash import Dash

from src.layout.navbar import navbar

app = Dash(external_stylesheets=[dbc.themes.CERULEAN])

app.layout = navbar

if __name__ == "__main__":
    app.run(debug=True)
