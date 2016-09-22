# Tornado Template

## Setup
Make sure you have ```virtualenv``` and ```autoenv``` installed.

### Install Locally

```
git clone <url> <new-app-name>
cd new-app-name

echo "source venv/bin/activate" > .env

# create virtual environment
virtualenv venv 

# move out of directory and back in to activate the autoenv environment
cd ..
cd new-app-name

# install dependencies
pip install -r requirements.txt

# launch server
python app.py
```

>Note: If the app does not run immediately, it may be because the mongodb has not been configured on heroku.  Continue with the steps below which should solve the problem.

>Note: If you add variables to the ```.env```, you need to deactivate the virtual environment and reactivate.

### Deploy to Heroku

```
# create the app
heroku create

# rename app
heroku apps:rename newname

git push heroku master
```

### Development Notes

```
# Add module to requirements
pip freeze > requirements.txt

# Stop virtual environment
deactivate

# Test post
ipython
> import requests
> requests.post(<url>, json={'test': 'post'})
```