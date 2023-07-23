# -- BAHSER -- 
# History Cleaner v1.0.1

import os

bash_history = os.path.expanduser("~/.bash_history")
with open(bash_history, "r") as textFile:
    history = textFile.readlines()
    
    n = 0
    for x in history:
        n += 1

values = list(dict.fromkeys(history))

i = 0
for x in values:
    i += 1
        
    removed = n - i

removed_history = []

for d in range(0, len(history)):
    for j in range(d+1, len(history)):
        if(history[d] == history[j]):
            removed_history.append(history[j].strip("\n"))

# Prints History after duplicates removed
# To turn On -- DELETE the following 2 sets of (""")

"""
print("\nHistory:\n")
t = 0
for v in values:
    t += 1
    print(f"{t} -- {v}")
"""  

print(f"\nTotal values: {i}\n")
print(f"Removed {removed} values: {removed_history}")

with open(bash_history, "w") as f:
    f.writelines(values)