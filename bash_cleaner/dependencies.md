# Dependencies

> You MUST do the following in order for Bash Cleaner to properly function:

1. Have Python installed 
	
	> Python is required, in order for the .py file to run.

    If On Windows:  
    > You can install the latest "Python 3.11" once again using winget"  
	
    ```sh
    winget install -e --id Python.Python.3.11
    ```
	
    > Follow the default install, but make sure to include Python to PATH.  
    > Once installed, we need to copy where the PATH for python is and let Git know.  
	
	Your Python environment PATH should look similar to this:  
	
    ```
    C:/Program Files/Python311 
    C:/Program Files/Python311/Scripts
    ```
	
2. Link Git

    We need to let Git know the Python PATH.  
    > The export PATH feature is what tells Git where to look.  
	
	
    On the Git Bash terminal enter:
    > Or enter whichever your PATH is..
	
    ```
    echo 'export PATH="$PATH:[C:/Program Files/Python311]:[C:/Program Files/Python311]/Scripts]"' >> ~/.bashrc
    ```
	
3. Refresh Git

    All that's left, is to (refresh) .bashrc file.
	
    ```
    . ~/.bashrc
    ```
	
4. Proceed with BASHER

    Now that all the depencies are out of the way!
    > It's time to get back to setting up the bash_cleaner.py
	* https://github.com/flapjacksauce/learn_Git/blob/main/bash_cleaner/README.md
	
## BASH CLEANER
* https://github.com/flapjacksauce/learn_Git/blob/main/bash_cleaner/bash_cleaner.py