from flask import request, Flask
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
        recipe(url)
        publish(user)
        return '''<h1>Thanks {},</h1> your request has been submitted'''.format(user)

    #--- Make the form ---#
    return '''<form method = "POST">
                    What is the cookpad recipe page? <input type="text" name="recipe"><br>
                    What is your name? <input type="text" name="name"><br>
                    <input type="submit" value="Submit"><br>
                </form>'''
                # The form makes a post request to the same route that made the form

def publish(user):
    #copy the recipe.doc file to a new dir
    #shutil.copy2 can copy directories as well
    shutil.copyfile('/home/peter/NetShare/cookpad_scrape/recipe.doc', '/home/peter/NetShare/core/recipe.doc') 
    os.chdir("/home/peter/NetShare/core")
    os.system("python3 pwb.py login")
    os.system("python3 pwb.py pagefromfile -file:recipe.doc -force -summary:Uploaded from cookpad.thegates.online")
    print('recipe uploaded to wiki')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')