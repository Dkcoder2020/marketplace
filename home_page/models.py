from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField

# Create your models here.

class Title(models.Model):
    category_title = models.CharField(_("Category Title"),max_length=250,blank=True,null=True)

    def __str__(self):
        return self.category_title

class TotalSales(models.Model):
     sales = models.IntegerField(_("Sales"),default=0,blank=True,null=True)

     def __str_(self):
        return str(self.sales)

class Category(models.Model):
    cat_title =models.ForeignKey(Title, on_delete=models.CASCADE,null=True)
    total_sales = models.ForeignKey(TotalSales, on_delete=models.CASCADE,null=True)
    image = models.ImageField(blank=True,null=True,upload_to='Product_Category')
    heading = models.CharField(_("Product Heading"),max_length=250,blank=True,null=True)
    discription = RichTextField(_("Discription"),blank=True,null=True)
    price = models.IntegerField(_("Price"),default=0,blank=True,null=True)

    def __str__(self):
        return self.heading
    

class Banner(models.Model):
    heading = models.CharField(max_length=250,blank=True,null=True)
    discription = RichTextField(blank=True,null=True)
    image = models.ImageField(blank=True,null=True,upload_to='Banner')

    def __str__(self):
        return self.heading

   

    




