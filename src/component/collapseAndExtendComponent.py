# from dash import html
# from dash.development.base_component import Component
# from dash import html, callback, Input, Output


# class CollapseAndExtendComponent:
#     def getFC(
#         self,
#         children: Component,
#     ) -> Component:
#         return html.Div(
#             children=[
#                 self.__upperBar(),
#                 self.__mainContainer(
#                     leftUpperChildren,
#                     leftLowerChildren,
#                     rightChildren,
#                 ),
#             ],
#             style={"height": "97%", "overflow": "hidden"},
#         )

#     @callback(
#         Output("left-panel", "style"),
#         Output("left-upper-panel", "style"),
#         Output("left-lower-panel", "style"),
#         Output("right-panel", "style"),
#         Input("input", "n_clicks"),
#     )
#     def changePortion(n_clicks):
#         print(n_clicks)
#         if (n_clicks) % 2 == 0:
#             leftStyle = {
#                 "width": "35%",
#             }
#             rightStyle = {
#                 "width": "64%",
#                 "height": "100%",
#                 "border": "1px solid cyan",
#                 "overflow": "auto",
#             }
#             leftUpperStyle = {
#                 "height": "300px",
#                 "border": "1px solid cyan",
#             }
#             leftLowerStyle = {
#                 "border": "1px solid cyan",
#             }
#         else:
#             leftStyle = {
#                 "width": "49.5%",
#             }
#             rightStyle = {
#                 "width": "49.5%",
#                 "height": "100%",
#                 "border": "1px solid cyan",
#                 "overflow": "auto",
#             }
#             leftUpperStyle = {
#                 "height": "500px",
#                 "border": "1px solid cyan",
#             }
#             leftLowerStyle = {
#                 "border": "1px solid cyan",
#             }

#         return leftStyle, leftUpperStyle, leftLowerStyle, rightStyle
