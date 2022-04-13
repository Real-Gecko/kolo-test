from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from jff import models
from jff.forms import OfficeForm


class IndexView(TemplateView):
    template_name = "jff/index.html"


class CompanyList(ListView):
    model = models.Company
    template_name = "jff/list.html"


class CompanyCreate(CreateView):
    model = models.Company
    fields = "__all__"
    template_name = "jff/form.html"
    success_url = reverse_lazy("jff:company_list")


class CompanyUpdate(UpdateView):
    model = models.Company
    fields = "__all__"
    template_name = "jff/form.html"
    success_url = reverse_lazy("jff:company_list")


class OfficeList(ListView):
    model = models.Office
    template_name = "jff/list.html"
    success_url = reverse_lazy("jff:office_list")


class OfficeCreate(CreateView):
    model = models.Office
    form_class = OfficeForm
    template_name = "jff/form.html"
    success_url = reverse_lazy("jff:office_list")


class OfficeUpdate(UpdateView):
    model = models.Office
    form_class = OfficeForm
    template_name = "jff/form.html"
    success_url = reverse_lazy("jff:office_list")
    title = "Office update"
