from django.urls import path
from . import views

app_name = "catalog"

# urlpatterns = [
#      # path('', views.index, name='index'), # for Function
#      path('', views.Index.as_view(), name='index'), # for template
# ]

urlpatterns = [
    # path('', views.index, name='index'), # for Function
    path('', views.Index.as_view(), name='index'), # for template
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),

    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),

    path('book/<slug:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),

    path('author/create/', views.AuthorCreate.as_view(), name='author_create'),
    path('author/<int:pk>/update/', views.AuthorUpdate.as_view(), name='author_update'),
    path('author/<int:pk>/delete/', views.AuthorDelete.as_view(), name='author_delete'),
]
