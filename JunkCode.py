# Utility
name = os.path.splitext(WorkingFile)[0]


# VID Mapping
# Adding a new column "VID Table" and deriving the value from the "File Name"
df_vid['VID Table'] = df_vid['File Name'].str.split('- ').str[1]
# Formatting the value and replacing the spaces with the "_"
df_vid['VID Table'] = df_vid['VID Table'].replace({'Dim': 'D', 'Fact': 'F', ' ': '_'}, regex=True)

#######################

