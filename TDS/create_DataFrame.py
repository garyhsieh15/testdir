
from pandas import DataFrame

def show_DataFrame_info(_data):
    print(DataFrame(_data))

def get_column_data(_data, _column_index):
    data_frame = DataFrame(_data)

    return data_frame[_column_index]

def data_frame_transfer(_data):
    data_frame = DataFrame(_data)

    return data_frame.T

def get_multi_column_data(_data, _index):
    data_frame = DataFrame(_data)

    return data_frame[_index]
