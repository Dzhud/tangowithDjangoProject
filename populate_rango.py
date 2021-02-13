# Script to populate the database with 
# realistic and credible data.
#When importing Django models, make sure you have imported your project’s settings
#by importing django and setting the environment variable DJANGO_SETTINGS_MODULE
#to be your project’s setting file, as demonstrated in lines 1 to 6 above. You then call
#django.setup() to import your Django project’s settings.

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
    python_pages = [
        {"title": "Official Python Tutorial", "url": "http://docs.python.org/2/tutorial/", "views": 2600},
        {"title": "How to Think Like a Computer Scientist", "url": "http://www.greenteapress.com/thinkpython/", "views": 350},
        {"title": "Learn Python in 10 Minutes", "url": "http://www.korokithakis.net/tutorials/python/", "views": 750}   
    ]
    
    django_pages = [
        {"title": "Official Django Tutorial", "url": "http://docs.djangoproject.com/en/1.9/intro/tutorial01/", "views": 240},
        {"title": "Django Rocks", "url": "http://djangorocks.com/", "views": 120},
        {"title": "How to Tango with Django", "url": "http://www.tangowithdjango.com/", "views": 180}
        
    ]
    
    other_pages = [
        {"title": "Bottle", "url": "http://bottlepy.org/docs/dev/", "views": 240},
        {"title": "Flask", "url": "http://flask.pocco.org", "views": 9000}
    ]
    
    cats =  {
        "Python": {"pages": python_pages, "views": 128, "likes": 64},
        "Django": {"pages": django_pages, "views": 64, "likes": 32},
        "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}
    }  


  
    
 #The below code helps to iterate ovr the dics above
    for cat, cat_data in cats.items(): 
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])  

        
# Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("-{0} - {1}".format(str(c), str(p)))
        
def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, likes=0, views=0):
    c= Category.objects.get_or_create(name=name)[0]
    c.likes = likes
    c.views = views
    c.save()
    return c  
 
# Start execution here
if __name__=='__main__':
    print("Starting Rango population script...")
    populate()