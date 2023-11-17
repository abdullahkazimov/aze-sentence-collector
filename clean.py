from config import allowed_pattern, min_word_limit, max_word_limit, fname, lname
from datetime import datetime
from config import install, create_folder
import re
import sys


install('pandas')
import pandas as pd

def is_valid(sentence, pattern=allowed_pattern):
    matches = re.findall(pattern, sentence)
    matches = ''.join(matches)
    if 'w' in matches or 'W' in matches:
        matches = ''
    return len(matches) == len(sentence)

# Access command-line arguments
# sys.argv[0] is the script name
# sys.argv[1:] contains the arguments
args = sys.argv[1:]

# Check if there are any arguments
if not args:
    file_name = input('file name (with extension): ')
    df = pd.read_csv(f'./data/{file_name}')
    print('[INFO] Upload: Successful')
    text_column = input('sentence column: ')
    sentences = list(df[text_column])
    print('[INFO] Fetch: Successful')
    print()
else:
    file_name = args[0]
    df = pd.read_csv(f'./data/{file_name}')
    print('[INFO] Upload: Successful')
    text_column = args[1]
    sentences = list(df[text_column])
    print('[INFO] Fetch: Successful')
    print()
        


print('[INFO] Deleting invalid sentences...')
# delete invalid sentences
tmp = []
for sentence in sentences:
    if is_valid(sentence):
        tmp.append(sentence)
sentences = tmp

print('[INFO] Trimming and Splitting...')
tmp = set()
for sentence in sentences:
    sentence = sentence.strip()
    tmp.add(sentence)
sentences = list(tmp)

print('[INFO] Applying word limitation...')
tmp = []
for sentence in sentences:
    current = sentence
    sentence = sentence.split(' ')
    if len(sentence) >= min_word_limit and len(sentence) <= max_word_limit:
        tmp.append(current)
sentences = tmp

current_time = datetime.now()
formatted_time = current_time.strftime("%S_%M_%H_%d_%m_%Y")

print('[INFO] Saving file...')
df = pd.DataFrame({"sentences": sentences})

file_name = f'dev_{fname}_{lname}_{formatted_time}.csv'

create_folder('./export/')
df = df[['sentences']]
df = df.drop_duplicates()
df.to_csv(f'./export/{file_name}')

print(f'[SUCCESS] File saved as {file_name}')