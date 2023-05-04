import dash
import dash_bootstrap_components as dbc
from dash.development.base_component import Component
from typing import List


# upper navigation bar
class NavbarComponent:
    def __getNavLinks(self) -> List[dbc.NavLink]:
        pages = dash.page_registry.values()
        pages_navigatable = [page for page in pages if page.get("top_nav")]
        pages_navigatable_sorted = sorted(
            pages_navigatable, key=lambda page: page.get("top_nav_order")
        )
        return [
            dbc.NavLink(page["name"], href=page["path"])
            for page in pages_navigatable_sorted
        ]

    def getFC(self) -> Component:
        # TODO: 예쁘게 바꾸기. 현재는 예시코드 가져다 붙인 거.
        # https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/
        # 나중에 분명 예쁘게 바꾸게 될거고, 간격같은거 style 건들면 될 것.
        links = self.__getNavLinks()
        return dbc.NavbarSimple(
            dbc.Nav(links),
            brand="EmoViz",
            color="primary",
            dark=True,
            className="mb-2",
        )


# 코드 돌아가는지 테스트용
if __name__ == "__main__":
    print("skip")
