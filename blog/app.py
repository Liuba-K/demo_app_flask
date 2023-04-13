import os

from blog.security import flask_bcrypt
from flask import Flask, render_template
from flask_migrate import Migrate

from blog.views.users import users_app
from blog.views.articles import articles_app
from blog.views.auth import login_manager, auth_app
from blog.views.authors import authors_app

from blog.models.database import db
from blog.admin import admin

from blog.api import init_api

app = Flask(__name__)

app.config.from_object('blog.configs')
app.config["SQLALCHEMY_DATABASE_URI"] ="sqlite:///D:\\IT\\projects\\Flask\\sqlite.db"
app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")
app.register_blueprint(auth_app, url_prefix="/auth")
app.register_blueprint(authors_app, url_prefix="/authors")

migrate = Migrate(app, db, compare_type=True)
login_manager.init_app(app)
db.init_app(app)
flask_bcrypt.init_app(app)
admin.init_app(app)
api = init_api(app)

@app.route("/")
def index():
    return render_template("index.html")


@app.cli.command("create-tags")
def create_tags():
    """
    Run in your terminal:
    ➜ flask create-tags
    """
    from blog.models import Tag
    for name in [
        "flask",
        "django",
        "python",
        "sqlalchemy",
        "news",
    ]:
        tag = Tag(name=name)
        db.session.add(tag)
    db.session.commit()
    print("created tags")
