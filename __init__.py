from flask import Flask
from api.py import app
#from . import models

# Connect sqlalchemy to app
#models.db.init_app(app)

#Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')