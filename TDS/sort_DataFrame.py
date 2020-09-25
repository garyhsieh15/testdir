
from pandas import DataFrame

def data_frame_sort_value(_data):
    data_frame = DataFrame(_data)

    return data_frame.ID.sort_values()
