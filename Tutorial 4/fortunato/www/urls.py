from django.conf.urls import url

from .views import IndexTemplateView

urlpatterns = [
    url(r'^', IndexTemplateView.as_view()),
]
