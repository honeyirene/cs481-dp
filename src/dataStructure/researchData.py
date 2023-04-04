import numpy
from typing import Dict, Union, List

Data_X = List[Dict[str, Union[List[int], List[numpy.int64]]]]
Data_y = numpy.ndarray
Data_baseline = Dict[str, any]
Data_pids = numpy.ndarray
Data_labels = numpy.ndarray
Data_data_types = numpy.ndarray

ResearchDataElement = Union[Data_X,Data_y,Data_baseline,Data_pids,Data_labels,Data_data_types]
ResearchData = Dict[str, ResearchDataElement]

# keys = 'X', 'y', 'baseline', 'pids', 'labels', 'data_types'
