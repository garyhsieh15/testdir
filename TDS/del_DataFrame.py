
from pandas import DataFrame

def del_column_data(_data, _column_index):
    data_frame = DataFrame(_data)

    return data_frame.drop(_column_index, axis = 1)
