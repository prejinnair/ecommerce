from django.db import models

# Create your models here.
from django.urls import reverse


class category(models.Model):
    name =models.CharField(max_length=250,unique=True)
    slug = models.SlugField(max_length=250,unique=True)
    desc=models.TextField(null=True)
    image=models.ImageField(upload_to='category',null=True)

    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def __str__(self):
        return '{}'.format(self.name)

    def get_url(self):
        return reverse('shopapp:products_by_category',args=[self.slug])

class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    desc = models.TextField(null=True)
    image = models.ImageField(upload_to='products', null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated= models.DateTimeField(auto_now=True)
    def get_url(self):
        return reverse('shopapp:procatdetails',args=[self.category.slug,self.slug])
    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'


    def __str__(self):
        return '{}'.format(self.name)

