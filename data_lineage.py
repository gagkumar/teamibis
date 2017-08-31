import pandas as pd
import source2cdm
import cdm2vin
import cdm2vid

# Joining Source to cdm and CDM to VIN data frames and join type is inner
df = pd.merge(source2cdm.df_cdm, cdm2vin.df_vin, how='inner', on=["CDM Table", "CDM Column"])

# Joining the combined data frame with the VID data frames and join type as "left"
df_final = pd.merge(df, cdm2vid.df_vid, how='left', on=["CDM Table", "CDM Column"])

print(df_final)