from flask import Flask, render_template
from backened.models import db

#app = Flask(__name__)#instance of app
app=None

def setup_app():        #connect to sql,crerte flask instance,debu dev env ison and allow app to interact with other models

    app=Flask(__name__)
    app.debug=True
    #we will put sqlite connection
    app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///house_services.sqlite3" #Having db file
    db.init_app(app)    #flask app conected to db (sqlalchemy)


    app.app_context().push() #direct access to other models
    print("house services started.....")
    


#call the setup
setup_app()

#instaed of routes here paste it to controller.py and access them via

from backened.controller import *

if __name__ == "__main__":
    app.run(debug=True)
