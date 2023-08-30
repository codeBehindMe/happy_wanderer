from dash import Dash 
import dash_bootstrap_components as dbc
from src.layout.navbar import navbar

app = Dash(external_stylesheets=[dbc.themes.CERULEAN])

app.layout = navbar

if __name__ == '__main__':
    app.run(debug=True)