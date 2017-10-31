from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Comment,User,Pitch,Category
from .. import db

@main.route('/')
def index():
    '''
    view funciton for the landing page
    '''
    categories=Category.query.all()
    return render_template('index.html',categories=categories)
