
from collections import defaultdict
import re

# DICTIONARY TO COLLECT LOGS AND COUNT 

logs_count = defaultdict(lambda : {
    "messages": {},    #selected as dictionary
    "total": 0    
    })
# seen_messages = defaultdict(set)

pattern = r"\x1b\[[0-9;]*m" 
# with open("app.log", "r") as file:
#     for line in file:
#         # print(line.splitlines()[-1].rsplit("-",2))   #If rsplit is specified, the list will have the maximum of rsplit+1 items
        
#         # clean the line which have special characters with re.sub which replace the pattern with nothing in the sentence
#         clean_line = re.sub(pattern,"",line).strip()

#         # if the line is empty then continue
#         if not clean_line:
#             continue
        
#         # now with the clean line split the characters with the - so that it can come into list[]
#         lines_in_list = clean_line.split(" - ")

#         # logs level
#         level = lines_in_list[2]

#         # logs message
#         message = lines_in_list[3].split("(")[0].strip()
#         # print(message)




#second method with the rsplit

with open("app.log", "r") as file2:
    for line in file2:

        clean_line = re.sub(pattern,"",line).strip()  # cleans pattern from lin

        if not clean_line:    # clean blank spcases or empty sentences
            continue

        lines_in_list = clean_line.rsplit(" - ",2)  #splt from right with only 3 entries

        level = lines_in_list[1]   #info warning critical
        
        message = lines_in_list[2].split("(")[0].strip()    #message of logs\

        logs_count[level]["total"]+=1

        if message not in logs_count[level]["messages"].values():
            count = len(logs_count[level]["messages"])+1
            logs_count[level]["messages"][count]=message

# print(logs_count.values())
for level, inner in logs_count.items():
    for key, value in inner.items():
        print(level, key, value)



# file typo:  r = read   w = overwrite existing file  a = add something to file    x = to create file

# re.sub for separting out words and split for spliitting the sentence and strip  for clear out blank spaces
# rsplit for splitting the sentence from the right