from django.urls import path
from app import views
from rest_framework.authtoken.views import obtain_auth_token 

  
urlpatterns = [
       path('saveusername/',views.save_username),
       path('delete/<str:pk>/',views.eventdelete),
       path('update/<str:pk>/',views.eventupdate),
       # path('gettoken/', obtain_auth_token, name='api_token_auth'),  
]