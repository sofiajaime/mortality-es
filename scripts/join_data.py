import pandas as pd

# STEP 1: 
# In order to solve the memory issues of joining all the years in one DataFrame,
# Save from 1759 to 2000 first and then from 2001 to 2019.

COUNTRY = 'ES'
INIT_YEAR = 1975
LAST_YEAR = 2000

joined = None
for year in range(INIT_YEAR, LAST_YEAR+1):
    print(f"Loading year {year}")
    if joined is None:
        joined = pd.read_stata(f"output/mort_{COUNTRY}_{year}.dta", convert_categoricals=False)
    else:
        joined = pd.concat([joined, pd.read_stata(f"output/mort_{COUNTRY}_{year}.dta", convert_categoricals=False)])

print(joined.shape)
print(joined.head())

print(f"Saving output to file output/mort_{COUNTRY}_{INIT_YEAR}_{LAST_YEAR}.dta")
joined.to_stata(f"output/mort_{COUNTRY}_{INIT_YEAR}_{LAST_YEAR}.dta", write_index = False)

# STEP 2:
# Join the 2 generated dataframes

# COUNTRY = 'ES'

# joined = None

# print(f"Loading output/mort_{COUNTRY}_1975_2000.dta")
# joined = pd.read_stata(f"output/mort_{COUNTRY}_1975_2000.dta", convert_categoricals=False)

# print(f"Loading output/mort_{COUNTRY}_2001_2019.dta")
# joined = pd.concat([joined, pd.read_stata(f"output/mort_{COUNTRY}_2001_2019.dta", convert_categoricals=False)])

# print(joined.shape)
# print(joined.head())

# print(f"Saving output to file output/mort_{COUNTRY}_1975_2019.dta")
# joined.to_stata(f"output/mort_{COUNTRY}_1975_2019.dta", write_index = False)