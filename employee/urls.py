from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.Index,name='emp_index'),
    path('addbook/',views.AddBookView,name='addbookview'),
    path('showbooks/',views.ShowBookView,name='showbookview'),
    # path('header',views.Header,name='header'),
    path('deletebooks/<int:id>',views.DeleteBookView,name='deleteBook'),
    path('editbook/<int:id>',views.EditBookView,name='editbookview'),
    path('exitingusers/',views.ExistingUserView,name='existinguserview'),
]