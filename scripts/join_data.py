from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.sql import SparkSession

# create Spark context with Spark configuration
conf = SparkConf().setAppName("mortality-es")
sc = SparkContext(conf=conf)
spark = SparkSession(sc)

import utils
import os
import pandas as pd

COUNTRY = 'ES'
INIT_YEAR = 1975
LAST_YEAR = 2019

# Create the output folder if it does not exist
if not os.path.exists("output"):
    os.mkdir("output")

# Write (erase any existing contents) the headers into the file
columns = ['PROVI', 'MUNI', 'MESN', 'ANON', 'SEX', 'MESDEF', 'ANODEF', 'NACION', 'PAISNAC', \
    'LUGNAC', 'PROVNAC', 'MUNNAC', 'PAISNACX', 'LUGRES', 'PROVRES', 'MUNRES', 'PAISRESX', 'ECIV', \
    'OCU', 'ANOSCUM', 'MESCUM', 'DIASCUM', 'TAMAMUNI', 'TAMAMUNN', 'TAMAMUNR', 'TAMAPAISN', \
    'TAMAPAISR', 'TAMAPAISNACION', 'CBAS', 'CRED', 'CPER', 'CINF','NEDU','LUGDEF','RELA']
with open(f"output/mort_{COUNTRY}_{INIT_YEAR}_{LAST_YEAR}.csv", "w") as f:
    f.write(','.join(columns) + '\n')

# Remember to run download_data.sh to download the data
for year in range(INIT_YEAR, LAST_YEAR+1):
    print(f"Processing year {year}")        

    if year < 1999:
        parse_fn = utils.parse_line_less_1998
    elif year < 2009:
        parse_fn = utils.parse_line_less_2008
    elif year < 2015:
        parse_fn = utils.parse_line_less_2015    
    else:
        parse_fn = utils.parse_line_less_2019       

    # Using Spark
    lines = sc.textFile(f'data/DEF{COUNTRY}{year}')
    df = lines.map(parse_fn).toDF().toPandas()
    df.to_csv(f'output/mort_{COUNTRY}_{INIT_YEAR}_{LAST_YEAR}.csv', mode='a', header=False, index=False)