# can start with: uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
from cookpad_start import app

if __name__ == "__main__":
    app.run()
