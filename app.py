from flask import Flask


app=None #initially none

def init_app():
    kanban_app=Flask(__name__) #object of Flask
    kanban_app.debug=True
    kanban_app.app_context().push() #Direct access app by other modules(db, authentication)
    print("Kanban application started....")
    return kanban_app

app=init_app()
from backend.controllers import *

if __name__=="__main__":
    app.run()


