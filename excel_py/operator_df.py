
import pandas as pd




def create_df(_data):
    return pd.DataFrame(_data)

def modify_index(_data, _index):
    _data.index = _index
    return _data

def info_df(_data):
    print("info_df:\n", _data)
