import config
import utility

df_vin = utility.multi_xls_reader(config.vin_path, config.Cdm2VinSheetName)

# Splitting the rows into multiple based on the field separator ";" of column "Mapping to Physical Columns"
df_vin = utility.row_splitter(df_vin)

# Splitting the "Mapping to physical column" into two columns
# Creating two columns "Vin table" and "Vin Column" based on the value around "."
df_vin[['VIN Table', 'VIN Column']] = (df_vin['Mapping to Physical Columns'].str.replace('.', ' ').
                                       str.extract(r'(.*)\s+([^\s]*)', expand=True))

# The below data frame will only have the selected columns
df_vin = df_vin[["Code", "Loadable", "Mapping Join", "Mapping Selector", "VIN Table", "VIN Column",
                 "Parent.code"]]

# Renaming the column header before returning the data frame
df_vin = df_vin.rename(columns={'Code': 'CDM Column', 'Mapping Join': 'VIN Mapping Join',
                                'Mapping Selector': 'VIN Mapping Selector', 'Parent.code': 'CDM Table'},
                       inplace=False)