from flask import Flask, render_template
from pymongo import MongoClient
from forms import TestForm


app = Flask(__name__)
app.secret_key = 'secret stuff'



@app.route('/')
def hello_geek():
    return render_template('base.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = TestForm()
    if form.validate_on_submit():
        name = {}
        name['Name: '] = form.name.data
        
        
    return render_template('submit.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)