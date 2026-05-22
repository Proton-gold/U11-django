from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    publish_date = models.DateField(auto_now=True)

    class Meta:
        db_table = 'book'


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order'
