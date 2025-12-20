from django.db import models

class Category(models.Model):
    # (Assuming your Category model looks something like this)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    
    # ForeignKey to Category
    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="products"
    )
    
    # DecimalField requires max_digits and decimal_places
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Optional fields (blank=True allows empty in forms, null=True for database)
    description = models.TextField(blank=True, null=True)
    
    # ImageField with specific upload path
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name