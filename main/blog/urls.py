from django.urls import path

from blog.views import category_list

urlpatterns = [
    path("api/v1/categories/", category_list)
]
