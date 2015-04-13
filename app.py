from project import app, db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

# This allows us to use a .env file to load environment variables
import os
import dotenv
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
dotenv.load_dotenv(BASE_DIR + "/.env")

# Allows you to run migrations with this file
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
