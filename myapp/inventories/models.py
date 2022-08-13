from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class BookGenres(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Books(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True)
    genre = models.ForeignKey(BookGenres, on_delete=models.CASCADE)
    author = models.CharField(max_length=250)
    isbn = models.IntegerField()
    count = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Books, self).save(*args, **kwargs)

