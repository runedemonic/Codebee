from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:study_pk>', views.detail, name='detail'),
    path('<int:study_pk>/update', views.update, name='update'),
]