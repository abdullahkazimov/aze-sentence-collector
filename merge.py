import pandas as pd
from os import sys
import subprocess

subprocess.run(['python3', './update.py'], check=True)

# Read the main DataFrame from 'prod.csv'
df = pd.read_csv('./prod.csv')

# Read the 'unchecked.csv' file and get the list of files
unchecked = pd.read_csv('./unchecked.csv')['files'].values

# Check if there are unchecked files
if len(unchecked) == 0:
    print("Database is up-to-date.")
    sys.exit()

# Get the first unchecked file
file = unchecked[0]
for file in unchecked:  
    subprocess.run(['python3', './update.py'], check=True)
    # Read the main DataFrame from 'prod.csv'
    df = pd.read_csv('./prod.csv')
    # Read the sentences from the file and convert to a list
    f = pd.read_csv(f'./export/{file}')
    new = list(f['sentences'])
    
    # Get the existing sentences from the main DataFrame
    sentences = list(df['sentences'].values)
    
    # Add new sentences to the existing list
    for s in new:
        if s not in sentences:
            sentences.append(s)
    
    # Concatenate the main DataFrame with the new sentences
    df = pd.concat([df, pd.DataFrame({"sentences": sentences})], ignore_index=True)
    
    # Keep only the 'sentences' column
    df = df[['sentences']]
    
    # Remove duplicate rows
    df = df.drop_duplicates()
    
    # Save the updated main DataFrame to 'prod.csv'
    df.to_csv('./prod.csv', index=False)
    
    # Read the 'checked.csv' file
    df = pd.read_csv('./checked.csv')
    
    # Add the current file to the 'checked' list
    df = pd.concat([df, pd.DataFrame({"files": [file]})], ignore_index=True)
    
    # Keep only the 'files' column
    df = df[['files']]
    
    # Remove duplicate rows
    df = df.drop_duplicates()
    
    # Save the updated 'checked' DataFrame to 'checked.csv'
    df.to_csv('./checked.csv', index=False)
    
    # Read the 'unchecked.csv' file
    df = pd.read_csv('./unchecked.csv')
    
    # Remove the current file from the 'unchecked' list
    tmp = set(df['files'].values) - {file}
    
    # Append the updated 'unchecked' list to the DataFrame
    df = pd.concat([df, pd.DataFrame({'files': list(tmp)})], ignore_index=True)
    
    # Keep only the 'files' column
    df = df[['files']]
    
    # Remove duplicate rows
    df = df.drop_duplicates()
    
    # Save the updated 'unchecked' DataFrame to 'unchecked.csv'
    df.to_csv('./unchecked.csv', index=False)


subprocess.run(['python3', './update.py'], check=True)
