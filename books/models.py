from django.db import models


from django.conf import settings
from django.urls import reverse

from account.models import Account

User=settings.AUTH_USER_MODEL
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    slug = models.SlugField(unique=True, max_length=100, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    # def get_absolute_path(self):
        # return reverse('store:product_list') + f'?category={self.id}'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_wise_books',kwargs={'slug':self.slug})


STREAM=(
    ('EXTC','EXTC'),
    ('INFT','INFT'),
    ('CS','CS'),
    ('ETRX','ETRX'),
    ('BIOMED','BIOMED'),
)
YEAR=(
    ('F.E','F.E'),
    ('S.E','S.E'),
    ('T.E','T.E'),
    ('B.E','B.E'),
)

TERM=(
    ('MID_TERM','MID_TERM'),
    ('END_TERM','END_TERM'),
)

class Notes(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False,help_text="Name of the Module")
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    thumbnail = models.ImageField(upload_to='media/books-thumbnail/', blank=True,default='media/no-image.jpg')
    pdf_file = models.FileField(upload_to='media/books/', blank=True, null=True)

    google_drive_url = models.URLField(unique=True, blank=True, null=True)

    is_visible = models.BooleanField(null=False, default=True)
    is_check = models.BooleanField(default=True)

    year = models.CharField(choices=YEAR, max_length=100,blank=True)
    stream = models.CharField(choices=STREAM, max_length=100,blank=True)
    term = models.CharField(choices=TERM,max_length=100,blank=True)
    subject=models.CharField(default="Signals & System" ,max_length=100)


    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="notes_uploaded_by")

    downloads = models.ManyToManyField(User, blank=True, related_name="notes_downloaded_by")

    def __str__(self):
        return self.name+" "+ self.subject+" "+ self.stream

    def get_absolute_url(self):
        return reverse('notes_detail',kwargs={'slug':self.slug})

class Book(models.Model):
    category = models.ManyToManyField(
        Category,blank=True,related_name='books')
    name = models.CharField(max_length=100, null=False, blank=False)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    author  = models.CharField(max_length=30,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    thumbnail = models.ImageField(upload_to='media/books-thumbnail/',blank=True,default='media/no-image.jpg')
    pdf_file  = models.FileField(upload_to='media/books/',blank=True,null=True)

    google_drive_url = models.URLField(unique=True,blank=True,null=True)

    is_visible = models.BooleanField(null=False, default=True)
    is_check   = models.BooleanField(default=True)

    is_syllabus = models.BooleanField(blank=False)

    year        = models.CharField(choices=YEAR,blank=True,max_length=100)
    stream      = models.CharField(choices=STREAM,blank=True,max_length=100)
    term      = models.CharField(choices=TERM,blank=True,max_length=100)

    uploaded_by=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True,related_name="uploaded_by")

    downloads=models.ManyToManyField(User,blank=True,related_name="downloaded_by")


    class Meta:
        index_together = ('id', 'slug')
        ordering = ('-created',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_detail',kwargs={'slug':self.slug})




