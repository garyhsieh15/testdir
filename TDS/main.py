
import numpy
import class_ex
import vector_matrix
from scipy.optimize import newton as nt

#    module          class       function           variable
#from class_ex import MyCalClass, show_me_the_money, class_ex_a
from class_ex import show_me_the_money, class_ex_a
from class_ex import MyCalClass
# import vector_matrix.show_info as show_info

import create_DataFrame
import search_data
import del_DataFrame
import merge_DataFrame
import sort_DataFrame
import set_DataFrame
#      package  module
import draw.draw_pic
#    package  module      function
#from draw.draw_pic import draw_x2_func_curve
import calc_newton

# NG
# import draw
# OK
# import draw.draw_pic
# OK
# import draw.draw_pic as draw_pic
# OK 
#from draw.draw_pic import draw_scatter
# OK
#from draw import draw_pic
# OK package  module
#from draw import draw_pic as dc
#    package1  package2     module
from draw.draw_line import draw_color_line


if __name__ == "__main__":
    print("enter main function")
        #print("random.__name__:", numpy.random.__name__)
        #print("random.__package__:", numpy.random.__package__)
        #print("random.__file__:", numpy.random.__file__)

    """
        object00 = MyCalClass(2, 3)
        print(object00.calc_add1(4, 5))
        print(object00.calc_add2())
    """
    print("=======================================================")
    # vector_matrix.show_info()
    print("=======================================================")
    #vector_matrix.create_random()
    print("=======================================================")

    #edit dic
    data = {"ID": [11, 22 ,33, 44, 55, 77, 66],
            "city": ["aa", "bb", "cc", "dd", "ee", "gg", "ff"],
            "name": ["gary", "terry", "tom", "mary", "cindy", "bob", "gary"]}

    data_01 = {"city": ["gg", "hh", "ii", "dd", "ee", "ff"],
            "math": [60, 70, 80, 90, 91, 92],
            "English": [61, 71, 81, 91, 93, 94],
            "chinese": [62, 72, 82, 95, 96, 97]}
    
    # create_DataFrame.show_DataFrame_info(data)
    """  
        column_index = "ID"
        column_data = create_DataFrame.get_column_data(data, column_index)
        print("show column data:", column_data)
        data_frame_t = create_DataFrame.data_frame_transfer(data)
        print("show data frame transfer:\n", data_frame_t)
    """
    """ 
        index = []
        index.append("ID")
        index.append("name")
        multi_column_data = create_DataFrame.get_multi_column_data(data, index)
        print("show multi column data:\n", multi_column_data)
    """
    """
        print("========================================================")
        search_index = "name"
        search_key = []
        search_key.append("gary")
        print(search_data.search_row_data(data, search_index, search_key))
        print(search_data.search_isin(data, search_key))
    """
    """
        column_index = []
        column_index.append("name")
        print(del_DataFrame.del_column_data(data, column_index))
    """
    """ 
        merged_data_frame = merge_DataFrame.merge_data_frame(data, data_01)
        print(merged_data_frame)
        #print(merge_DataFrame.merge_data_frame(data, data_01))
    """
    """    
        print(sort_DataFrame.data_frame_sort_value(data))
    """
    """
        print(set_DataFrame.calc_num_of_nan(set_DataFrame.set_data_frame_nan_cell(data, "name")))
    """
    """ draw pic
        #print("draw.draw_pic.__name__:", dc.__name__)
        #print("draw.draw_pic.__package__:", dc.__package__)
        #print("draw.draw_pic.__file__:", dc.__file__)

        # package  module  function
    """
    #draw.draw_pic.draw_scatter()
    #draw.draw_pic.draw_scatter()
    """
        #draw_scatter()
        #draw_pic.draw_scatter()
        #dc.draw_scatter()
        
        #draw_color_line.draw_color()
    """
    #draw.draw_pic.draw_continue_curve(100)

    #print(nt(calc_newton.x2_function,0))
    #draw.draw_pic.draw_x2_func_curve()
    #draw_x2_func_curve()
