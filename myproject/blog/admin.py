from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Post, Comment


# Если вы хотите настроить интерфейс администратора для пользователей, создайте класс UserAdmin
class UserAdmin(BaseUserAdmin):
    # Настройте здесь атрибуты класса UserAdmin, если это необходимо
    pass


# Зарегистрируйте модель User с использованием настроенного класса UserAdmin
admin.site.register(User, UserAdmin)


# Регистрация других моделей
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')
    list_filter = ('author', 'created_at')
    date_hierarchy = 'created_at'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_at')
    search_fields = ('post__title', 'author__username')
    list_filter = ('author', 'created_at')
    date_hierarchy = 'created_at'
