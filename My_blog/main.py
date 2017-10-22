from flask import Flask
from config import DevConfig
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config.from_object(DevConfig)
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<int:page>')
def home(page=1):
    posts = User.query.order_by(User.id.desc()).paginate(page, 10)
#   user = User.query.order_by().all()

    return render_template(
        'home.html',
        posts=posts,
        page=page
    )



@app.route('/user',methods=['GET', 'POST'])
def user():
    form = NameForm()
    if form.validate_on_submit():
        new_post = User(username=form.username.data,text=form.text.data)
        db.session.add(new_post)
        db.session.commit()
    return render_template(
        'login.html',
        form=form
    )


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    text = db.Column(db.Text())

    def __repr__(self):
        return "<User(username='%s',text='%s')>"%(self.username, self.text)

class NameForm(Form):
    username = StringField('name', validators=[DataRequired()])
    text = TextAreaField('周报',validators=[DataRequired()])
    submit = SubmitField('Submit')



if __name__ == '__main__':
    app.run()
