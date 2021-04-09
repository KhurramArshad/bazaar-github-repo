from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)


    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title


# class CustomCatItemsManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(status='published')


class Cat_items(models.Model):
    ITEM_STATUS_CHOICES = (('draft', 'Draft'), ('published', 'Published'))
    name = models.CharField(max_length=256)
    pid = models.CharField(max_length=256)
    actual_price = models.FloatField()
    discounted_price = models.FloatField()
    desc = models.TextField()
    image = models.ImageField(upload_to='static/home/images')
    slug = models.SlugField(max_length=264, unique_for_date='publish')
    category = models.ForeignKey(Category, related_name='cat_items', on_delete=models.CASCADE)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=ITEM_STATUS_CHOICES, default='draft')

    #objects = CustomCatItemsManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('item_detail', args=[self.slug])

class Comments(models.Model):
    item = models.ForeignKey(Cat_items, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='commentator')
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Commented by {} on {}'.format(self.user,self.item)




