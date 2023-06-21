from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from user.models import Admin


class Category (models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models. TextField(null=True, blank=True)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)



# User class model
class Product(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    brand = models.CharField(max_length=50, null=False, blank=False, unique=True)
    instock = models.CharField(max_length=128,null=False, blank=False,)
    discountpercentage = models.CharField(max_length=128,null=False, blank=False,)
    thumbnail = models.ImageField(upload_to='product_images/', null=True, blank=True)
    category = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='products') 
    
    def set_password(self, raw_password):
        # Use make_password to hash the raw password
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        # Use check_password to compare the raw password to the hashed password
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username

# Author class model inhariting from the user
class Author(User):
    title = models.CharField(max_length=60, null=True, blank=True)
    bio = models. TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_images/', null=True, blank=True)

# Reader class model inhariting from the user
class Reader(User):
    pass

# Book classs model
class Book(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=500, null=True)

    # books of the author in books
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books') 

    book_cover = models.ImageField(upload_to='book_images/', null=True, blank=True)
    publication_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title

# many to many relationship between readers and books 
class Reader_books(models.Model):
    reader = models.ForeignKey(Reader, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

# book pages class model
class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='pages')
    page_number = models.IntegerField()
    content = models.TextField()

    def __str__(self):
        return f"{self.book.title} - Page {self.page_number}"