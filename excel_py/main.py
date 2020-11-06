
import operator_df
import read_file




if __name__ == "__main__":
    print("enter excel_py main")
    """
    dic1 = {"name":["gary", "mary", "tom"], "age":[11, 22, 33]}
    df1 = operator_df.create_df(dic1)
    operator_df.info_df(df1)

    print(len(df1.index))    # get index length
    df2 = operator_df.modify_index(df1, ["one", "two", "three"])
    operator_df.info_df(df2)
    """

    df = read_file.read_file_xlsx(r"/Volumes/Transcend/testdir/excel_py/EX/ACD019600/data/test.xlsx")
    read_file.show_data(df)

    df1 = operator_df.modify_index(df, ["one", "two", "three", "four"])
    read_file.show_data(df1)
    
    print(df1.columns)
    print(df1.index)

