from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Comment,User,Pitch,Category
from .. import db
from .forms import NewPitch

@main.route('/')
def index():
    '''
    view function for the landing page
    '''
    categories=Category.query.all()
    return render_template('index.html',categories=categories)

@main.route('/new-pitch',methods = ['GET', 'POST'])
def new_pitch():
    '''
    view function for creating a new pitch
    '''
    form=NewPitch()
    if form.validate_on_submit():
        title=form.title.data
        print (title)
        body=form.body.data
        print (body)
        category=form.category.data
        print (category)
        user='david'
        new_pitch=Pitch(header=title,body=body,category=category)
        print (',.,.,><><><><>,.,.<><><><><')
        new_pitch.save_pitch()
        return render_template('main.index',form=form)

    return render_template('new-pitch.html',form=form)
