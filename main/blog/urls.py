from django.urls import path

# from blog.views import category_list, category_detail
from .views import *


urlpatterns = [
    # path("api/v1/categories/<int:pk>/", category_detail),
    # path("api/v1/categories/", category_list,)
    # path("categories/<slug:slug>/", CategoryDetailView.as_view()),
    # path("categories/", CategoryListView.as_view()),
    path("contact/", ContactFormView.as_view(), name="contact"),
    path("<slug:slug>/", TopicDetailView.as_view(), name="topic_detail"),
    path("", TopicListView.as_view(), name="index"),
]
