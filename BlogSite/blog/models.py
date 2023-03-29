from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=70)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Categories, self).save(*args, **kwargs)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField( max_length=200)
    slug = models.SlugField(unique=True,blank=True)
    image = models.ImageField( upload_to='images')
    content = RichTextField()
    created = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Categories, related_name='post' ,on_delete=models.CASCADE)
    metatitle = models.CharField( max_length=200)
    metadesc = models.TextField()
    Publish = models.BooleanField(default=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comments(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=254)
    comments = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post