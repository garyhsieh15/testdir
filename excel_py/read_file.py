
import pandas as pd



def read_file_xlsx(_path):
    #print("show path:", _path)
    df = pd.read_excel(_path, sheet_name = "工作表2")

    return df

#def read_file_csv(_path):

#def read_file_txt(_path):

def show_data(_data):
    print("show data:", _data)

if __name__ == "__main__":

    #df = pd.read_excel(r"/Volumes/Transcend/testdir/excel_py/EX/ACD019600/data/test.xlsx")
    #print("show df data:", df)

    df = read_file_xlsx(r"/Volumes/Transcend/testdir/excel_py/EX/ACD019600/data/test.xlsx")
    show_data(df)



