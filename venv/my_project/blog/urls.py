# pages/urls.py
from django.urls import path

from .views import blog_post_detail_page

urlpatterns = [
    path('', blog_post_detail_page),



]