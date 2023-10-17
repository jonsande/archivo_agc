from django.contrib import admin
from .models import Article, Slug, Category

# Register your models here.

class TertuliaAdmin(admin.ModelAdmin):
    list_filter = ['new_cod', 'status', "categories"]
    #list_display = ['new_cod','old_cod','title','status']
    list_display = ['new_cod','old_cod','title','status', "get_categories"]
    search_fields = ['new_cod', 'old_cod', 'cuerpo']
    readonly_fields = ("created", "updated")

    def get_categories(self, obj):
            # TODO: ponerle un verbose_name a este 'get_categories', para que la
            # columna correspondiente del panel de administración diga 'Categorías'
            return ", ".join([str(i) for i in obj.categories.all()])

    get_categories.short_description = 'Categorias'

admin.site.register(Article, TertuliaAdmin)

admin.site.register(Slug)

class CategoryAdmin(admin.ModelAdmin):
      list_display = ['name', 'parent']
      list_filter = ['name', 'parent']
      search_fields = ['name', 'parent']

admin.site.register(Category, CategoryAdmin)