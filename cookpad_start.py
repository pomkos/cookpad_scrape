from flask import request, Flask, render_template, url_for, redirect
from cookpad_recipe_only import recipe
import os
import shutil

app = Flask(__name__) #create Flask app

@app.route('/', methods=['GET','POST']) #allow get and post requests
def home(): # sending via forms as a post request (behind the scenes)

    #--- Check if its a post or get request: ---#
    if request.method == 'POST': #this block is only entered if the form is submitted
        url = request.form.get('recipe') 
        user = request.form['name']
        title = recipe(url) #puts the title_ext returned from recipe() into the title variable
        publish(user) #publishes the scraped recipe into wiki
        return redirect(url_for('thanks', title=title, user=user)) #redirects to url.com/thanks?title=something&user=something_else. Variables are in the link

    #--- Make the form ---#
    return render_template('home.html')

def publish(user):
    #--- Copy the recipe.doc file to a new dir ---#
        #shutil.copy2 can copy directories as well
    shutil.copyfile('/home/peter/NetShare/cookpad_scrape/recipe.doc', '/home/peter/NetShare/core/recipe.doc') 
    os.chdir("/home/peter/NetShare/core")
    os.system("python3 pwb.py login")
    os.system("python3 pwb.py pagefromfile -file:recipe.doc -force -summary:'Uploaded by {}' ".format(user))

@app.route('/thanks')
def thanks():
    user = request.args.get('user')
    title = request.args.get('title')
    return render_template('thanks.html', name = user, title = title) # pass the variables to the html page

@app.route('/test')
def test():
    user = 'Peter'
    title = 'My Recipe'
    return render_template('test.html', name = user, title = title)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')