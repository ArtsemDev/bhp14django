from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_GET

from .models import Category


@require_GET
def category_list(request: HttpRequest):
    objs = Category.objects.all()
    return JsonResponse(data={"result": [{"id": obj.id, "name": obj.name, "slug": obj.slug} for obj in objs]})
