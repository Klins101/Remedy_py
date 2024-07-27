from flask import Flask, render_template, url_for
from flask_restx import Api, Resource
from config import DevelopmentConfig
from models import User
from exts import db

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
api = Api(app, doc='/docs', title='Remedy API',
          version='1.0', description='API for Remedy data')


@api.route('/home')
class Home(Resource):
    def get(self):
        return {'message': 'Welcome to Remedy API'}


@app.shell_context_processor
def make_shell_context():
    return dict(app=app, db=db, User=User)


@app.route('/about')
def about():
    return '<h1>About Page </h1>'


if __name__ == "__main__":
    app.run()
