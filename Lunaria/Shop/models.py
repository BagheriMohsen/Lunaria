from django.db import models
from django.db.models import Model
from tinymce import models as tinymce_models
# Create your models here.
class Product(Model):
    title       =   models.CharField(max_length=255,verbose_name="نام محصول")
    slug        =   models.SlugField(editable=False)
    desc        =   models.TextField(verbose_name="توضیحات",help_text="توضیحات جزئی برای نمایش یادداشت کنید")
    body        =   tinymce_models.HTMLField(verbose_name="محتوی")
    created_at  =   models.DateField(auto_now_add=True,verbose_name="تاریخ ایجاد")
    updated_at  =   models.DateField(auto_now=True,verbose_name="تاریخ ویرایش")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name="محصول"
        verbose_name_plural="محصولات"
