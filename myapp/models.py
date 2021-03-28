from django.db import models

# Create your models here.

#tao table
class Library(models.Model):
    store_name = models.CharField('Ten thu vien', max_length=100)
    store_addr = models.CharField('Dia chi', max_length=100)
    class Meta:
        db_table = "Library"

class Book(models.Model):
    book_name = models.CharField('Ten sach', max_length=100)
    book_price = models.CharField('Gia sach', max_length=100)
    book_actor = models.CharField('Nha xuat ban', max_length=100)
    store = models.ForeignKey(Library,default='1' , on_delete= models.CASCADE)
    class Meta:
        db_table = "Book"


    