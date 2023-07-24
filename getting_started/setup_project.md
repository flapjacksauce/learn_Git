# Creating Our First Repository 

The first choice you make when starting to work with Git is either clone an existing remote source code repository or create your own new local repository to publish. In this brief example we will will be creating our own from scratch so you can get a taste of what's to come. 

> We began by creating our very first repo in https://github.com/flapjacksauce/learn_Git/blob/main/getting_started/setting_up_git.md which is closer related to using a basic web layout you're probably familar with, buttons, icons, bells and wistles. There are multiple ways to make pull requests and push updates, for now we will stick to the easier easier approach.

1. Navigate to a project folder you wish to store your repository. 

    If using Windows: 

    > Once in the project folder on your desktop that you have just created, it will be the home for all of your project code and individual depencies to live in.

    Let's create our first file:

    > Press "Windows" + "R" keys at the same time to start RUN  
    > Once in RUN type in "cmd" and press enter.  
    > Open CMD Prompt and CD into project folder directory  

    ```sh
    CD %USERPROFILE%/Desktop/Project
    ```

2. Initialize Repository

    > (master)

    ```sh
    git init
    ```

    > Here we are running a slightly more advanced command and created a branch off of the main.  
    > Feel free to name your branches how you please. Typically, main is what most users default to.

    ```sh
    git branch -M main
    ```

3. Create a README.md

    > GitHubs entire display is formated in .md files known as markdown, you will be getting very familliar with these shortly. But for now, just a Title will do. 

    ```sh
    echo "# My First Repo" > README.md
    ```

    We called echo to print the string "# My First Repo" all markdown titles start with a (#).

4. Checking status

    > Notice how the README.md file is highligihed red? Git has been tracking all your changes!
    > When you called echo and output the title to > README.md Git tracked that progress.
    > (This command is just to track status, it is not needed for final push)

    ```sh
    git status
    ```

5. Add Changes

    > This command will add all your changes to be staged for commitment.
    > This command is neccesary to tell Git what which changes we wish to finalize. Afterall, we may have many files and we wish to only stage 2 of them, we can call the file by its nam and extension.

    ```sh
    git add README.md
    ```
6. Commit Changes.

    > A commit is basically reassuring that this is the actual file(s) you would like to post.
    > You may have has many changes on your working branch but to cherry pick which files we would like to upload at a given time, we can use the (add) command in our previous step.
    > Once commited, the working branch is clear of the file(s) you selected and ready to push. 

    Making the changes final and ready to upload
    ```sh
    git commit origin main
    ```

7. Create a Remote Connection

    > This step is vital to tell Git where to go from your local repository on your machine.

    Creating the repo is one step but now we have to tell git where we are pushing to.
    ```sh
    git remote add origin https://github.com/yourAccount/yourRepo.git
    ```

    Check remote connection setup with the command

    ```sh
    git remote -v
    ```
    > Your output should say (fetch) (pull) after your repository URL, is so, your all set to make your first official push to GitHub!
 

8. Push to Github

    You are now ready to make a push to Github
    ```sh
    git push origin main
    ```
	
	Loging in with Git 
	> Git will require not your GitHub passphrase, but a PAT what is known as a "Personal Access Token"
	Refer to:  https://github.com/flapjacksauce/learn_Git/blob/main/getting_started/personal_access_token.md

9. Check out your NEW REPO

    > Navigate to your new GitHub Repo web page , you should see a README.md file and the title displayed on the GitHub Repository.

    If pushed succesfully your output should be similar to this:
    ```
    Enumerating objects: 5, done.
    Counting objects: 100% (5/5), done.
    Delta compression using up to 8 threads
    Compressing objects: 100% (3/3), done.
    Writing objects: 100% (4/4), 2.43 KiB | 2.43 MiB/s, done.
    Total 4 (delta 0), reused 0 (delta 0), pack-reused 0
    To https://github.com/yourAccount/yourRepo.git
    6380228..81a9857  main -> main
    ```

10. Congrats

    You have officially made your first commit to GitHub
    > We just scratched the surface, so we will be diving deeper into the next section, where we will create a validation signature.

## References

* https://github.com/flapjacksauce/learn_Git