from ijot1 import app,db
from flask_migrate import Migrate,MigrateCommand

# flask-migrate
migrate = Migrate(app,db)

"""# cli initializer
manager = Manager(app)
manager.add_command('db', MigrateCommand)

#run manager
manager.run()
"""