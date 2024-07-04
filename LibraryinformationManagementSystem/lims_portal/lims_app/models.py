
from django.db import models


# Create your models here.
class reader(models.Model):
    def __str__(self):
        return self.reference_name
    reference_id=models.CharField(max_length=200)
    reference_name=models.CharField(max_length=200)
    reference_contact=models.CharField(max_length=200)
    reader_address=models.TextField()
    active=models.BooleanField(default=True)
    
class LoanDetail(models.Model):
    tc = models.CharField(max_length=11)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    book = models.CharField(max_length=255)
    date = models.DateField()

    def __str__(self):
        return f"{self.tc} - {self.name} {self.surname} - {self.book}"

class Record(models.Model):
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=255)
    due_date = models.DateField()
    return_date = models.DateField()
    penalty = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"ID: {self.id}, Kitap Adı: {self.book_name}, Son Teslim Tarihi: {self.due_date}, Teslim Edilen Tarih: {self.return_date}, Ceza: {self.penalty}"

class Bookso(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    publish_date = models.DateField()
    page_count = models.IntegerField()
    book_code = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to='book_covers/', blank=True, null=True)

    def __str__(self):
        return self.title