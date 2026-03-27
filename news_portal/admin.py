from django.contrib import admin
from .models import Category, Post, PostCategory

# 1. Создаем Inline класс для связи
class PostCategoryInline(admin.TabularInline):
    model = PostCategory
    extra = 1  # Количество пустых строк для новых категорий

# 2. Настраиваем админку поста
class PostAdmin(admin.ModelAdmin):
    # Убираем filter_horizontal, он тут не сработает
    inlines = [PostCategoryInline]

# 3. Регистрируем
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
