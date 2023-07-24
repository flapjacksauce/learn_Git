# Patch 

Bug fixes, optimization, and quality of life features documentation.

> Most of these patch notes will orient around quality of life

# v1.0.1

1. Initial Release
	
    Script was puplished July 22, 2023
    * All included features function as intended.
    * Documentation released.  
	
# v1.0.2

2. Fixed issues

    Some human errors that I forgot to include from my test enviornment
    * Output was not sorting alpha-numerically  
    * Removed value output duplicates to clean-up the users terminal output  
	
    Outdated: Removed value output:
	
    ```
    Total values: 122

    Removed 4 values: ['nano ~/.bashrc', 'git status', 'git push', 'git push,' ]
    ```
	
    Updated: Removed values output:
	
    ```
    Total values: 122

    Removed 4 values: ['nano ~/.bashrc', 'git status', 'git push' ]
    ```  
	
    The output has simply been shortened to show only one of each command in the bash history
	
    > This approach lightens up the terminal screen, especially if you have a lengthy bash history.  
    > It will not show how many of which individual command was removed.
    > Although, the output count will still give an accurate answer of the total removed.
	
	
## Bash Cleaner

* https://github.com/flapjacksauce/learn_Git/blob/main/bash_cleaner/bash_cleaner.py

	
## Comments

	Any bugs or issues found please do inform me and I will look into the situation.
	
	> Hope this serves you well,
	
	flapjacksauce