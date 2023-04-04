import numpy
from typing import Dict, Union, List

# 사실상 numpy ndarray 인게 많음.
# ndarray.dtype 이나 ndarray.astype 같은거 활용?
# 파이썬의 타입은 큰 코드에서 언제나 폭탄이 될 수 있으니 조심.

Data_X = List[Dict[str, Union[List[numpy.float64], List[numpy.int64]]]]
Data_y = List[List[numpy.int64]]
Data_baseline = Dict[int, Dict[str, Dict[str,numpy.float64]]]
Data_pids = List[numpy.int64]
Data_labels = List[str]
Data_data_types = List[str]

ResearchDataElement = Union[Data_X,Data_y,Data_baseline,Data_pids,Data_labels,Data_data_types]
ResearchData = Dict[str, ResearchDataElement]
