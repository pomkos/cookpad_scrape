# Required to host the website:

## core folder
* This folder should contain pythonwikibot, fully set up and owned by nginx:
```
wget http://tools.wmflabs.org/pywikibot/core.tar.gz
tar -xvzf core.tar.gz
sudo chown www-data:www-data core -R
```
* https://www.mediawiki.org/wiki/Manual:Pywikibot

## scrape_env folder
* This folder should contain a python virtual environment, with all requirements installed within.

```
python3.6 -m venv scrape_env # make environment
source scrape_env/bin/activate # use environment
cp ~/cookpad_scrape/requirements.txt ~/cookpad_scrape/website/scrape_env # copy-paste requirements.txt
pip install -r requirements.txt # install all requirements
```

## hosting with nginx
* In /etc/systemd/system/[my_cookpad_scraper].service
```
[Unit]
Description=uWSGI instance to serve scraper
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/home/USER/cookpad_scrape/website/
Environment="PATH=/home/USER/cookpad_scrape/website/scrape_env/bin$"
ExecStart=/home/USER/cookpad_scrape/website/scrape_env/bin/uwsgi --ini scrape.ini

[Install]
WantedBy=multi-user.target
```
* In /etc/nginx/sites-available

```
server {
    server_name cookpad.my_website.com;

    location / {
        include uwsgi_params;
        uwsgi_pass unix: /home/USER/cookpad_scrape/website/cookpad_start.sock;
    }

    listen 80;
}
```
* run letsencrypt as needed
