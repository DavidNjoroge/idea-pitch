from . import db
from datetime import datetime
from flask_login import UserMixin
from . import login_manager
from werkzeug.security import generate_password_hash,check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255))
    # bio=db.Column(db.String(255))
    pass_secure=db.Column(db.String(255))
    pitch=db.relationship('Pitch',backref='user',lazy="dynamic")
    comment=db.relationship('Comment',backref='commentz',lazy="dynamic")


    @property
    def password(self):
        raise AttributeError('sorry you cannot view the password')

    @password.setter
    def password(self,password):
        self.pass_secure=generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        # return str(self.username)
        return f'User {self.username}'



class Pitch(db.Model):
    __tablename__='pitches'

    id =db.Column(db.Integer,primary_key=True)
    header=db.Column(db.String(255))
    body=db.Column(db.String(255))
    category=db.Column(db.String(255))
    time=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    # comment=db.relationship('Comment',backref='pitches',lazy="dynamic")

    # user=db.Column(db.String())

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def get_all_pitches(self):
        pitches=Pitch.query.all()
        return pitches

    @classmethod
    def get_pitches(cls,id):
        pitches=Pitch.query.filter_by(user_Id=id)
        return pitches
    def __repr__(self):
        return f'User {self.header}'

# @classmethod
class Comment(db.Model):
    __tablename__='comments'

    id=db.Column(db.Integer,primary_key=True)
    body=db.Column(db.String(255))
    time=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id=db.Column(db.Integer)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments=Comment.query.filter_by(user_Id=id)
        return comments

    def __repr__(self):
        return f'User {self.body}'

# @classmethod
class Category(db.Model):
    __tablename__='categories'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))

    # def save_category(self):
    #     db.session.add(self)
    #     db.session.commit()
    #
    def get_categories(self):

        return

    def __repr__(self):
        return f'User {self.name}'
