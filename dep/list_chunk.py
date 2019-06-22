import re
from pathlib import Path


#https://www.geeksforgeeks.org/break-list-chunks-size-n-python/

# Yield successive n-sized
# chunks from l.
def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]



#FORM: Term, Definition
#mycology_pattern = re.compile(r"(^[A-Z]{3,} [A-Z]{3,}\(?S?\)?|^[A-Z]{3,})(.*$)?", re.MULTILINE)

#FORM: Definition
mycology_pattern = re.compile(r"(  .*$)", re.MULTILINE)

bir = Path("C:/Users/user/workspace/inno_extract/commonappdata/MatchMaker/bir.txt")
data_file = open(bir)
data_contents = data_file.read()
matches = re.findall(mycology_pattern, data_contents)

 # How many elements each list should have
n = 14

x = list(divide_chunks(matches, n))
#print(x)
