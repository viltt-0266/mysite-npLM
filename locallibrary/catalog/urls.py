from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', include([
        path('', views.BookListView.as_view(), name='books'),
        path('<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
        path('<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
        path('<int:pk>/update/', views.BookUpdate.as_view(), name='book-update'),
        path('<int:pk>/delete/', views.BookDelete.as_view(), name='book-delete'),
        path('create/', views.BookCreate.as_view(), name='book-create'),
    ])),
    path('authors/', include([
        path('', views.AuthorListView.as_view(), name='authors'),
        path('<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
        path('<int:pk>/update/', views.AuthorUpdate.as_view(), name='author-update'),
        path('<int:pk>/delete/', views.AuthorDelete.as_view(), name='author-delete'),
        path('create/', views.AuthorCreate.as_view(), name='author-create'),
    ])),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('allbooks/', views.LoanedBooksByStaffListView.as_view(), name='all-borrowed'),
]


