### ----- Start with: python3 russell.py ----- ###
### ----- Picture download function commented out ----- ###
### ----- pythonwikibot command:
#               python3 pwb.py pagefromfile -force -file:recipes2.doc
import requests
import os
import urllib
from bs4 import BeautifulSoup

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

def download_mainpic(title_ext, mainpic_clean, url, f):
    if mainpic_clean is None:
        return
    else:
        mainpic_name = title_ext + '.jpg'
        dir1 = 'main_pics'
        dirpath = os.path.join(dir1,mainpic_name)
        r2 = requests.get(mainpic_clean)
        with open(dirpath, "wb") as f2:
            f2.write(r2.content)
        f.write('\n' + '[[File:' + mainpic_name + '|' + 'link=' + url + "|'''" + title_ext + "'''" + ']]' + '\n')

def get_ingredients(soup, f):
    ingredients = soup.find(id='ingredients')
    ingredients_ext = ingredients.ol.extract()
    ingredients_clean = ingredients_ext.find_all(itemprop='ingredients')
    f.write('\n'+'=Ingredients=' + '\n')
    for ingredient in ingredients_clean:
        ing = ingredient.text.strip()
        f.write('* ' + ing + '\n')

def get_steps(soup, f):
    steps = soup.find(id='steps')
    steps_p = steps.find_all(itemprop='recipeInstructions')
    steps_pics_messy = steps.find_all(class_='step numbered-list__item card-sm')
    f.write('\n'+'=Steps=' + '\n')
    for i, step in enumerate(steps_p):
        extracted = step.p.extract()
        extract = extracted.text.strip()
    #---- Steps Pics ----#
        steps_pics_lines = steps_pics_messy[i].a
        download_steppic(steps_pics_lines, extract, i, f)

def download_steppic(steps_pics_lines, extract, i, f):
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
            dir1 = 'step_pics'
            dirpath = os.path.join(dir1,pic_name)
            r3 = requests.get(pic_link)
            with open(dirpath, "wb") as f3:
               f3.write(r3.content)
        except:
            f.write('\n' + str(i) + '. ' + extract + '\n')
            pass

def recipe(url):
    f = (open('recipe.doc', 'w'))

    #--- Inside the Recipe Link, Scrape Info for... ---#
    page = requests.get(url)
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
    download_mainpic(title_ext, mainpic_clean, url, f)
    f.write('\n' + '=About=' + '\n' + about_clean + '\n')
    
    #--- Ingredients ---#
    get_ingredients(soup, f)
    #--- Steps ---#
    get_steps(soup, f)
    f.write('\n' + '[[Category:Recipes]]' + '\n')
    f.write('\n' + '{{-stop-}}' + '\n')
    print("Scraped:  " + title_ext)