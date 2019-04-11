from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_pk>/',views.update_comment,name='update_comment'),
]