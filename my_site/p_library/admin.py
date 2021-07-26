from django.contrib import admin
from p_library.models import Book, Author, PublishingHouse, Friend

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name', 'friend',)
    fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price', 'publishing_house', 'friend')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(PublishingHouse)
class PublishingHouse(admin.ModelAdmin):
    pass

@admin.register(Friend)
class Friend(admin.ModelAdmin):
    pass