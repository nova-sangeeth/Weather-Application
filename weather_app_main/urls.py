from django.conf.urls import url

from .views import index, delete

urlpatterns = [
    url(r"^$", index, name="index"),
    url(r"^delete/(?P<pk>\d+)$", delete, name="delete"),
]

