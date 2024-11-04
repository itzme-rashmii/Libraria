from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.signin, name="signin"),  # Added trailing slash
    path('logout/', views.signout, name="signout"),  # Added trailing slash
    path('registration/', views.registration, name="registration"),  # Added trailing slash
    path('book/<int:id>/', views.get_book, name="book"),  # Added trailing slash
    path('books/', views.get_books, name="books"),  # Added trailing slash
    path('category/<int:id>/', views.get_book_category, name="category"),  # Added trailing slash
    path('writer/<int:id>/', views.get_writer, name="writer"),  # Added trailing slash
]
