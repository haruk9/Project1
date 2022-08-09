from multiprocessing import connection
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from webapp.forms import RegForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = '...'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.secret_key = 'secret stuff'

class Regtable(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), index = True, unique = True)
    name = db.Column(db.String(50), index = True, unique = False)
    email = db.Column(db.String(50), index = True, unique = True)
    password = db.Column(db.String(50), index = True, unique = False)

@app.route('/', methods=['GET', 'POST'])
def index():
    reg_form = RegForm(meta={'csrf': False})
    if reg_form.validate_on_submit():
        
        username = reg_form.username.data
        name = reg_form.name.data
        email = reg_form.email.data
        password = reg_form.password.data

        user = Regtable(username = username, name = name, email = email, password=password)

        db.session.add(user)
        db.session.commit()

    return render_template('base.html', title='Registration', form=reg_form)


if __name__ == "__main__":
    app.run(debug=True)