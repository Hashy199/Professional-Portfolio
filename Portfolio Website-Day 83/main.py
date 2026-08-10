from flask import Flask, render_template, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from flask_bootstrap import Bootstrap5
from functools import wraps
from flask import session, request
from werkzeug.security import generate_password_hash, check_password_hash
import os
import datetime as dt
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField
ADMIN_PASSWORD_HASH = os.environ.get("ADMIN_PASSWORD_HASH")
# WTForm for creating a blog post
class CreateProjectForm(FlaskForm):
    title = StringField("Project Title", validators=[DataRequired()])
    subtitle = StringField("Project Subtitle", validators=[DataRequired()])
    img_url = StringField("Project Image URL", validators=[DataRequired()])
    github_link = StringField("Project Github URL", validators=[DataRequired()])
    submit = SubmitField("Submit")
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "dev-only-change-this")
bootstrap = Bootstrap5(app)

class Base(DeclarativeBase):
    pass
db_url = os.environ.get('POSTGRES_URL')
if db_url:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace('postgres://', 'postgresql://', 1)
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///local.db'


db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Projects(db.Model):

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)
    github_link: Mapped[str] = mapped_column(String(250), nullable=False)

with app.app_context():
    db.create_all()


year = dt.datetime.now().year
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def home():
    result = db.session.execute(db.select(Projects))
    projects = result.scalars().all()
    return render_template('index.html', year=year, projects=projects)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        password = request.form.get('password')
        if check_password_hash(ADMIN_PASSWORD_HASH, password):
            session['logged_in'] = True
            return redirect('/add')
    return render_template('login.html')

@app.route('/add', methods=['GET', 'POST'])
@login_required
def add():
    form = CreateProjectForm()
    if form.validate_on_submit():
        print('hi')
        new_project = Projects(
            title=form.title.data,
            subtitle=form.subtitle.data,
            img_url=form.img_url.data,
            github_link=form.github_link.data
        )
        db.session.add(new_project)
        db.session.commit()
        return redirect('/')

    for field, errors in form.errors.items():
        for error in errors:
            flash(f"Error in {getattr(form, field).label.text}: {error}", 'error')
    return render_template('add.html', form=form)
if __name__ == "__main__":
    app.run()
