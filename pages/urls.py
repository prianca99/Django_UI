from django.urls import path , include
from django.conf.urls.static import static
from pages import views


urlpatterns = [
    path('', views.index ,name='index'),
    path('about', views.about ,name='about'),
    path('login', views.login, name="login" ),
    path('landing', views.landing, name='landing'),
    path('logout' , views.logout, name='logout'),
    path('external',views.external, name='external'),
    path('view_all',views.view_all, name='view_all'),
    path('delete/<UserRequests_id>',views.delete,name='delete'),
    # path('edit/<UserRequests_id>',views.edit,name='edit'),
    #path('', views.login, name='login'),
]