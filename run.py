from ijot1 import app,db
from flask_migrate import Migrate,MigrateCommand
from flask_script import Manager

# flask-migrate
migrate = Migrate(app,db)

# cli initializer
manager = Manager(app)
manager.add_command('db', MigrateCommand)

#run manager
manager.run()
