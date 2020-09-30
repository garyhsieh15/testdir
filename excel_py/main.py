
import operator_df





if __name__ == "__main__":
    print("enter excel_py main")

    dic1 = {"name":["gary", "mary", "tom"], "age":[11, 22, 33]}
    df1 = operator_df.create_df(dic1)
    operator_df.info_df(df1)

    print(len(df1.index))    # get index length
    df2 = operator_df.modify_index(df1, ["one", "two", "three"])
    operator_df.info_df(df2)
