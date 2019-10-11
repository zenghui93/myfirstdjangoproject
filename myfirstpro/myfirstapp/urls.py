from . import views
from .api import CategoryViewSet, ListViewSet, RecordViewSet
from django.conf.urls import url
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter





router = DefaultRouter()
router.register(r'lists', ListViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'records', RecordViewSet)


urlpatterns = router.urls + [
    url(r'^home', TemplateView.as_view(template_name="myfirstapp/home.html")),

]


