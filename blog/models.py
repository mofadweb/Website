from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    POST_TYPE = (
        ("Blog", "Blog"),
        ("Press release", "Press release"),
    )
    type = models.CharField(choices=POST_TYPE, default="Blog", max_length=25)
    title = models.CharField(max_length=255)
    image = models.FileField(null=True, upload_to="post_images")
    text = RichTextUploadingField()
    created_at = models.DateTimeField(default=timezone.now)
    slug = models.SlugField(default="will-be-added-when-saved")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"slug": self.slug})

    def get_press_url(self):
        return reverse("press-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.created_at)
        return super(Post, self).save(*args, *kwargs)
