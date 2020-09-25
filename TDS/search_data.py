
from pandas import DataFrame

def search_row_data(_data, _search_index, _search_key):
    data_frame = DataFrame(_data)

    return data_frame[data_frame[_search_index].isin(_search_key)]
    #return data_frame[_search_index].isin(_search_key)

def search_isin(_data, _search_key):
    data_frame = DataFrame(_data)

    return data_frame.isin(_search_key)
