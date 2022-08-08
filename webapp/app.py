from multiprocessing import connection
from flask import Flask, render_template
import psycopg2
from psycopg2 import Error
from webapp.forms import RegForm


app = Flask(__name__)
app.secret_key = 'secret stuff'



@app.route('/', methods=['GET', 'POST'])
def index():
    reg_form = RegForm(meta={'csrf': False})
    if reg_form.validate_on_submit():
        try:
            # Connect to an existing database
            connection =psycopg2.connect(user="...", password="...", host="...", port="...", database="...")

            cursor = connection.cursor()
            username = reg_form.username.data
            name = reg_form.name.data
            email = reg_form.email.data
            password = reg_form.password.data
            # Call stored procedure
            cursor.execute("...")
            connection.commit()
            cursor.close()

            
        except (Exception, psycopg2.DatabaseError) as error:
            print("Error while connectiong to PostgreSQL.", error)

        finally:
            #Closing connection
            if connection:
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    return render_template('base.html', title='Registration', form=reg_form)


if __name__ == "__main__":
    app.run(debug=True)