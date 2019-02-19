#!/bin/bash

function ask_user() {    

echo -e "Default \e[93mLight yellow"

echo -e "
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
| 0.) Pip install                           |
| 1.) Runserver                             |
| 2.) Migrate                               |
| 3.) Makemigrations                        |
| 4.) Load-Data JSON for Crawler Services   |
| 5.) Crawl Services                        | 
| 6.) Git Fetch and PULL origin             |
| 7.) Git status                            |
| 8.) Git Add and Push Origin   
| 9.) Git Stash            | 
| 10.) Quit                                  |
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#\n"

read -e -p "Select 1: " choice

if [ "$choice" == "0" ]; then

pip install -r requirements.txt


elif [ "$choice" == "1" ]; then

python manage.py runserver

elif [ "$choice" == "2" ]; then

python manage.py migrate

elif [ "$choice" == "3" ]; then

python manage.py makemigration

elif [ "$choice" == "4" ]; then

python manage.py loaddata services.json

elif [ "$choice" == "5" ]; then

function ask_for_services() {

echo -e "Default \e[96mLight cyan"

echo -e "
#-----------------------------------#
| 1.) Reddit                        |
| 2.) Nytimes                       |
| 3.) Github                        |
|-----------------------------------#\n"

read -e -p "Select 1: " choice

if [ "$choice" == "1" ]; then 

python manage.py crawl reddit

elif [ "$choice" == "2" ]; then

python manage.py crawl nytimes

elif [ "$choice" == "3" ]; then

python manage.py crawl github

else 
clear &&  ask_for_services
fi
}
ask_for_services




elif [ "$choice" == "6" ]; then

if git checkout master &&
    git fetch origin master &&
    [ `git rev-list HEAD...origin/master --count` != 0 ] &&
    git merge origin/master
then
    echo 'Updated!'
else
    echo 'Not updated.'
fi



elif [ "$choice" == "7" ]; then

git status


elif [ "$choice" == "8" ]; then

read -p "Commit description: " desc
git add . && \
git add -u && \
git commit -m "$desc" && \
git push origin master

elif [ "$choice" == "9" ]; then 

git stash

elif [ "$choice" == "10" ]; then

    clear && exit 0


else

    echo "Please select 1, 2, or 3." && sleep 3
    clear && ask_user

fi
}

ask_user
