# Wagtail News Image Example

Example app used to showcase the News Image plugin for Draftail.

Setup requires `virtualenv` and Python 3

```
# Setup virtualenv, load demo data
./scripts/setup.sh
. env/bin/activate

# Install the app
pip3 install -e ~/code/wagtail-news-image

# Run the server on localhost
cd demo
./manage.py runserver
```

Now you can visit `localhost:8000` to see the demo page.

You can also visit `localhost:800/cms/pages/` to see the Wagtail admin. Username and password are `admin` / `z`