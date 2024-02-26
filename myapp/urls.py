from django.urls import path
from myapp import views


urlpatterns = [
   path("",views.home, name ='home'),
   path('processamento/', views.processamento, name ='processamento')
]
