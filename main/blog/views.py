from django.http import HttpRequest
from django.views.generic import *

from .models import Category
from .forms import FeedbackForm, CategoryForm


class CategoryListView(ListView):
    model = Category
    queryset = model.objects.all()
    template_name = "blog/category_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.GET.get("q"):
            queryset = queryset.filter(name__icontains=self.request.GET.get("q"))
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["title"] = "Category List"
        context["feedback_form"] = FeedbackForm()
        context["category_form"] = CategoryForm()
        return context

    def post(self, request: HttpRequest):
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            ...
        return self.get(request=request)


class CategoryDetailView(DetailView):
    model = Category
    template_name = "blog/category_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        return context
