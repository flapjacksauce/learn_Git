# Setting Up Bash Cleaner

To start we need to install Bash Cleaner into our Git directory  

> We will start by running a few CMD lines   

# How to Install 
	
    The easy method:
    > Once you have your copy of Bash Cleaner by pulling this repo   
    > Store the bash_cleaner.py in the Git directory path  
    > C:\Program Files\Git
	
    The more complex method:
    > Alternatively you can create a system PATH vairable pointing it wherever script is located.

# BASH Prompt 

1. Creating Alias

    ```sh
	echo 'alias clean="python bash_cleaner.py"' >> ~/.bashrc
	```  
	
	If you get a access denied error, try this:
	
	```sh
	nano ~/.bashrc
	```
	Enther in this line, save and close .bashrc
	
	```sh
	alias clean="python bash_cleaner.py"
	```
	
	
	Let's add another alias, this will allow our script to update in real time:
	
    ```sh
	echo 'export PROMPT_COMMAND="history -a;history -c;history -r"' >> ~/.bashrc
	```  
	
	If you get a access denied error, try this:
	
	```sh
	nano ~/.bashrc
	```
	Enther in this line, save and close .bashrc
	
	```sh
	export PROMPT_COMMAND="history -a;history -c;history -r"
	```
	
	Now that you successfully created the alias shortcuts, let's update Git so it knows where to look:
	> What this command does is simply (refresh) the .bashrc file
    > Once this command is run our custom aliases will be activated for each new Git session we open!  

    ```sh
    . ~/.bashrc
    ```
	
	That's it, now let's try out our new Bash Cleaner!
	
	```sh
	clean
	```

   If installed and no issues you should see an output similar to this:  

    ```
    Total values: 122

    Removed 4 values: ['nano ~/.bashrc', 'git status', 'git push', 'git push,' ]
    ```
	
# Uses
    * Your bash will always update in real time  
    * Never Have any duplicates  
    * Cleans and organizes alpha-numerically
    * Stores all current entries unsorted until "clean" has been ran

# Output

2. Output History

    If you wish to have verbose History output.  
    > In the script there is a commented section    
    > Removing the commented out portion will activate verbose output  
    * Default (off)  
    * Verbose History output  (listed by index)
	> (may be a lengthy list depending on your bash command history)    

## Bash Cleaner

* https://github.com/flapjacksauce/learn_Git/blob/main/bash_cleaner/bash_cleaner.py

	
## Comments

	Any bugs or issues found please do inform me and I will look into the situation.
	
	> Hope this serves you well,
	
	flapjacksauce