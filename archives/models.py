from django.db import models
from django.utils import timezone
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    subject = models.CharField(max_length=200)
    message = RichTextField()

    is_read = models.BooleanField(default=False)

    slug = models.SlugField(default="")
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.name + " - " + self.subject

    def get_absolute_url(self):
        return reverse("contact-detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.date)
        return super(Contact, self).save(*args, **kwargs)


class Report(models.Model):
    REPORT_TYPE = (
        ("Financial statement", "Financial statement"),
        ("Research report", "Research report"),
        ("Developmental report", "Developmental report"),
    )
    type = models.CharField(choices=REPORT_TYPE, default="Budget", max_length=25)
    date = models.DateTimeField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    text = RichTextUploadingField()
    by = models.CharField(default="", max_length=80)
    slug = models.SlugField(default="Will-be-added-when-saved")

    def __str__(self):
        return (
            self.type
            + " - "
            + self.date.strftime("%B")
            + ", "
            + self.date.strftime("%Y")
        )

    class Meta:
        ordering = ["-date"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.time)
        return super(Report, self).save(*args, *kwargs)

    def get_absolute_url(self):
        return reverse("report-detail", kwargs={"slug": self.slug})


class Agency(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(null=True, upload_to="agency_images")
    bio = RichTextUploadingField()
    created = models.DateTimeField(default=timezone.now, null=True, blank=True)
    slug = models.SlugField(default="Will-be-added-when-saved")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.created)
        return super(Agency, self).save(*args, *kwargs)

    def get_absolute_url(self):
        return reverse("agency-detail", kwargs={"slug": self.slug})


class AgencyLeader(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    image = models.FileField(null=True, upload_to="agencyLeader_images")
    position = models.CharField(max_length=150)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.agency} | {self.name} - {self.position}"

    class Meta:
        ordering = ["date"]


class AgencyDivision(models.Model):
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    role = models.TextField()

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=225)
    image = models.FileField(null=True, upload_to="project_images")
    details = RichTextUploadingField()
    created = models.DateTimeField(default=timezone.now, null=True, blank=True)
    slug = models.SlugField(default="Will-be-added-when-saved")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.created)
        return super(Project, self).save(*args, *kwargs)
