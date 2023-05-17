from typing import List, Union


# add trace 하나에 들어가는 데이터.
class GraphTraceDataModel:
    def __init__(self, name: str, y: List[Union[int, float]]):
        self.name = name
        self.y = y


# sub plot 하나에 들어가는 데이터.
class GraphPlotDataModel:
    def __init__(self, title: str, traces: List[GraphTraceDataModel]):
        self.title = title
        self.traces = traces
