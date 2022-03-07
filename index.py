import os

from dash import dcc, html
from dash.dependencies import Input, Output

from app1.pages.sidebar import app1_sidebar
from app1.routes import app1_urlpatterns
from dash_app.app import app
from dash_app.base.urls import display_page
from dash_app.base.utils import setup_logging
from dash_app.config import BASE_PATH

LOGGING_CONFIG_PATH = os.path.join(BASE_PATH, 'dash_app/logging.yaml')
"""
main app layout, which has a component to track the url, and rest are
div to store sidebar, and content
"""
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='sidebar'),
    html.Div(id='page-content',
             style={
                 "margin-left": "18rem",
                 "margin-right": "2rem",
                 "padding": "2rem 1rem",
             })
])


@app.callback(Output('page-content', 'children'),
              Output('sidebar', 'children'), Input('url', 'pathname'))
def display_app(pathname):
    """
    callback function to update the correct app related
    routes to the main app
    """
    if pathname.split('/')[1] == 'app':
        return display_page(pathname, app1_urlpatterns), app1_sidebar
    else:
        return '404'


if __name__ == "__main__":
    setup_logging()
    app.run_server(debug=True)
