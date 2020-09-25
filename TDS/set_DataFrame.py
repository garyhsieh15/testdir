
import numpy as np
from pandas import DataFrame

def set_data_frame_nan_cell(_data, _item):
    data_frame = DataFrame(_data)

    data_frame[_item] = np.nan
    return data_frame.isnull()

def calc_num_of_nan(_data):
    return _data.sum()
