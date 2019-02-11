# Online-Trending
*****
## Team Members - Developers
* [Nidhi Gupta](https://github.com/nidhi98gupta)
* [Raksha Rank](https://github.com/RakshaRank)
* [Chirag Podar](https://github.com/ChiragPoddar99)
* [Swapnil Dhimmar](https://github.com/sdhimmar006)
* [Tikam Alma](https://github.com/Tikam02)
* [Amey Ghate](https://github.com/amey-ghate)
* [Shreya Sagar]()
* [Vishwa Seth](https://github.com/Vishwa-Sheth)
## Installation

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
### Instructions For Execution the App.
## Running Locally

First, clone the repository to your local machine:

```
git clone https://github.com/Tikam02/Online-Trending
```


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
pip install -r requirements
```

Apply the migrations:

```bash
python manage.py migrate
```

Apply Make migrations:
```bash
python manage.py makemigration
```


Finally, run the development server:

```bash
python manage.py runserver
```

The site will be available at **127.0.0.1:8000**.


