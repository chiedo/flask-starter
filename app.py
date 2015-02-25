from project import app, db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

# Allows you to run migrations with this file
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
