from django.db import models
from django.template.defaultfilters import slugify 
from django.contrib.auth.models import User 

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

#this class is to tell django about the right spelling to put in the Admin page
    class Meta:
        verbose_name_plural= 'Categories'

    def __str__(self):
        return self.name
    
    

class Page(models.Model):
    #looks like d other or 2nd model in a model.py always bear a 'models.Foreignkey' of the 1st model as seen below
    category = models.ForeignKey(Category) 
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title 


    
class UserProfile(models.Model):
    # This line is required. 
    # it links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    
    class Meta:
        verbose_name_plural= 'User Profiles'
    
    def __str__(self):
        return self.user.username


