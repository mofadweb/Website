from django.shortcuts import render, redirect
from django.views import generic
from django.contrib import messages

from .models import Contact, Report, Agency
from leadership.models import Leader
from .forms import ContactForm

from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def ContactView(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Message sent successfully!")
            return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "archives/contact.html", {"form": form})


@login_required
def ContactPanel(request):
    unread = Contact.objects.filter(is_read=False)
    read = Contact.objects.filter(is_read=True)
    all = Contact.objects.all()
    context = {"unread_messages": unread, "read_messages": read, "all_messages": all}
    return render(request, "archives/contact_panel.html", context)


class ContactDetailView(LoginRequiredMixin, generic.View):
    def get(self, request, *args, **kwargs):
        if "slug" in self.kwargs:
            message = Contact.objects.get(slug=self.kwargs["slug"])
            message.is_read = True
            message.save()
            message.refresh_from_db()
        context = {"message": message}
        return render(request, "archives/contact_detail.html", context)


def ReportList(request):
    budget = Report.objects.filter(type="Budget Statement")
    nec = Report.objects.filter(type="NEC & G.A Meeting")
    financial = Report.objects.filter(type="Financial Statement")
    context = {"budgets": budget, "meetings": nec, "financial": financial}
    return render(request, "archives/reports.html", context)


class ReportDetailView(generic.DetailView):
    model = Report
    template_name = "archives/report_detail.html"
    context_object_name = "report"


class Agencies(generic.ListView):
    model = Agency
    template_name = "archives/agencies.html"
    context_object_name = "agencies"
    paginate_by = 12


class AgencyDetail(generic.DetailView):
    model = Agency
    template_name = "archives/agency_detail.html"
    context_object_name = "agency"


def AboutView(request):
    leader_list = Leader.objects.filter(feature=True)[:3]
    context = {"leaders": leader_list}
    return render(request, "archives/about.html", context)
