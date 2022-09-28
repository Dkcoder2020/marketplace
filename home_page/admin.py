from django.contrib import admin
from home_page.models import Title,TotalSales,Category,Banner

# Register your models here.

class TitleAdmin(admin.ModelAdmin):
    model = Banner
    list_display = ['category_title']
admin.site.register(Title,TitleAdmin)


class TotalSalesAdmin(admin.ModelAdmin):
    model = TotalSales
    list_display = ['sales']
admin.site.register(TotalSales,TotalSalesAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['get_title','total_sales','heading','discription','price']
    
    def get_title(self,obj):
        return obj.cat_title.category_title

admin.site.register(Category,CategoryAdmin)

class BannerAdmin(admin.ModelAdmin):
    model = Banner
    list_display = ['heading','discription','image']

admin.site.register(Banner,BannerAdmin)



