from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from . import views
#from views import IndexView, EmploginView,EmplogoutView ,UserloginView, EmpsignupView, UsersignupView,UserslogoutView

urlpatterns = [
    path('',views.IndexView,name='indexview'),
    path('index',views.IndexView,name='indexview'),
    path('emp_signup',views.EmpsignupView,name='empsignupview'),
    path('emp_login',views.EmploginView,name='emploginview'),
    path('emp_logout',views.EmplogoutView,name='emplogoutview'),
    path('emp_chgpasswd',views.EmpchgpasswdView,name='emp_chgpasswd'),
    path('user_login',views.UserloginView,name='usersloginview'),
    path('user_signup',views.UsersignupView,name='usersignupview'),
    path('user_logout',views.UserslogoutView,name='userslogoutview'),
] #+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)