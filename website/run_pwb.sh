#!/bin/bash

cd /var/www/homepage/scrape/core

. "/var/www/homepage/scrape/scrape_env/bin/activate"

python3 pwb.py -login
python3 pwb.py pagefromfile -file:recipe.doc -force

