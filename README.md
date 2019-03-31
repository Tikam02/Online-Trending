# Online-Trending - Apex
*****
### Instructions For Execution the App.
## Running Locally

First, clone the repository to your local machine:

```
git clone https://github.com/Tikam02/Online-Trending
```
Make sure to add your username and password because this is private Repository and You're collaborator.

Go To the Online-Trending Folder
```bash
cd Online-Trending
```
Activate Virtual Environment
```bash
source env/bin/activate
```

Install the requirements:

```bash
pip3 install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Apply Make migrations:
```bash
python manage.py makemigration
```

Load the API Services that is stored in services.json,so that it will be loaded to the database.

```
python manage.py loaddata services.json
```

then Crawl the services:
```
python manage.py crawl reddit
```
You can pass multiple services at once:

```
python manage.py crawl reddit hn nytimes
```

Finally, run the development server:

```bash
python manage.py runserver
```

To run the crawler
```
python manage.py crawl reddit
```


The site will be available at **127.0.0.1:8000**.

***** 
# Web Pages Links
```
127.0.0.1:8000/login  ----->>>> Login Page
127.0.0.1:8000/signup ---->>>> Sign Up Page
127.0.0.1:8000/home   ---->>>> Home Page
127.0.0.1:8000/about  ---->>>> About Page
127.0.0.1:8000/status  ---->>>> Status of Crawler and Server
127.0.0.1:8000/privacy ---->>>>
127.0.0.1:8000/terms ---->>>> 
127.0.0.1:8000/logout ---->>>> 

```
****** 
### Developers Guide To Contribute
#### To create a branch from Terminal
```
    $ git fetch && git checkout <feature>

    Make your changes locally and then add, commit, and push your changes to the <feature> branch:
    $ git add .
    $ git commit -m "adding a change from the dev"
    $ git push origin dev
```
 

To create a branch locally

You can create a branch locally as long as you have a cloned version of the repo.
```
    From your terminal window, list the branches on your repository.
    $ git branch
    dev
    *master

    This output indicates there is a single branch, the master and the asterisk indicates it is currently active.
    
    Create a new feature branch in the repository
    $ git branch dev

    Switch to the feature branch to work on it.
    $ git checkout dev

    You can list the branches again with the git branch command.

    Commit the change to the feature branch:
    $ git add .
    $ git commit -m "adding a change from the feature branch"

    Switch back to the master branch.
    $ git checkout master
    
    Push the feature branch to Bitbucket:
    $ git push origin dev
```

*****
###How to install Virtual Environments
### Installing virtualenv
* On Mac and Linux:
```
python3 -m pip install --user virtualenv
```
* On windows:
```
py -m pip install --user virtualenv
```


### Creating Virtual Environment
* On Mac and Linux:
```
python3 -m virtualenv env
```
* On windows:
```
py -m virtualenv env
```
### Activating a virtualenv
* On Mac and Linux:
```
source env/bin/activate
```
* On Windows:
```
.\env\Scripts\activate
```
******
## Team Members - Developers
* [Nidhi Gupta](https://github.com/nidhi98gupta)
* [Raksha Rank](https://github.com/RakshaRank)
* [Chirag Podar](https://github.com/ChiragPoddar99)
* [Swapnil Dhimmar](https://github.com/sdhimmar006)
* [Tikam Alma](https://github.com/Tikam02)
* [Amey Ghate](https://github.com/amey-ghate)
* [Shreya Sagar](https://github.com/shreya1706) 
* [Vishwa Seth](https://github.com/Vishwa-Sheth)
******


    
