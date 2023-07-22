# Setting Up Git 

To start we need to install Git in order to upload to GitHub  

> We will start by running a few CMD lines   

# How to Install 

    > On a windows machine you can install Git by opening a new cmd terminal  
    > Once terminal window is opened enter the following command:  

# CMD Prompt 

1. Install Git

    ```sh
	winget install -e --id Git.Git
	```  
	
	If you do not have winget, it will ask you if you wish to install; select yes.  Winget is a very helpful package downloader similar to how Git works, instead its focus is primarily installing, updating, and managing programs via the CMD Promt.  
    > (This will install Git and all it's neccesary files to operate without the need of navigating to the webpage and installing the installer)
    > This will check version if installed properly  

    ```sh
    git -v
    ```

   If installed and no issues you should see an output similar to this:  

    ```
    git version 2.41.0.windows.2
    ```

    > On a Mac OS machine (null)  
    > On a Linux machine (null)  

# Setting up GitHub

2. Creating a GitHub account

    If you do not have a GitHub account, then after creating your new account and are finished setting up your profile, navigate to my repositories and click "NEW".  
    > Give your new repository a memorable name  
    > Select privacy (Public or Private)  
    * (Public = Anyone on the internet can see this repository.  You choose who can commit.)  
    * (Private = You choose who can see and commit to this repository.)  

    Skip these 3 steps for now
    * Decide whether to have GitHub include a README file (which basically includes just the repository title), or upload your own (more on README: whats_README.txt)  
    * Decide whther to add .gitignore file (more on .gitignore: whats_gitignore.txt)  
    * Choose which license to include (more on licensing: choose_license.txt)  

    Congrats!
    > Once finished setting up repository, click "Create Repository"  
    > (You have just made your first GitHub repo! Although, it's a little empty, so let's go ahead and add some files.)  
	
## References

* https://github.com/flapjacksauce/learn_Git/getting_started/setting_up_git.md