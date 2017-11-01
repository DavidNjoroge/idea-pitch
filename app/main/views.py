from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Comment,User,Pitch,Category
from .. import db
from .forms import NewPitch,NewComment

from flask_login import login_required,login_user,current_user


@main.route('/')
def index():
    '''
    view function for the landing page
    '''
    categories=Pitch.query.filter_by(category='category')
    pitches=Pitch.query.all()
    return render_template('index.html',categories=categories,pitches=pitches)

@main.route('/new-pitch',methods = ['GET', 'POST'])
@login_required
def new_pitch():
    '''
    view function for creating a new pitch
    '''
    form=NewPitch()
    if form.validate_on_submit():
        title=form.title.data
        # print (title)
        body=form.body.data
        # print (body)
        category=form.category.data
        print (current_user)
        print (',.,.,><><><><>,.,.<><><><><')
        # user='david'
        new_pitch=Pitch(header=title,body=body,category=category,user=current_user)
        new_pitch.save_pitch()
        return render_template('index.html',form=form)

    return render_template('new-pitch.html',form=form)

@main.route('/pitch/<int:id>')
def pitch(id):
    pitch=Pitch.query.get(id)
    comments=Comment.query.filter_by(pitch_id=id)

    return render_template('pitch.html',pitch=pitch,comments=comments)

@main.route('/comment/<int:id>',methods = ['GET', 'POST'])
def comments(id):
    form=NewComment()
    if form.validate_on_submit():
        body=form.body.data
        pitchq=Pitch.query.filter_by(id=id)
        new_comment=Comment(body=body,commentz=current_user,pitch_id=id)
        new_comment.save_comment()
        return redirect(url_for('.pitch',id=id))


    return render_template('comment.html',form=form)
