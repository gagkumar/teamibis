import config
import utility

df = utility.multi_xls_reader(config.cdm_path, config.Source2CdmSheet1, config.Source2CdmSheet2)
df_new = utility.refactor_df(df)

# Selecting only the attributes of the table and ignoring other rows
df_cdm = df_new[df_new["Target Column Type"].notnull() &
                (df_new["Target Column Type"] != "TBC")].reset_index(drop="True")

# The below data frame will only have the selected columns
df_cdm = df_cdm[["New Table Name", "Target Column Name", "Data Type", "Source", "CDM Table"]]

# Renaming the column header before returning the data frame
df_cdm = df_cdm.rename(columns={'Target Column Name': 'CDM Column', 'Data Type': 'CDM Data Type',
                                "Source": "Source Attribute", "New Table Name": "Source Table"}, inplace=False)





