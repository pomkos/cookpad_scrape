# Assumptions:
* mediawiki is installed in /var/www/mediawiki and [fully set up](https://www.digitalocean.com/community/tutorials/how-to-install-mediawiki-on-ubuntu-14-04) via mydomain.com
```
cd /var/www
sudo wget https://releases.wikimedia.org/mediawiki/1.31/mediawiki-1.31.0.tar.gz
sudo tar -xvzf mediawiki*
sudo mv mediawiki* mediawiki
```
* highly recommended: [UploadLocal extension](https://www.mediawiki.org/wiki/Extension:UploadLocal), with default folder set to location of site_pics
```
sudo nano /var/www/mediawiki/LocalSettings.php

# Extension: UploadLocal
require_once("$IP/extensions/UploadLocal/UploadLocal.php");
$wgUploadLocalDirectory = $GP . '/var/www/website/scrape/site_pics';
```

# Required to host the website:

## core folder
* This folder should contain pythonwikibot, [fully set up](https://www.mediawiki.org/wiki/Manual:Pywikibot) and owned by nginx:
```
wget http://tools.wmflabs.org/pywikibot/core.tar.gz
tar -xvzf core.tar.gz
sudo chown www-data:www-data core -R
```

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

# Result:
## Scraper form:
![alt text](https://i.imgur.com/cYvHHoI.png)

## Scraping success:
![alt text](https://i.imgur.com/kiAkTCQ.png)

## Scraping error:
![alt text](https://i.imgur.com/uknib8m.png)
