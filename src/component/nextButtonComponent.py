import dash
import dash_bootstrap_components as dbc
from dash.development.base_component import Component


class nextButtonComponent:
    def __getPageLinks(self, pageName: str):
        pages = dash.page_registry.values()
        for page in pages:
            print(page["path"])
            if page["name"] == pageName:
                return page["path"]
        print("wrong page name")

    def getFC(self, title, pageLink) -> Component:
        return dbc.Button(title, href=pageLink)
