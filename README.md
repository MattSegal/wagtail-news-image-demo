# Wagtail News Image Example

Example app used to showcase the [News Image](https://github.com/StocksDigital/wagtail-news-image) plugin for Draftail.

Setup requires `virtualenv` and Python 3

```
# Setup virtualenv, load demo data
./scripts/setup.sh
. env/bin/activate

# Run the server on localhost
cd demo
./manage.py runserver
```

Now you can visit `localhost:8000` to see the demo page.

You can also visit `localhost:8000/cms/pages/` to see the Wagtail admin. Username and password are `admin` / `z`
