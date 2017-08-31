import config
import utility

df_new = utility.multi_xls_reader(config.vid_path, config.Cdm2VidSheet1, config.Cdm2VidSheet2)

# Selecting only the attributes of the table and ignoring other rows
df_vid = df_new[df_new["Attribute Type"].notnull()].reset_index(drop="True")

# Creating two columns "CDM table name" and "CDM Column name" based on the value around "."
df_vid[['CDM Table', 'CDM Column']] = (df_vid['Source'].str.replace('.', ' ').
                                       str.extract(r'(.*)\s+([^\s]*)', expand=True))

# The below data frame will only have the selected columns
df_vid = df_vid[["Target Column Name", "Data Type", "Join Condition", "New Table Name", "CDM Table", "CDM Column"]]

# Renaming the column header before returning the data frame
df_vid = df_vid.rename(columns={'Target Column Name': 'VID Column', 'Join Condition': 'VID Join Condition',
                                'Data Type': 'VID Data Type', 'New Table Name': 'VID Table'},
                       inplace=False)

