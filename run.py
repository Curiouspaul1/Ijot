from ijot1 import __call__,db
from flask_migrate import Migrate
import os

# flask-migrate
app = __call__('default' or os.getenv('FLASK_CONFIG'))
migrate = Migrate(app,db)

"""# cli initializer
manager = Manager(app)
manager.add_command('db', MigrateCommand)

#run manager
manager.run()
"""