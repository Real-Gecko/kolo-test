from django.contrib.auth.views import LoginView
from django.urls import path

from jff import views

app_name = "jff"

urlpatterns = [
    path("accounts/login/", LoginView.as_view(template_name="jff/form.html"), name="login"),
    path("", views.IndexView.as_view(), name="index"),
    path("company/", views.CompanyList.as_view(), name="company_list"),
    path("company/create/", views.CompanyCreate.as_view(), name="company_create"),
    path("company/<int:pk>/update/", views.CompanyUpdate.as_view(), name="company_update"),
    path("office/", views.OfficeList.as_view(), name="office_list"),
    path("office/create/", views.OfficeCreate.as_view(), name="office_create"),
    path("office/<int:pk>/update/", views.OfficeUpdate.as_view(), name="office_update"),
]
