from django.urls import reverse_lazy
from django.views.generic import *
from django.core.mail import send_mail

from .forms import FeedbackForm
from .models import Topic


class TopicListView(ListView):
    model = Topic
    template_name = "blog/index.html"
    paginate_by = 5
    extra_context = {
        "heading": "Main Page",
        "header_image": 'blog/assets/img/home-bg.jpg'
    }


class TopicDetailView(DetailView):
    model = Topic
    template_name = "blog/post.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["heading"] = context.get("topic").title
        context["header_image"] = "blog/assets/img/post-sample-image.jpg"
        return context


class ContactFormView(FormView):
    template_name = "blog/contact.html"
    extra_context = {
        "heading": "Contact Page",
        "header_image": 'blog/assets/img/home-bg.jpg'
    }
    form_class = FeedbackForm
    success_url = reverse_lazy("contact")

    def form_valid(self, form: FeedbackForm):
        send_mail(
            subject="Feedback",
            message=form.data.get("message"),
            from_email=None,
            recipient_list=[form.data.get("email")]
        )
        return super().form_valid(form=form)
