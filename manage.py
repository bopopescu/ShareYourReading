# encoding: utf-8

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from syr import app
from exts import db
from models import User, Post, Comment, Book

manager = Manager(app)

# use Migrate to bind app and db
migrate = Migrate(app, db)

# add the comment to manager
manager.add_command('db', MigrateCommand)

db.init_app(app)

if __name__ == "__main__":
    manager.run()

