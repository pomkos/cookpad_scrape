### ----- Start with: python3 russell.py ----- ###
### ----- Picture download function commented out ----- ###
### ----- pythonwikibot command:
#               python3 pwb.py pagefromfile -force -file:recipes2.doc
import requests
import os
import urllib
from bs4 import BeautifulSoup

f = (open('recipes2.doc', 'w'))

# input("What is the profile link? ")
base_input = 'https://cookpad.com/hu/felhasznalok/6659384'
num_input = 100000

page_list = []

def profile():
    #--- Get the Next Page in the Profile ---#
    for i in range(1, num_input + 1):
        next_page = '?page=' + str(i)
        url = base_input + next_page
        #--- In Each Profile Link... ---#
        profile = requests.get(url)
        psoup = BeautifulSoup(profile.text, 'lxml')
        main_profile = psoup.body.find(id='main')
        recipe_list = main_profile.find(class_='recipe-list')
        # if there is no more content on the page, stop putting the link in page_list matrix.
        if (recipe_list.text.strip()) == "":
            break
        #--- Find All Recipes' Link in the Page ---#
        for recipe in recipe_list.find_all(class_='wide-card ranked-list__item'):
            base = 'https://cookpad.com'
            recipe_clear = recipe.find(class_='media')
            recipe_link = recipe_clear.get('href')
            url = base + recipe_link
            page_list.append(url)

def get_about(soup, about):
    about_ext = about.p.extract()
    about_clean = about_ext.get_text()
    return about_clean

def get_title(about):
    title = about.find('h1')
    title_ext = title.text.strip()
    return title_ext

def get_mainpic(soup, title_ext):
    for mainpic in soup:
        try:
            mainpic = soup.find(id='recipe_image')
            mainpic_ext = mainpic.find(alt=title_ext)
            mainpic_clean = mainpic_ext.get('src')
            return mainpic_clean
        except:
            print("No Main Picture in " + title_ext)
            pass

def download_mainpic(title_ext, mainpic_clean, item):
    if mainpic_clean is None:
        return
    else:
        mainpic_name = title_ext + '.jpg'
        # r2 = requests.get(mainpic_clean)
        # with open(mainpic_name, "wb") as f2:
        #     f2.write(r2.content)
        f.write('\n' + '[[File:' + mainpic_name + '|' + 'link=' + item + "|'''" + title_ext + "'''" + ']]' + '\n')

def get_ingredients(soup):
    ingredients = soup.find(id='ingredients')
    ingredients_ext = ingredients.ol.extract()
    ingredients_clean = ingredients_ext.find_all(itemprop='ingredients')
    f.write('\n'+'=Ingredients=' + '\n')
    for ingredient in ingredients_clean:
        ing = ingredient.text.strip()
        f.write('* ' + ing + '\n')

def get_steps(soup):
    steps = soup.find(id='steps')
    steps_p = steps.find_all(itemprop='recipeInstructions')
    steps_pics_messy = steps.find_all(class_='step numbered-list__item card-sm')
    f.write('\n'+'=Steps=' + '\n')
    for i, step in enumerate(steps_p):
        extracted = step.p.extract()
        extract = extracted.text.strip()
    #---- Steps Pics ----#
        steps_pics_lines = steps_pics_messy[i].a
        download_steppic(steps_pics_lines, extract, i)

def download_steppic(steps_pics_lines, extract, i):
    for child in steps_pics_lines.children:
        try:
            i=i+1
            pic_link = child.find('img').get('src')
            pic_jpg = os.path.split(pic_link)[0]
            pic_jpg2 = os.path.split(pic_jpg)[0]
            pic_jpg3 = os.path.split(pic_jpg2)[1]
            pic_name = 'STEP-' + pic_jpg3 + '-' + str(i) + '.jpg'
            f.write('\n' + '[[File:' + pic_name + '|300px|Step ' + str(i) + ']]' + '\n')
            f.write('\n' + str(i) + '. ' + extract + '\n')
            # r3 = requests.get(pic_link)
            # with open(pic_name, "wb") as f3:
            #    f3.write(r3.content)
        except:
            f.write('\n' + str(i) + '. ' + extract + '\n')
            pass

def recipe():
    #--- Inside the Recipe Link, Scrape Info for... ---#
    for item in page_list:
        page = requests.get(item)
        soup = BeautifulSoup(page.text, 'lxml')
        about = soup.find(id='about')

        #--- About Section ---#
        about_clean = get_about(soup, about)
        #--- Title ---#
        title_ext = get_title(about)
        #---Main Picture ---#
        mainpic_clean = get_mainpic(soup, title_ext)
        #----Download Main Pic----#
        f.write('\n' + "{{-start-}}" + "\n")
        download_mainpic(title_ext, mainpic_clean, item)
        f.write('\n' + '=About=' + '\n' + about_clean + '\n')
        
        #--- Ingredients ---#
        get_ingredients(soup)
        #--- Steps ---#
        get_steps(soup)
    # f.write('\n </gallery>')
        f.write('\n' + '[[Category:Recipes]]' + '\n')
        f.write('\n' + '{{-stop-}}' + '\n')
        print("Scraped:  " + title_ext)
        
profile()
recipe()