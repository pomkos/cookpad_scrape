from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from cookpad_recipe_only import recipe

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/", methods=['GET', 'POST'])
def index():
    form = ReusableForm(request.form)
    print(form.errors)
    if request.method == 'POST':
        url=request.form['name']
        print(url)
 
        if form.validate():
            success = recipe(url)
            flash(success)
        else:
            flash('All the form fields are required. ')
 
    return render_template('hello.html', form=form)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8092)