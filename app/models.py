from . import db
from datetime import datetime

class User(db.Model):
    __tablename__='users'

    id = db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(255))
    email=db.Column(db.String(255))
    bio=db.Column(db.String(255))
    pass_secure=db.Column(db.String(255))
    pitches=db.relationship('Pitch',backref='user',lazy='dynamic')


    # @property
    # def password(self):
    #     raise AttributeError('sorry you cannot view the password')
    #
    # @password.setter
    # def password(self,password):
    #     self.pass_secure=generate_password
class Pitch(db.Model):
    __tablename__='pitches'

    id =db.Column(db.Integer,primary_key=True)
    header=db.Column(db.String(255))
    body=db.Column(db.String(255))
    category=db.Column(db.String(255))
    time=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    def get_all_pitches(self):
        pitches=Pitch.query.filter_by().all()
        return pitches

    @classmethod
    def get_pitches(cls,id):
        pitches=Pitch.query.filter_by(user_Id=id)
        return pitches

@classmethod
class Comment:
    __tablename__='comments'

    id=db.Column(db.Integer,primary_key=True)
    body=db.Column(db.String(255))
    time=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id=db.Column(db.Integer,db.ForeignKey('users.id'))

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
        comments=Comment.query.filter_by(user_Id=id)
        return comments
