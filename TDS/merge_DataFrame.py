# -------------------------------------------------------------------------------------
# Description:
#             merge data, data_frame_00 and data_frame_01
# 
# author: garyhsieh
# Data: 20200918
# -------------------------------------------------------------------------------------


#import pandas as pd
from pandas import DataFrame, merge

def merge_data_frame(_data_00, _data_01):
    #data_frame_00, data_frame_01 = DataFrame(_data_00, _data_01)
    data_frame_00 = DataFrame(_data_00)
    data_frame_01 = DataFrame(_data_01)

    #merged_data = pd.merge(data_frame_00, data_frame_01)
    merged_data = merge(data_frame_00, data_frame_01)
    
    return merged_data


