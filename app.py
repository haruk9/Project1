from flask import Flask, render_template
from pymongo import MongoClient
from forms import RegForm


app = Flask(__name__)
app.secret_key = 'secret stuff'

client = MongoClient('mongodb+srv://mongodb:mongo@cluster0.iiyah.mongodb.net/?retryWrites=true&w=majority')
db = client.registration
user_col = db.users

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    reg_form = RegForm()
    if reg_form.validate_on_submit():
        
        user = {}
    
        user['Username: '] = reg_form.username.data
        user['Name: '] = reg_form.name.data
        user['Email: '] = reg_form.email.data
        user['Password: '] = reg_form.password.data

        user_col.insert_one(user)
        
    return render_template('registration.html', title='Registration', form=reg_form)


if __name__ == "__main__":
    app.run(debug=True)