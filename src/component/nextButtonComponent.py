import dash
import dash_bootstrap_components as dbc
from dash.development.base_component import Component


class nextButtonComponent:
    def __getNavLinks(self, pageName: str):
        pages = dash.page_registry.values()
        for page in pages:
            if page["name"] ==pageName:
                return page["path"]
        print("wrong page name")

    def getFC(self, title, pageName)-> Component:
        return dbc.Button(
            title,
            href= self.__getNavLinks(pageName) )