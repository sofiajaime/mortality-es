import pandas as pd
pd.options.display.max_columns = None
import numpy as np
from tqdm import tqdm
import utils

COUNTRY = 'ES'
INIT_YEAR = 1975
LAST_YEAR = 2019

# Create dataframe object
df = pd.DataFrame(columns=['PROVI', 'MUNI', 'MESN', 'ANON', 'SEX', 'MESDEF', 'ANODEF', 'NACION', 'PAISNAC', 'LUGNAC', 'PROVNAC', 'MUNNAC', 'PAISNACX', 'LUGRES', 'PROVRES', 'MUNRES', 'PAISRESX', 'ECIV', 'OCU', 'ANOSCUM', 'MESCUM', 'DIASCUM', 'TAMAMUNI', 'TAMAMUNN', 'TAMAMUNR', 'TAMAPAISN', 'TAMAPAISR', 'TAMAPAISNACION', 'CBAS', 'CRED', 'CPER', 'CINF'])

# Remember to run download_data.sh to download the data
years = range(INIT_YEAR, LAST_YEAR)
# Read the files line by line
for year in years:
    print(f"Processing year {year}")
    if year < 1999:
        parse_fn = utils.parse_line_less_1998
    elif year < 2009:
        parse_fn = utils.parse_line_less_2008
    else:
        parse_fn = utils.parse_line_less_2019       

    with open(f'data/DEF{COUNTRY}{year}') as file:
        lines = file.readlines()
    
    for line in tqdm(lines[:1]):
        df.loc[len(df)] = parse_fn(line)

df.to_stata(f"mort_{COUNTRY}_{INIT_YEAR}_{LAST_YEAR}.dta", write_index = False)