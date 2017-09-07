from flask import *
from wtforms import *
from flask.ext.wtf import Form
import json

SECRET_KEY = 'development'

app = Flask(__name__)
app.config.from_object(__name__)
class NewUserForm(Form):
    firstname = StringField('Firstname', [
        validators.DataRequired(message='Requires a first name')
    ])
    lastname = StringField('Lastname', [
        validators.DataRequired(message='Requires a last name')
    ])
    email = StringField('Email Address', [
        validators.Email(message='Requires a valid email address'),
    ])
    department = SelectField(u'Department', choices=DEPARTMENTS)

@app.route('/done')
def done():
    flash('done')

@app.route('/',methods=['post','get'])
def register():
    form = NewUserForm(request.form)
    if form.validate_on_submit():
        app.logger.info(json.dumps(request.form))
        # Add json line to json list rakker json.dump(request.form, outfile)
        return render_template('done.html')
    return render_template('newUserForm.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)