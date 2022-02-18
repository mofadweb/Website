from django.contrib import admin
from .models import Contact, Report, Agency, AgencyDivision, AgencyLeader, Project

models = [Contact, Report, Agency, AgencyDivision, AgencyLeader, Project]

for models in models:
    admin.site.register(models)
