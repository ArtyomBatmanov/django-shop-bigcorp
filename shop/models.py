import random
import string


from django.db import models
from django.utils.text import slugify
from django.urls import reverse


def random_slug():
    return "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(3))


class Category(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=256, db_index=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="Категория", related_name="children",
                               blank=True, null=True)
    slug = models.SlugField(verbose_name="URL", max_length=256, unique=True, null=False, editable=True)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    class Meta:
        unique_together = (["slug", "parent"])
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        full_path = [self.name]
        key = self.parent
        while key is not None:
            full_path.append(key.name)
            key = key.parent
        return " > ".join(full_path[::-1])

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(random_slug() + "-pickBetter" + self.name)
        super(Category, self).save(*args, **kwargs)

    #
    # def get_absolute_url(self):
    #     return reverse()
# Create your models here.
