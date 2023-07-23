# BASH CLEANER

import time, os

system = (os.path.expanduser('~'))
user = system.replace('\\', '/')

# Cleans every 4 HOURS
def clean(t=14400):

    # Loop
    while True:

        # GRABS URLS FROM TEXTFILE
        global values
        with open (f'{user}/.bash_history') as textFile:
            file = textFile.read().split('\n')
        textFile.close()

        file.remove("")

        # ITERATES NUMBER of individual lines from text file
        n = 0
        for x in file:    
            n += 1

        # ITERATES NUMBER of individual lines from text file and remove duplicates
        i = 0
        values = [*set(file)]
        for x in values:    
            i += 1
            
        removed = n - i

        print(f"Commands: \n {values}\n")
        print(f"Total values: {i}\n")
        print(f"Removed values: {removed}\n")

        with open('C:/Users/npalu/.bash_history', 'w') as f:
            for line in values:
                f.write(line + '\n')    

        time.sleep(t)

clean()
