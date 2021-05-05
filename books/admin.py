from django.contrib import admin

# Register your models here.
from .models import Category,Book,Notes,ContactUs,ClassCR

# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name', 'slug')
#     prepopulated_fields = {'slug': ('name',)}
#     list_per_page = 24
#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'availibility', 'updated', 'created')
#     prepopulated_fields = {'slug': ('name',)}
#     raw_id_fields = ('category',)
#     list_editable = ('price', 'availibility')
#     list_per_page = 24

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(ContactUs)
admin.site.register(ClassCR)