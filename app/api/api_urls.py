from django.contrib import admin
from django.urls import path, include
from . import views
from api.serialize import ProvinsiApiVview, KabupatenApiView
from api.serialize import KecamatanApiView, KelurahanApiView
from rest_framework import routers

router = routers.DefaultRouter()
router.register('list-provinsi', ProvinsiApiVview, basename="list-provinsi")

urlpatterns = [
    path('', include(router.urls)),
    path('list-kabupaten/<provinsi>/', KabupatenApiView.as_view()),
    path("list-kecamatan/<kabupaten>/", KecamatanApiView.as_view(), name="list-kecamatan"),
    path("list-kelurahan/<kecamatan>/", KelurahanApiView.as_view(), name="list-kelurahan")
]   


