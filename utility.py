import pandas as pd
import os

"""Utility to load multiple excel sheet """


def multi_xls_reader(filepath , sheet1, sheet2=None):
    # Not using glob has accessing xlsx and retrieving data from specific spreadsheet is easier with listdir
    # reading all the files from CDM directory
    filenames = os.listdir(filepath)
    final_df = []
    for WorkingFile in filenames:
        print("Loading file : ", WorkingFile)
        xlsx_file = pd.ExcelFile(filepath + WorkingFile)
        df = xlsx_file.parse(sheet1)
        # This data frame will be used to derive the table name for source and VID
        df_tbl = xlsx_file.parse(sheet2)
        # Removing the all null records from the data frame
        df = df.dropna(how="all")
        # Adding New Table name as a new column, will be used to derive Conformed Source Table/ vid table from sheet2
        if filepath[-4:-1] == "CDM":
            df["New Table Name"] = df_tbl.iloc[0][0]
            print("Source Table Name : ", df_tbl.iloc[0][0])
        elif filepath[-4:-1] == "VID":
            df["New Table Name"] = df_tbl.iloc[-2][1]
            print("VID Table Name : ", df_tbl.iloc[-2][1])
        final_df.append(df)

    # converting from list to data frame and also ignoring the indexes
    final_df = pd.concat(final_df, ignore_index=True)
    return final_df

"""Utility to refactor the Source to CDM data lineage"""


def refactor_df(dataframe):
    df = dataframe
    # getting the row which has the header i.e. C_ table
    df_startswithc = df[df["Target Column Name"].str.contains("^C_")]
    # List containing index position and the C_ table name as the attribute
    c_ind_pos = [(index, rows[0]) for index, rows in df_startswithc.iterrows()]
    # Adding a new column "Target Table" in the data frame and aligning with the columns
    for i in c_ind_pos:
        df.loc[df.index > i[0], "CDM Table"] = i[1]
    return df

"""Utility to create multiple rows based on the column value separator"""


def row_splitter(df):
    # Expanding the column value into rows based on the field separator ";"
    s = df["Mapping to Physical Columns"].str.split(';', expand=True).stack()
    # Getting the level value (position) of the entire rows (new and old row will have the same value)
    i = s.index.get_level_values(0)
    # Copying all the fields into df2 from df + it will have extra rows with the repeated values
    df2 = df.loc[i].copy()
    # Now finally copy the rows against the column
    df2["Mapping to Physical Columns"] = s.values
    return df2





