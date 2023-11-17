import subprocess
import sys

args = sys.argv[1:]
file_name = args[0]
column = args[1]

subprocess.run(['python3', 'clean.py', file_name, column])
subprocess.run(['python3', 'merge.py'])