from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField


class Board(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(default="will-be-added-when-saved")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["date"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Board, self).save(*args, *kwargs)

    def get_absolute_url(self):
        return reverse("board-detail", kwargs={"slug": self.slug})


class Leader(models.Model):
    name = models.CharField(max_length=70)
    image = models.FileField(null=True, upload_to="leader_images")
    board = models.ForeignKey("Board", on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=255)
    bio = RichTextField()
    feature = models.BooleanField(default=False)
    slug = models.SlugField(default="will-be-added-when-saved")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.board} | {self.role}"

    class Meta:
        ordering = ["date"]

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.board) + " - " + str(self.pk))
        return super(Leader, self).save(*args, *kwargs)
