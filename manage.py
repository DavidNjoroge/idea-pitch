from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Pitches,Comments


# creating app is=nstances
app=create_app('development')
