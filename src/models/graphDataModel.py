import pandas as pd
from typing import List
from dataStructure.researchDataType import ResearchDataType


# add trace 하나에 들어가는 데이터.
class GraphTraceDataModel:
    def __init__(self, xname: str, yname: str, displayName: str):
        self.xname = xname
        self.yname = yname
        self.displayName = displayName


# sub plot 하나에 들어가는 데이터.
class GraphPlotDataModel:
    def __init__(
        self,
        title: str,
        id: ResearchDataType,
        df: pd.DataFrame,
        traces: List[GraphTraceDataModel],
    ):
        self.title = title
        self.id = id
        self.df = df
        self.traces = traces
