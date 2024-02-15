from django.urls import path

# from blog.views import category_list, category_detail
from .views import CategoryListView, CategoryDetailView


urlpatterns = [
    # path("api/v1/categories/<int:pk>/", category_detail),
    # path("api/v1/categories/", category_list,)
    path("categories/", CategoryListView.as_view()),
    path("categories/<slug:slug>/", CategoryDetailView.as_view()),
]
