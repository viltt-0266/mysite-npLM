from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

admin.site.register (Book)
admin.site.register (Author)
admin.site.register (Genre)
admin.site.register (BookInstance)
# admin.site.register(Author)
# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
