import pandas as pd
from os import sys
from config import list_files

files = list_files('./export/')
checked = pd.read_csv('./checked.csv')
df = pd.read_csv('./unchecked.csv')

tmp = []
for file in files:
    if file not in checked['files'].values:
        tmp.append(file)

files = tmp
if len(files) == 0:
    print("Database is up-to-date.")
    sys.exit()
df = pd.DataFrame({'files': files})
df = df[['files']]
df = df.drop_duplicates()
print("Total unchecked files: " + str(len(df)))
print(df['files'])
df.to_csv('./unchecked.csv')