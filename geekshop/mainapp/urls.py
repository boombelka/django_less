from django.urls import path
import authapp.views as authapp
import mainapp.views as mainapp


app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.products, name='index'),
   path('<int:pk>/', mainapp.products, name='category'),
   path('logout/', authapp.logout, name='logout'),
   path('login/', authapp.EditViews.as_view, name='edit'),
   path('edit/<int:pk>/', authapp.EditViews.as_view(), name='edit'),
   path('register/', authapp.register, name='register'),
]