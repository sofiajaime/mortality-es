import pandas as pd
pd.options.display.max_columns = None
import numpy as np
from tqdm import tqdm
import utils
import os

COUNTRY = 'ES'
INIT_YEAR = 2019
LAST_YEAR = 2020

# Define columns
columns = ['PROVI', 'MUNI', 'MESN', 'ANON', 'SEX', 'MESDEF', 'ANODEF', 'NACION', 'PAISNAC', 'LUGNAC', 'PROVNAC', 'MUNNAC', 'PAISNACX', 'LUGRES', 'PROVRES', 'MUNRES', 'PAISRESX', 'ECIV', 'OCU', 'ANOSCUM', 'MESCUM', 'DIASCUM', 'TAMAMUNI', 'TAMAMUNN', 'TAMAMUNR', 'TAMAPAISN', 'TAMAPAISR', 'TAMAPAISNACION', 'CBAS', 'CRED', 'CPER', 'CINF']

if not os.path.exists("output"):
    os.mkdir("output")

# Remember to run download_data.sh to download the data
for year in range(INIT_YEAR, LAST_YEAR):
    print(f"Processing year {year}")

    if year < 1999:
        parse_fn = utils.parse_line_less_1998
    elif year < 2009:
        parse_fn = utils.parse_line_less_2008
    else:
        parse_fn = utils.parse_line_less_2019       

    df = pd.read_csv(f'data/DEF{COUNTRY}{year}', names=["raw"])
    df = df.merge(df.raw.apply(lambda s: pd.Series({columns[i]:el for i,el in enumerate(parse_fn(s))})), left_index=True, right_index=True)
    df = df.drop(['raw'], axis=1)

    df.to_stata(f"output/mort_{COUNTRY}_{year}.dta", write_index = False)