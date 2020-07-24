### initialize a git repository in a folder
* In the folder right click->open git bash here
* use command 'git init'
* use command 'git status' to see the status of files
* use command 'git add .' to add all untracked files and changes for staging to get committed
* use command git commit -am 'commit comment' to commit the changes of your code to git 

### pushing code to remote git repositories like GitHub
* Create an account in sites like GitHub, Bitbucket
* Create a repository in your account
* In the folder right click and select 'Git bash here' to open git command prompt
* add remote repo url to local git using the command ```git remote add origin <your_repo_url>```
* Pull remote code to local git folder using the command ```git pull origin master```
For unrelated histories issue use command ```git pull origin master --allow-unrelated-histories```
* Push code to remote repository using the command ```git push origin master```