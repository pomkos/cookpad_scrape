from flask import request, Flask, render_template
from cookpad_recipe_only import recipe
import os
import shutil

app = Flask(__name__) #create Flask app

@app.route('/', methods=['GET','POST']) #allow get and post requests
def cookpad_form(): # sending via forms as a post request (behind the scenes)

    #--- Check if its a post or get request: ---#
    if request.method == 'POST': #this block is only entered if the form is submitted
        url = request.form.get('recipe')
        user = request.form['name']
        title = recipe(url)
        publish(user)
        return render_template('thanks.html', name = user, title = title) # pass the variables to the html page

    #--- Make the form ---#
    return '''<form method = "POST">
                    What is the cookpad recipe url? <input type="text" name="recipe"><br>
                    What is your name? <input type="text" name="name"><br>
                    <input type="submit" value="Submit"><br>
                </form>'''
                # The form makes a post request to the same route that made the form

def publish(user):
    #--- Copy the recipe.doc file to a new dir ---#
        #shutil.copy2 can copy directories as well
    shutil.copyfile('/home/peter/NetShare/cookpad_scrape/recipe.doc', '/home/peter/NetShare/core/recipe.doc') 
    os.chdir("/home/peter/NetShare/core")
    os.system("python3 pwb.py login")
    os.system("python3 pwb.py pagefromfile -file:recipe.doc -force -summary:'Uploaded by {}' ".format(user))
    print('recipe uploaded to wiki')

@app.route('/test')
def test():
    user = 'Peter'
    title = 'My Recipe'
    return render_template('thanks.html', name = user, title = title)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')