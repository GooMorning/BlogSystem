from flask_script import Manager, Server
from main import app
from main import app,db,User
from flask_migrate import Migrate,MigrateCommand


manager = Manager(app)
mirgrate = Migrate(app, db)

manager.add_command("server",Server())
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User)

if __name__ == '__main__':
    manager.run()