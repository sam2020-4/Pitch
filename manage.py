from app import create_app
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import User, Pitches, Comments

app = create_app('development')


manager = Manager(app)
manager.add_command('server',Server)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Pitches = Pitches, Comments= Comments)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


if __name__ == '__main__':
    app.run(debug = True)