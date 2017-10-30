from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Pitches,Comments
from flask_migrate import Migrate,MigrateCommand


# creating app is=nstances
app=create_app('development')
migrate=Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)
@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User)
@manager.MigrateCommand
def test():
    import unittest


if __name__=='__main__':
    manager.run()
