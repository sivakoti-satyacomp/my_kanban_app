from flask import Flask
from backend.models import *

app=None #initially none

def init_app():
    kanban_app=Flask(__name__) #object of Flask
    kanban_app.debug=True
    kanban_app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///kanban.sqlite3"
    kanban_app.app_context().push() #Direct access app by other modules(db, authentication)
    db.init_app(kanban_app) #object.method(<parameter>)
    print("Kanban application started....")
    return kanban_app

app=init_app()
from backend.controllers import *

if __name__=="__main__":
    app.run()


