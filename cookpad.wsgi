activate_this = '/home/peter/NetShare/myproject/django_demo'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

import sys
sys.path.insert(0,'/home/peter/NetShare/cookpad_scrape')

from cookpad import app as application
