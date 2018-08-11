from flask import request, Flask, render_template, url_for, redirect
from cookpad_recipe_only import recipe
import os
import shutil
import fnmatch
import subprocess

app = Flask(__name__) #create Flask app

@app.route('/', methods=['GET','POST']) #allow get and post requests
def scraper(): # sending via forms as a post request (behind the scenes)
    #--- Check if its a post or get request: ---#
    if request.method == 'POST': #this block is only entered if the form is submitted
        url = request.form.get('recipe') 
        user = request.form['name']
        check_url = 'https://cookpad.com'
        if check_url in url: #if a string is submitted with https://cookpad. in it
            title = recipe(url) #puts the title_ext returned from recipe() into the title variable
            publish(user) #publishes the scraped recipe into wiki
            return redirect(url_for('thanks', title=title, user=user)) #redirects to url.com/thanks?title=something&user=something_else. Variables are in the link
        else: #otherwise return bad_link.html
            return redirect(url_for('bad_link', link=url, user=user))

    #--- Make the form ---#
    return render_template('scraper.html')

def publish(user):
    #--- Copy the recipe.doc file to a new dir ---#
        #shutil.copy2 can copy directories as well
    shutil.copyfile('/var/www/homepage/scrape/recipe.doc', '/var/www/homepage/scrape/core/recipe.doc')
    #shutil.copytree('/var/www/homepage/scrape/main_pics/*', '/var/www/mediawiki/extensions/UploadLocal/data')
    #shutil.copytree('/var/www/homepage/scrape/step_pics/*', '/var/www/mediawiki/extensions/UploadLocal/data')
    os.chdir("/var/www/homepage/scrape")
    subprocess.run(['./run_pwb.sh']) # Just run the program
    # os.system("./pwb.py pagefromfile -file:recipe.doc -force -summary:'Uploaded by {}' ".format(user))

@app.route('/thanks')
def thanks():
    user = request.args.get('user')
    title = request.args.get('title')
    return render_template('thanks.html', name = user, title = title) # pass the variables to the html page

@app.route('/bad_link')
def bad_link():
    user = request.args.get('user')
    link = request.args.get('link')
    return render_template('bad_link.html', name = user, link=link)

@app.route('/test')
def test():
    user = 'Peter'
    title = 'My Recipe'
    return render_template('test.html', name = user, title = title)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
