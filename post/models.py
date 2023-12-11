from django.db import models

# Create your models here.

class Product(models.Model):
    image=models.ImageField(upload_to='posts', null=True, blank=True)
    title=models.CharField(max_length=255)
    description=models.TextField()
    price=models.FloatField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f"{self.id}{self.title}"
    
class Category(models.Model):
    product=models.ForeignKey('post.Product', on_delete=models.CASCADE, related_name='categories')
    name=models.CharField(max_length=255)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    product=models.ForeignKey('post.Product', on_delete=models.CASCADE, related_name='reviews')
    rate=models.FloatField(default=0)
    text=models.TextField()

    
# product=Product.objects.get(id=1)
# product.categories

# category=Category.objects.get(id=1)

# class Categoryy(models.Model):
#     parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
#     title = models.CharField(max_length=100)