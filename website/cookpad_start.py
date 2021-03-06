from flask import request, Flask, render_template, url_for, redirect
from cookpad_recipe_only import recipe
from cook_db import send_data, read_data
import os
import shutil
import fnmatch
import subprocess
import requests

app = Flask(__name__) #create Flask app
app._static_folder = 'static/'


@app.route('/', methods=['GET','POST'])
def homepage():
        #--- Check if its a post or get request: ---#
    if request.method == 'POST': #this block is only entered if the form is submitted
        scraper()
    return render_template('index.html')

#--- Cookpad Scraper Stuff ---#
def scraper(): # sending via forms as a post request (behind the scenes)
    #--- Check if its a post or get request: ---#
    if request.method == 'POST': #this block is only entered if the form is submitted
        url = request.form.get('recipe') 
        user = request.form['name']
        #--- Assign variables to the multiple choices ---#
        category = request.form.get('category')
        dessert = request.form.get('dessert') 
        main_dish = request.form.get('main_dish') 
        side_dish = request.form.get('side_dish') 
        soup = request.form.get('soup') 
        mommy = request.form.get('mommy')
              
        #--- Make sure a valid url was submitted ---#
        check_url = 'https://cookpad.com'
        if check_url in url: #if a string is submitted with https://cookpad.com in it
            title = recipe(url, category, dessert, main_dish, side_dish, soup, mommy, user) #puts the title_ext returned from recipe() into the title variable
            send_data(title, url, mommy, category) # send data to rethinkdb: cookpad_scrape database
            publish(user) #publishes the scraped recipe into wiki
            telegram(user, title) #notifies telegram

            return redirect(url_for('thanks', title=title, user=user)) #redirects to url.com/thanks?title=something&user=something_else. Variables are in the link

        else: #otherwise return bad_link.html
            return redirect(url_for('bad_link', link=url, user=user))

    #--- Make the form ---#
    return render_template('#Scraper')

def publish(user):
    #--- Copy the recipe.doc file to a new dir ---#
        #shutil.copy2 can copy directories as well
    shutil.copyfile('/var/www/homepage/scrape/recipe.doc', '/var/www/homepage/scrape/core/recipe.doc') 
    os.chdir("/var/www/homepage/scrape")
    subprocess.run(['./run_pwb.sh']) # Just run the program
    
def telegram(user, title):
    #--- Telegram Params ---#
    token = 'CHANGE ME' #find by messaging @BotFather
    chat_id = 'CHANGE ME' # find by messaging @ChatsIDsBot
    message = user + ' finished scraping ' + title #message
    url = 'https://api.telegram.org/' + 'bot' + token + '/sendMessage'

    #--- Send a notification to telegram that a recipe has been wikified ---#
    requests.post(url, data={'chat_id':chat_id, 'text':message})

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
