from django.contrib import admin
from .models  import ProductModel,CategoryModel,Order

# Register your models here.
# class ProductAdminTable(admin.TabularInline):
#     model = ProductModel


# class CateogoryAdminTable(admin.TabularInline):
#     model = CategoryModel

# class OrderAdminTabel(admin.TabularInline):
#     model = OrderModel

class ProductAdmin(admin.ModelAdmin):
    # inlines=[ProductAdminTable]
    list_display=['__str__','product_name', 'description', 'price','CategoryModel']
    # search_fields=['user__product_name', 'user__description']
    class Meta:
        model=ProductModel

class CategoryAdmin(admin.ModelAdmin):
    # inlines=[CateogoryAdminTable]
    list_display=['__str__','category_name', 'description']
    # search_fields=['category_name', 'description']
    class Meta:
        model=ProductModel

class OrderAdmin(admin.ModelAdmin):
    # inlines=[OrderAdminTabel]
    list_display=['__str__','customername', 'customeremail','product','quantity']
    # search_fields=['category_name', 'description']
    class Meta:
        model=Order

admin.site.register(CategoryModel,CategoryAdmin)
admin.site.register(ProductModel,ProductAdmin)
admin.site.register(Order,OrderAdmin)