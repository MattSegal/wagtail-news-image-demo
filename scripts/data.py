from django.contrib.auth.models import User
from wagtail.core.models import Site, Page

from demo.models import NewsImagePage

Site.objects.all().delete()
Page.objects.all().delete()
User.objects.all().delete()

admin = User.objects.create(
    **{
        "password": "pbkdf2_sha256$100000$zDoltk5zVX2x$2WovHsoOPtFS6xFbwFoSUwQqNP4mnpfYMY9I7k5UsU0=",
        "is_superuser": True,
        "username": "admin",
        "is_staff": True,
        "is_active": True,
    }
)

root_page = Page(title='Root Page')
Page.add_root(instance=root_page)

news_page = NewsImagePage(**{
    "title": "News Image Demo Page",
    "slug": "news-image-demo-page",
    "live": True,
    "has_unpublished_changes": False,
    "url_path": "/",
    "owner": admin,
    "first_published_at": "2018-08-28T04:30:35.450Z",
    "last_published_at": "2018-08-28T04:30:35.450Z",
    "body": '<h2>Image with a link</h2><p>This is an image with a hyperlink wrapping it:</p><embed alt="Cadrona terrain park (New Zealand)" embedtype="news-image" href="https://www.cardrona.com/winter/" id="1" title="Cadrona terrain park (New Zealand)" width="800"/><p></p><p>Ut tristique et egestas quis. Aenean euismod elementum nisi quis eleifend quam adipiscing. Vel pretium lectus quam id leo in vitae turpis massa. Eu turpis egestas pretium aenean pharetra magna ac placerat. Ut porttitor leo a diam.</p><h2>Resized Image</h2><p>This is an image that has been resized using the &quot;resize&quot; button from the &quot;Edit&quot; tab:</p><embed alt="Snowmass, Aspen" embedtype="news-image" href="" id="2" title="Snowmass, Aspen" width="480"/><p></p><p>Non arcu risus quis varius quam. Sed sed risus pretium quam vulputate dignissim suspendisse in est. Ut tristique et egestas quis ipsum suspendisse ultrices gravida. Orci nulla pellentesque dignissim enim sit.</p><p></p>',
})
root_page.add_child(instance=news_page)


site = Site.objects.create(
    **{
        "hostname": "localhost",
        "port": 80,
        "site_name": "News Site",
        "root_page": news_page,
        "is_default_site": True
    }
)
