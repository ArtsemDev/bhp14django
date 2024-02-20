from datetime import datetime
from typing import TYPE_CHECKING

from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils.timezone import now


class Category(models.Model):
    if TYPE_CHECKING:
        name: str
        slug: str
    else:
        name = models.CharField(
            max_length=32,
            null=False,
            blank=False,
            unique=True,
            help_text="Название категории",
            verbose_name="название",
            validators=[
                validators.MinLengthValidator(limit_value=2)
            ]
        )
        slug = models.SlugField(
            max_length=32,
            null=False,
            blank=False,
            unique=True,
            help_text="Ссылка",
            verbose_name="Ссылка",
            validators=[
                validators.MinLengthValidator(limit_value=2)
            ]
        )

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"
        # abstract = True
        # managed = False
        # ordering = ["-name"]
        # db_table = "blog_category"
        # db_table_comment = "Topics Category"


class Topic(models.Model):
    if TYPE_CHECKING:
        title: str
        body: str
        slug: str
        date_created: datetime
        category: Category
        category_id: int
        is_published: bool
    else:
        tag = models.CharField(max_length=32, null=True, blank=True)
        title = models.CharField(
            max_length=128,
            null=False,
            blank=False,
            help_text="Заголовок поста",
            verbose_name="заголовок",
            validators=[
                validators.MinLengthValidator(limit_value=2)
            ]
        )
        body = models.TextField(
            null=False,
            blank=False,
            help_text="Тест поста",
            verbose_name="текст"
        )
        slug = models.SlugField(
            max_length=128,
            null=False,
            blank=False,
            unique=True,
            help_text="URL",
            verbose_name="URL",
            validators=[
                validators.MinLengthValidator(limit_value=2)
            ]
        )
        date_created = models.DateTimeField(
            verbose_name="дата создания",
            default=now
        )
        category = models.ForeignKey(
            to="Category",
            on_delete=models.PROTECT,
            verbose_name="категория",
            help_text="Категория поста",
            db_index=True
        )
        is_published = models.BooleanField(
            default=False,
            verbose_name="опубликован",
            help_text="Опубликован",
            null=False,
            blank=False,
            db_index=True
        )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "пост"
        verbose_name_plural = "посты"
        ordering = ["category", "date_created"]
        # indexes = [
        #     models.Index(fields=["category", "is_published"])
        # ]

    def get_absolute_url(self) -> str:
        return reverse(viewname="topic_detail", kwargs={"slug": self.slug})
