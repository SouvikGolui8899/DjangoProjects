from django.db import models

from django.urls import reverse

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.__class__.__name__}<{self.id}, {self.title}>"

    def __repr__(self):
        return self.__str__()

    def get_absolute_url(self):
        return reverse("articles:article_detail", kwargs={"id": self.id})
